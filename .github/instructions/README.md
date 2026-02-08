# ezqt_widgets - Guide de Projet

Guide de reference pour comprendre, maintenir et faire evoluer la bibliotheque **ezqt_widgets**.
Ce document decrit la structure du projet, ses conventions et les pratiques a suivre pour
contribuer dans la continuite de l'existant.

---

## Vue d'ensemble

**ezqt_widgets** est une bibliotheque Python de widgets Qt personnalises pour PySide6.
Elle fournit des composants graphiques reutilisables, animes et types pour le
developpement d'interfaces desktop modernes.

| Donnee        | Valeur                                     |
| ------------- | ------------------------------------------ |
| Python        | >= 3.10                                    |
| Framework Qt  | PySide6 >= 6.7.3, < 7.0.0                  |
| Build backend | setuptools (PEP 517)                       |
| Licence       | MIT                                        |
| Statut        | Production/Stable                          |
| Configuration | `pyproject.toml` (source unique de verite) |

---

## Hierarchie des instructions

Les fichiers d'instructions du projet sont organises par priorite decroissante :

1. **Ce fichier** (`README.md`) - Contexte projet et architecture
2. `core/advanced-cognitive-conduct.instructions.md` - Principes de raisonnement
3. `languages/python/python-development-standards.instructions.md` - Standards Python
4. `languages/python/python-formatting-standards.instructions.md` - Formatage et sections
5. `languages/python/pyproject-standards.instructions.md` - Standards pyproject.toml
6. `CLAUDE.md` (racine) - Preferences specifiques a Claude
7. `AGENTS.md` (racine) - Instructions generales pour agents IA

En cas de conflit, le fichier le plus haut dans cette liste prevaut.

---

## Architecture du projet

### Arborescence

```text
ezqt_widgets/
├── ezqt_widgets/              # Package principal
│   ├── __init__.py            # Exports publics + metadata
│   ├── button/                # Module boutons (3 widgets)
│   │   ├── __init__.py
│   │   ├── date_button.py     # DateButton, DatePickerDialog
│   │   ├── icon_button.py     # IconButton
│   │   └── loader_button.py   # LoaderButton
│   ├── input/                 # Module saisie (4 widgets)
│   │   ├── __init__.py
│   │   ├── auto_complete_input.py
│   │   ├── password_input.py
│   │   ├── search_input.py
│   │   └── tab_replace_textedit.py
│   ├── label/                 # Module labels (4 widgets)
│   │   ├── __init__.py
│   │   ├── clickable_tag_label.py
│   │   ├── framed_label.py
│   │   ├── hover_label.py
│   │   └── indicator_label.py
│   ├── misc/                  # Module utilitaires (6 widgets)
│   │   ├── __init__.py
│   │   ├── circular_timer.py
│   │   ├── draggable_list.py
│   │   ├── option_selector.py
│   │   ├── toggle_icon.py
│   │   └── toggle_switch.py
│   └── cli/                   # Interface CLI (Click)
│       ├── __init__.py
│       ├── main.py
│       └── runner.py
├── tests/                     # Tests unitaires
│   ├── conftest.py            # Fixtures pytest partagees
│   ├── run_tests.py           # Script d'execution
│   └── unit/                  # Miroir de la structure du package
│       ├── test_button/
│       ├── test_input/
│       ├── test_label/
│       └── test_misc/
├── examples/                  # Exemples executables par module
├── docs/                      # Documentation manuelle
├── .github/
│   ├── instructions/          # Standards et conventions (ce dossier)
│   └── workflows/             # CI/CD GitHub Actions
├── .hooks/                    # Hooks Git personnalises
├── .scripts/
│   ├── build/                 # build_package.py, upload_to_pypi.py
│   └── dev/                   # lint.py, update_version.py
├── pyproject.toml             # Configuration centralisee
├── Makefile                   # Commandes de dev
├── CLAUDE.md                  # Instructions Claude
└── AGENTS.md                  # Instructions agents IA
```

### Principes architecturaux

1. **Organisation modulaire par categorie** : les widgets sont regroupes par famille
   fonctionnelle (`button/`, `input/`, `label/`, `misc/`), pas par pattern technique.

2. **Un fichier = un widget** : chaque widget vit dans son propre fichier.
   Exception : `DraggableItem` cohabite avec `DraggableList` car ils forment un couple
   indissociable.

3. **Re-exports via `__init__.py`** : chaque module expose ses classes publiques dans
   son `__init__.py`, et le `__init__.py` racine re-exporte tout. L'utilisateur final
   peut importer depuis le top-level :

   ```python
   from ezqt_widgets import ToggleSwitch, DateButton
   ```

