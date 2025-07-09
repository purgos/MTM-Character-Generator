# MTM Character Sheet

A Python-based character sheet application for the MTM (Magic: The Gathering) tabletop roleplaying game.

## Features

- Character creation and management
- Aspect system with die assignments
- Gear die slot management
- Inventory tracking
- Special abilities management
- PDF export functionality
- Dice rolling with modifiers

## Quick Start

### Linux Users
```bash
# Run the existing Linux executable
./dist/MTM_Character_Sheet

# Or use the convenience script
./run_character_sheet.sh
```

### Windows Users
1. Copy this entire folder to a Windows machine
2. Run `build_windows.bat` to create the Windows executable
3. Run `run_windows.bat` to launch the application

## Installation and Setup

### Option 1: Using Pre-built Executables (Recommended)

#### Linux:
The Linux executable is already built and ready to use:
```bash
./dist/MTM_Character_Sheet
```

#### Windows:
1. **Transfer the project folder to a Windows machine**
2. **Install Python 3.8+ from [python.org](https://python.org)**
   - Make sure to check "Add Python to PATH" during installation
3. **Run the build script:**
   ```cmd
   build_windows.bat
   ```
4. **Launch the application:**
   ```cmd
   run_windows.bat
   ```

### Option 2: Running from Source

#### Linux:
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python src/character_sheet.py
```

#### Windows:
```cmd
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python src\character_sheet.py
```

## Building Executables

### Linux Build
```bash
# Use the automated build script
./build_linux.sh

# Or build manually
source venv/bin/activate
pip install -r requirements.txt
venv/bin/python -m PyInstaller character_sheet_linux.spec
```

### Windows Build
```cmd
# Use the automated build script
build_windows.bat

# Or build manually
venv\Scripts\activate
pip install -r requirements.txt
python -m PyInstaller character_sheet_windows.spec
```

### Cross-Platform Build
```bash
# Build both versions (Linux on Linux, Windows on Windows)
./build_all.sh
```

## File Structure

```
mtm-character-sheet-python/
├── src/
│   └── character_sheet.py          # Main application source
├── dist/
│   └── MTM_Character_Sheet         # Linux executable (built)
├── build_linux.sh                  # Linux build script
├── build_windows.bat               # Windows build script
├── run_character_sheet.sh          # Linux launcher
├── run_windows.bat                 # Windows launcher
├── character_sheet_linux.spec      # Linux PyInstaller config
├── character_sheet_windows.spec    # Windows PyInstaller config
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## Usage

1. **Basic Information Tab:** Enter character name, player name, race, and other basic details
2. **Aspects Tab:** Assign die types to your character's aspects (melee, ranged, rogue, magic)
3. **Abilities Tab:** Select special abilities based on your d12 aspect
4. **Gear Die Tab:** Manage your gear die slots for spells and abilities
5. **Inventory Tab:** Track your character's equipment and items

## File Management

- **Save Character:** Use File → Save to save your character as a JSON file
- **Load Character:** Use File → Load to load a previously saved character
- **Print Character:** Use File → Print to export your character sheet as a PDF
- **Reset Character:** Use File → Reset to start with a fresh character

## Dependencies

- Python 3.8+
- tkinter (GUI framework)
- reportlab (PDF generation)
- pillow (Image processing for reportlab)
- pyinstaller (for building executables)

## Platform-Specific Notes

### Linux
- Built on Ubuntu/Debian systems
- Requires X11 or Wayland display server
- Executable size: ~24MB

### Windows
- Must be built on Windows (cross-compilation not supported)
- Requires Python 3.8+ with PATH configuration
- Executable size: ~25-30MB
- May trigger antivirus warnings (false positive)

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Ensure you're using the correct Python version
3. Verify all dependencies are installed
4. Try running from source before building executable 
