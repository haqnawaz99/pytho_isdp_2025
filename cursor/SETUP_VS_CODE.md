# Setup: Python + Visual Studio Code (School Lab)

For mixed madrasa/school classes using **laptops**.

## 1. Install Python

1. Download Python 3.10 or newer from https://www.python.org/downloads/
2. Run installer — **check** “Add python.exe to PATH”.
3. Test in terminal (PowerShell or CMD):

```bash
python --version
```

Expected: `Python 3.10.x` or higher.

## 2. Install Visual Studio Code

1. Download from https://code.visualstudio.com/
2. Install with default options.

## 3. VS Code extensions (one-time per laptop)

Open VS Code → **Extensions** (Ctrl+Shift+X) → install:

- **Python** (Microsoft) — run and debug Python
- **Pylance** (Microsoft) — usually installed with Python extension

## 4. Open the course folder

1. **File → Open Folder**
2. Select: `...\Python\code\cursor`
3. Students see all modules in the left sidebar.

## 5. Run a Python file

1. Open any `.py` file (e.g. `0_Getting_Started/0_3_first_print.py`).
2. Click **Run Python File** (triangle icon top-right), or press **F5** (first time: choose “Python File”).
3. Output appears in the **Terminal** panel at the bottom.

## 6. Save files before running

- **Ctrl+S** saves the file. Always save before Run.
- File name must end with `.py`.

## 7. Common lab problems

| Problem | Fix |
|---------|-----|
| `python` not recognized | Reinstall Python with “Add to PATH” checked |
| No Run button | Install Python extension; reload VS Code |
| Wrong folder open | Open `cursor` folder, not parent `code` only |
| Urdu/Arabic in print looks wrong | Terminal font issue; code is still correct. Use UTF-8; avoid fancy fonts in terminal |

## 8. Optional: Urdu keyboard

Students type **code in English**. Urdu in strings is optional. For Urdu in `print()`, Windows Urdu keyboard (Windows+Space) works in VS Code.

## 9. Offline teaching

No internet needed after Python and VS Code are installed. Keep installer `.exe` files on a USB for new laptops.