4. **`__all__` systematique** : chaque `__init__.py` declare explicitement son API
   publique via `__all__`.

5. **Tests en miroir** : la structure de `tests/unit/` reproduit celle de
   `ezqt_widgets/`. Le test de `ezqt_widgets/misc/toggle_switch.py` se trouve dans
   `tests/unit/test_misc/test_toggle_switch.py`.

---

## Conventions de code

### Structure d'un fichier Python

Chaque fichier suit un layout strict avec des separateurs visuels :

```python
# ///////////////////////////////////////////////////////////////
# NOM_MODULE - Description courte
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Docstring du module.

Description etendue du module et de son contenu.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
import sys
from pathlib import Path

# Third-party imports
from PySide6.QtWidgets import QWidget

# Local imports
from .utils import helper

# ///////////////////////////////////////////////////////////////
# CONSTANTS
# ///////////////////////////////////////////////////////////////

DEFAULT_VALUE = 42

# ///////////////////////////////////////////////////////////////
# CLASSES
# ///////////////////////////////////////////////////////////////

class MyWidget(QWidget):
    """..."""

# ///////////////////////////////////////////////////////////////
# PUBLIC API
# ///////////////////////////////////////////////////////////////

__all__ = ["MyWidget"]
```

Points critiques :

- `from __future__ import annotations` est **toujours** le premier import.
- Les imports sont groupes : standard, third-party, local, separes par une ligne vide.
- Les separateurs `# ///...` sont en **majuscules** pour les sections principales.
- Les separateurs `# ----...` sont pour les sous-sections au sein d'une classe.

### Structure d'un widget

Chaque widget suit ce pattern :

```python
class WidgetName(QWidget):
    """Docstring Google-style avec Features, Args, Signals."""

    # Signaux Qt
    valueChanged = Signal(int)

    # ///////////////////////////////////////////////////////////////
    # INIT
    # ///////////////////////////////////////////////////////////////

    def __init__(self, parent=None, **kwargs) -> None:
        """Initialize the widget."""
        super().__init__(parent)
        self._private_attr = value
        self._setup_widget()
        self._setup_animation()  # si applicable

    # ------------------------------------------------
    # PRIVATE METHODS
    # ------------------------------------------------

    def _setup_widget(self) -> None: ...
    def _setup_animation(self) -> None: ...

    # ///////////////////////////////////////////////////////////////
    # PROPERTIES
    # ///////////////////////////////////////////////////////////////

    @property
    def attr(self) -> type:
        """Getter avec docstring."""
        return self._private_attr

    @attr.setter
    def attr(self, value: type) -> None:
        """Setter avec docstring."""
        ...

    # ///////////////////////////////////////////////////////////////
    # PUBLIC METHODS
    # ///////////////////////////////////////////////////////////////

    def toggle(self) -> None: ...

    # ///////////////////////////////////////////////////////////////
    # EVENT HANDLERS
    # ///////////////////////////////////////////////////////////////

    def mousePressEvent(self, event) -> None: ...
    def paintEvent(self, event) -> None: ...

    # ///////////////////////////////////////////////////////////////
    # OVERRIDE METHODS
    # ///////////////////////////////////////////////////////////////

    def sizeHint(self) -> QSize: ...

    # ///////////////////////////////////////////////////////////////
    # STYLE METHODS
    # ///////////////////////////////////////////////////////////////

    def refresh_style(self) -> None: ...
```

Ordre des sections dans une classe :
`INIT` > `PRIVATE METHODS` > `PROPERTIES` > `PUBLIC METHODS` > `EVENT HANDLERS` > `OVERRIDE METHODS` > `STYLE METHODS`

### Docstrings

- Format **Google-style** exclusivement.
- Sections supportees : `Args`, `Returns`, `Raises`, `Signals`, `Features`, `Example`.
- Les types sont dans la **signature**, pas dans la docstring.
- Les docstrings de classe incluent `Features`, `Args` et `Signals`.

```python
def clear_date(self) -> None:
    """Clear the current date and reset to placeholder.

    Emits dateChanged with an invalid QDate.

    Raises:
        RuntimeError: If the widget has been destroyed.
    """
```

### Nommage

| Element          | Convention         | Exemple                          |
| ---------------- | ------------------ | -------------------------------- |
| Module           | snake_case         | `toggle_switch.py`               |
| Classe           | PascalCase         | `ToggleSwitch`                   |
| Methode publique | snake_case         | `refresh_style()`                |
| Methode privee   | `_snake_case`      | `_setup_widget()`                |
| Attribut prive   | `_snake_case`      | `self._checked`                  |
| Signal Qt        | camelCase          | `toggled`, `dateChanged`         |
| Constante        | UPPER_SNAKE_CASE   | `DEFAULT_WIDTH`                  |
| Fichier de test  | `test_<module>.py` | `test_toggle_switch.py`          |
| Classe de test   | `Test<Widget>`     | `TestToggleSwitch`               |
| Methode de test  | `test_<behavior>`  | `test_toggle_switch_set_checked` |

