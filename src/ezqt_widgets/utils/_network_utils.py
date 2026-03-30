# ///////////////////////////////////////////////////////////////
# NETWORK_UTILS - Qt Network Helpers
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Qt network helper utilities.

Provides small utilities for fetching icon bytes using QtNetwork, which
respects system proxy settings by default.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Third-party imports
from PySide6.QtCore import QEventLoop, QObject, QTimer, QUrl, Signal
from PySide6.QtNetwork import (
    QNetworkAccessManager,
    QNetworkProxyFactory,
    QNetworkReply,
    QNetworkRequest,
)

# FUNCTIONS
# ///////////////////////////////////////////////////////////////


_network_manager_cache: dict[str, QNetworkAccessManager] = {}


def _get_network_manager() -> QNetworkAccessManager:
    if "instance" not in _network_manager_cache:
        QNetworkProxyFactory.setUseSystemConfiguration(True)
        _network_manager_cache["instance"] = QNetworkAccessManager()
    return _network_manager_cache["instance"]


class UrlFetcher(QObject):
    """Fetch URL data using QtNetwork and emit a signal on completion."""

    fetched = Signal(str, object)

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self._pending: dict[QNetworkReply, QTimer] = {}

    def fetch(self, url: str, timeout_ms: int = 5000) -> None:
        """Fetch bytes asynchronously and emit a signal on completion.

        Args:
            url: The URL to fetch.
            timeout_ms: Timeout in milliseconds (default: 5000).
        """
        if not url:
            self.fetched.emit(url, None)
            return

        manager = _get_network_manager()
        request = QNetworkRequest(QUrl(url))
        reply = manager.get(request)

        timer = QTimer(self)
        timer.setSingleShot(True)

        def _cleanup(data: bytes | None) -> None:
            if reply in self._pending:
                self._pending.pop(reply, None)
            timer.stop()
            timer.deleteLater()
            reply.deleteLater()
            self.fetched.emit(url, data)

        def _on_timeout() -> None:
            reply.abort()
            _cleanup(None)

        def _on_finished() -> None:
            if reply.error() != QNetworkReply.NetworkError.NoError:
                _cleanup(None)
                return
            data = bytes(reply.readAll().data())
            _cleanup(data)

        timer.timeout.connect(_on_timeout)
        reply.finished.connect(_on_finished)
        timer.start(timeout_ms)
        self._pending[reply] = timer


def fetch_url_bytes(url: str, timeout_ms: int = 5000) -> bytes | None:
    """Fetch bytes from a URL using QtNetwork.

    Args:
        url: The URL to fetch.
        timeout_ms: Timeout in milliseconds (default: 5000).

    Returns:
        The response bytes, or None on error/timeout.
    """
    if not url:
        return None

    manager = _get_network_manager()
    request = QNetworkRequest(QUrl(url))
    reply = manager.get(request)

    loop = QEventLoop()
    timer = QTimer()
    timer.setSingleShot(True)
    timer.timeout.connect(loop.quit)
    reply.finished.connect(loop.quit)

    timer.start(timeout_ms)
    loop.exec()

    if timer.isActive() and reply.error() == QNetworkReply.NetworkError.NoError:
        data = bytes(reply.readAll().data())
        reply.deleteLater()
        return data

    reply.abort()
    reply.deleteLater()
    return None


# ///////////////////////////////////////////////////////////////
# PUBLIC API
# ///////////////////////////////////////////////////////////////

__all__ = ["UrlFetcher", "fetch_url_bytes"]
