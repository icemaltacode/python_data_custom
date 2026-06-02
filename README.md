# PPF — Python Practice Exercises

Practice exercises for the course, organised by module (`Module 4/`, etc.).

## Prerequisites

- **Python 3.11 or newer** — download from <https://www.python.org/downloads/>.
  On Windows, tick **"Add Python to PATH"** during install.
- **[Visual Studio Code](https://code.visualstudio.com/)**.

## Getting started

```bash
git clone https://github.com/icemaltacode/python_data_custom.git
cd python_data_custom
code .
```

When VSCode opens the folder, it will offer to install the **recommended Python
extensions** — click **Install**.

After that, set up your environment using whichever path below works for you.
They all produce the same result: a local `.venv` with the required packages,
selected automatically as your interpreter.

### Path 1 — Automatic (recommended)

VSCode runs the setup for you on open. The first time, a prompt appears asking
to **"Allow Automatic Tasks"** — click **Allow** (or run *Tasks: Manage Automatic
Tasks* → *Allow Automatic Tasks*), then reload the window. The `.venv` is created
and packages installed in the background.

### Path 2 — VSCode "Create Environment"

If you skipped the automatic task:

1. Open the Command Palette — `Ctrl+Shift+P` (Windows) / `Cmd+Shift+P` (Mac).
2. Run **Python: Create Environment**.
3. Choose **Venv**, then your Python 3.11+ install.
4. Tick **`requirements.txt`** when asked which dependencies to install.

VSCode creates `.venv` and selects it automatically.

### Path 3 — Terminal (manual fallback)

From the project folder:

- **macOS:** `./setup.sh`
- **Windows (PowerShell):** `.\setup.ps1`

Then pick the interpreter manually if needed: Command Palette →
**Python: Select Interpreter** → choose the one under `.venv`.

## Verify it works

Open a new terminal in VSCode (it should auto-activate `.venv`) and run:

```bash
python -c "import pandas, numpy; print('OK', pandas.__version__)"
```

## Notes

- The `.venv` folder is **not** part of the repository — each machine builds its
  own. Don't commit it (it's already in `.gitignore`).
- Dependencies live in `requirements.txt`. If it changes, re-run any setup path
  above to update your environment.