### Type hints

- **Obligatoires** sur toute l'API publique (methodes, properties, signaux).
- Utiliser les types natifs Python 3.10+ : `list[str]`, `int | None`.
- `from __future__ import annotations` permet la syntaxe moderne partout.
- Les Qt Properties utilisent `Property(type, getter, setter)`.

---

## Patterns techniques recurrents

### Animations

Les widgets animes utilisent `QPropertyAnimation` avec une Qt Property :

```python
# Declaration de la Property
circle_position = Property(int, _get_pos, _set_pos)

# Setup de l'animation
self._anim = QPropertyAnimation(self, b"circle_position")
self._anim.setDuration(200)
self._anim.setEasingCurve(QEasingCurve.Type.InOutCubic)

# Lancement
self._anim.setStartValue(start)
self._anim.setEndValue(end)
self._anim.start()
```

### Custom painting

Les widgets avec rendu personnalise surclassent `paintEvent` :

```python
def paintEvent(self, _event: QPaintEvent) -> None:
    painter = QPainter(self)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    # ... dessin
    # Pas besoin d'appeler painter.end() (geree par le scope)
```

### Signaux Qt

- Declarer les signaux comme **attributs de classe**.
- Emettre uniquement quand la valeur change reellement.
- Nommer en camelCase, au passe ou participe present : `toggled`, `dateChanged`,
  `valueChanged`.

```python
class MyWidget(QWidget):
    valueChanged = Signal(int)

    def set_value(self, value: int) -> None:
        if self._value != value:
            self._value = value
            self.valueChanged.emit(value)
```

---

## Tests

### Principes

- Framework : **pytest** avec fixtures Qt partagees dans `conftest.py`.
- Couverture minimum : **60%** (seuil `--cov-fail-under`), objectif : **80%+**.
- Chaque widget a sa propre classe de test `Test<Widget>`.
- Marquer les tests : `@pytest.mark.unit`, `@pytest.mark.slow`,
  `@pytest.mark.integration`.

### Fixtures disponibles

| Fixture             | Scope      | Usage                                         |
| ------------------- | ---------- | --------------------------------------------- |
| `qt_application`    | `session`  | Instance QApplication partagee                |
| `qt_widget_cleanup` | `function` | Nettoyage des evenements Qt apres chaque test |
| `wait_for_signal`   | `function` | Attendre l'emission d'un signal avec timeout  |
| `mock_icon_path`    | `function` | Fichier PNG temporaire                        |
| `mock_svg_path`     | `function` | Fichier SVG temporaire                        |

### Convention de nommage des tests

```python
class TestToggleSwitch:
    def test_toggle_switch_creation_default(self, qt_application) -> None: ...
    def test_toggle_switch_creation_custom(self, qt_application) -> None: ...
    def test_toggle_switch_set_checked(self, qt_application) -> None: ...
```

Pattern : `test_<widget>_<comportement_teste>`

### Lancer les tests

```bash
make test           # Tests unitaires
make test-cov       # Tests avec rapport de couverture
make test-fast      # Tests rapides (sans @pytest.mark.slow)
```

---

## Outillage et qualite de code

### Chaine de formatage et linting

Les outils sont configures dans `pyproject.toml` et executes via le pre-commit hook
ou manuellement :

| Outil   | Role                     | Ligne de commande        |
| ------- | ------------------------ | ------------------------ |
| Black   | Formatage (88 chars)     | `black ezqt_widgets`     |
| isort   | Tri des imports          | `isort ezqt_widgets`     |
| Ruff    | Linting (format + check) | `ruff check --fix .`     |
| Bandit  | Securite                 | `bandit -r ezqt_widgets` |
| Pyright | Type checking            | `pyright ezqt_widgets`   |

Script tout-en-un : `python .scripts/dev/lint.py`

### Pre-commit hook

Le hook `.hooks/pre-commit` :

1. Execute `.scripts/dev/lint.py` (formatage + linting).
2. Met a jour le badge de version dans le README via `.scripts/dev/update_version.py`.
3. Stage automatiquement les fichiers reformates.

### Regles Ruff actives

```text
E (pycodestyle errors), W (warnings), F (pyflakes), I (isort),
B (bugbear), C4 (comprehensions), UP (pyupgrade), S (bandit),
T20 (print), ARG (unused args), PIE (pie), SIM (simplify)
```

