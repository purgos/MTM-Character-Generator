# MTM Character Generator

## Installation

### Windows
1. Download and install Python 3.12 or newer from [python.org](https://www.python.org/downloads/windows/).
2. Open Command Prompt and navigate to the project directory:
   ```sh
   cd path\to\MTM-Character-Generator
   ```
3. (Optional) Create a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
4. Install required packages:
   ```sh
   pip install -r requirements.txt
   ```
5. Run the application:
   ```sh
   python src/character_sheet_modular.py
   ```

### Linux

1. Install Python 3.12 or newer using your package manager (e.g., `sudo apt install python3.12`).
2. Open a terminal and navigate to the project directory:
   ```sh
   cd /path/to/MTM-Character-Generator
   ```
3. (Optional) Create a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install required packages:
   ```sh
   pip install -r requirements.txt
   ```
5. Run the application:
   ```sh
   python3 src/character_sheet_modular.py
   ```

### macOS
1. Install Python 3.12 or newer from [python.org](https://www.python.org/downloads/mac-osx/) or using Homebrew:
   ```sh
   brew install python@3.12
   ```
2. Open Terminal and navigate to the project directory:
   ```sh
   cd /path/to/MTM-Character-Generator
   ```
3. (Optional) Create a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install required packages:
   ```sh
   pip install -r requirements.txt
   ```
5. Run the application:
   ```sh
   python3 src/character_sheet_modular.py
   ```

## Troubleshooting

- **Python not found:** Ensure Python 3.12+ is installed and added to your PATH.
- **Permission denied:** Try running the command with elevated privileges (e.g., `sudo` on Linux/macOS).
- **Missing dependencies:** Run `pip install -r requirements.txt` to install all required packages.
- **Virtual environment issues:** Delete and recreate the `venv` folder if activation fails.
- **Module not found errors:** Double-check you are running the correct Python version and that your virtual environment is activated.
- **Application crashes:** Check for error messages in the terminal and ensure all dependencies are installed.

For further help, consult the official Python documentation or open an issue in this repository.
