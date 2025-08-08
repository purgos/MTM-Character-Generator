# AppImage Packaging

This directory contains a simple AppImage packaging setup for the MTM Character Generator.

## Requirements
- Linux x86_64
- python3 and pip
- tkinter available on system (Debian/Ubuntu: `sudo apt install python3-tk`)

## Build

```bash
bash packaging/appimage/build_appimage.sh
```

The script will:
1. Install Python dependencies (including PyInstaller)
2. Build a single-file binary with PyInstaller
3. Create an AppDir and bundle the binary, desktop file, and icon
4. Download `appimagetool` (if missing)
5. Produce `dist/MTM-Character-Generator-<version>-x86_64.AppImage`

## Notes
- The app does not need network access at runtime.
- The AppImage includes the PyInstaller-built executable and data files.
- If your distribution needs `libtk`/`libtcl`, ensure they are present.