Regles ignorees avec justification :

- `E501` : longueur de ligne geree par Black
- `T201` : `print()` autorise dans CLI et scripts
- `S101` : `assert` autorise dans les tests

---

## Ajouter un nouveau widget

Checklist pour integrer un widget dans la continuite du projet :

### 1. Creer le fichier du widget

Placer le fichier dans le module approprie (`button/`, `input/`, `label/`, `misc/`).
Suivre la structure de fichier et de classe documentee ci-dessus.

```text
ezqt_widgets/<module>/mon_widget.py
```

### 2. Exporter dans le `__init__.py` du module

```python
# Dans ezqt_widgets/<module>/__init__.py
from .mon_widget import MonWidget

__all__ = [
    ...,
    "MonWidget",
]
```

### 3. Re-exporter dans le `__init__.py` racine

```python
# Dans ezqt_widgets/__init__.py
from .<module> import MonWidget

__all__ = [
    ...,
    "MonWidget",
]
```

### 4. Ecrire les tests

Creer `tests/unit/test_<module>/test_mon_widget.py` avec :

- Test de creation par defaut
- Test de creation avec parametres personnalises
- Test des properties (getters/setters)
- Test des signaux (emission, valeurs)
- Test des interactions (mouse events)
- Test du `sizeHint`

### 5. Creer un exemple

Ajouter une section dans `examples/<module>_example.py` ou creer un nouvel exemple
si le module est nouveau.

### 6. Verifier

```bash
make check    # format + lint + test
```

---

## Publication

### Versioning

- Version semantique (MAJOR.MINOR.PATCH).
- La version est definie a **deux endroits** qui doivent etre synchronises :
  - `ezqt_widgets/__init__.py` : `__version__ = "X.Y.Z"`
  - `pyproject.toml` : `version = "X.Y.Z"`
- Le script `.scripts/dev/update_version.py` synchronise les deux.

### Processus de publication

1. Mettre a jour la version dans `ezqt_widgets/__init__.py`.
2. Executer `python .scripts/dev/update_version.py`.
3. Commit et merge sur `main`.
4. Creer un tag : `git tag vX.Y.Z && git push origin vX.Y.Z`.
5. Le workflow GitHub Actions `publish-pypi.yml` :
   - Verifie la coherence version tag / pyproject.toml.
   - Verifie que le tag est sur `main`.
   - Execute les tests.
   - Build le package (wheel + sdist).
   - Valide avec twine.
   - Publie sur PyPI.

### Contraintes d'environnement

- **Proxy** : configuration requise pour les requetes externes.
- **Wheel files** : privilegier les `.whl` pour les dependances.
- **Acces PyPI limite** : gestion locale des packages en contexte corporatif.
- **Windows** : environnement de developpement principal.

---

## Commandes Make

```bash
# Installation
make install          # pip install -e .
make install-dev      # pip install -e ".[dev]"

# Qualite
make format           # Black + isort
make lint             # .scripts/dev/lint.py
make fix              # Alias de format

# Tests
make test             # Tests unitaires
make test-cov         # Tests + couverture
make test-fast        # Tests sans @slow

# Hooks
make setup-hooks      # Installer pre-commit
make pre-commit       # Lancer pre-commit manuellement

# Nettoyage
make clean            # Supprimer __pycache__, .egg-info, build/, dist/

# Raccourcis
make check            # format + lint + test
make prepare          # format + lint + test-fast
```

---

## Pratiques interdites

- `print()` pour le logging : utiliser le module `logging`.
- Variables globales mutables.
- Code commente dans les commits.
- Credentials ou chemins absolus en dur dans le code.
- `os.path` : utiliser `pathlib.Path`.
- `Union[X, Y]` : utiliser `X | Y` (Python 3.10+).
- Imports depuis `typing` quand un equivalent natif existe (`list`, `dict`, `tuple`).

---

## Fichiers de reference

| Fichier                              | Contenu                                      |
| ------------------------------------ | -------------------------------------------- |
| `pyproject.toml`                     | Configuration centralisee de tous les outils |
| `Makefile`                           | Commandes de dev                             |
| `.hooks/pre-commit`                  | Hook de formatage automatique                |
| `.scripts/dev/lint.py`               | Script de linting                            |
| `.scripts/dev/update_version.py`     | Synchronisation de version                   |
| `.scripts/build/build_package.py`    | Build du package                             |
| `.scripts/build/upload_to_pypi.py`   | Upload vers PyPI                             |
| `.github/workflows/publish-pypi.yml` | CI/CD publication                            |
| `tests/conftest.py`                  | Fixtures pytest partagees                    |
