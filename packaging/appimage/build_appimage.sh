#!/usr/bin/env bash
set -euo pipefail

# Build an AppImage for MTM Character Generator
# Requirements:
#  - Linux x86_64
#  - Internet access to download appimagetool (first run)
#  - python3 with pip, and system tkinter (python3-tk)

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SRC_DIR="$ROOT_DIR/src"
PKG_DIR="$ROOT_DIR/packaging/appimage"
BUILD_DIR="$PKG_DIR/build"
DIST_DIR="$ROOT_DIR/dist"
APPDIR="$BUILD_DIR/AppDir"
APP_NAME="MTM-Character-Generator"
BIN_NAME="mtm-character-generator"
VERSION="0.1.0"

mkdir -p "$BUILD_DIR" "$DIST_DIR"

echo "[1/6] Creating Python virtual environment and installing deps…"
VENV_DIR="$BUILD_DIR/venv"
python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"
pip install --upgrade pip >/dev/null
pip install -r "$ROOT_DIR/requirements.txt" pyinstaller >/dev/null

echo "[2/6] Building executable with PyInstaller…"
pyinstaller \
  --noconfirm \
  --noconsole \
  --name "$BIN_NAME" \
  --onefile \
  --add-data "$SRC_DIR:src" \
  "$SRC_DIR/character_sheet_modular.py"

EXE_PATH="$ROOT_DIR/dist/$BIN_NAME"
if [[ ! -f "$EXE_PATH" ]]; then
  # Newer PyInstaller places binary at dist/<name>/<name>
  if [[ -f "$ROOT_DIR/dist/$BIN_NAME/$BIN_NAME" ]]; then
    EXE_PATH="$ROOT_DIR/dist/$BIN_NAME/$BIN_NAME"
  else
    echo "PyInstaller output not found. Build failed." >&2
    exit 1
  fi
fi

echo "[3/6] Preparing AppDir layout…"
rm -rf "$APPDIR"
mkdir -p "$APPDIR/usr/bin" "$APPDIR/usr/share/applications" "$APPDIR/usr/share/icons/hicolor/256x256/apps"

install -m 755 "$EXE_PATH" "$APPDIR/usr/bin/$BIN_NAME"
install -m 755 "$PKG_DIR/AppRun" "$APPDIR/AppRun"
install -m 644 "$PKG_DIR/$APP_NAME.desktop" "$APPDIR/$APP_NAME.desktop"
install -m 644 "$PKG_DIR/$APP_NAME.png" "$APPDIR/usr/share/icons/hicolor/256x256/apps/$APP_NAME.png"
# Also place a top-level icon to satisfy appimagetool's desktop Icon check
install -m 644 "$PKG_DIR/$APP_NAME.png" "$APPDIR/$APP_NAME.png"

echo "[4/6] Fetching appimagetool if needed…"
APPIMAGETOOL="$BUILD_DIR/appimagetool-x86_64.AppImage"
if [[ ! -x "$APPIMAGETOOL" ]]; then
  curl -L -o "$APPIMAGETOOL" "https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage"
  chmod +x "$APPIMAGETOOL"
fi

echo "[5/6] Building AppImage…"
OUTPUT_APPIMAGE="$DIST_DIR/${APP_NAME}-${VERSION}-x86_64.AppImage"
APPIMAGE_EXTRACT_AND_RUN=1 "$APPIMAGETOOL" "$APPDIR" "$OUTPUT_APPIMAGE"

echo "[6/6] Done"
echo "AppImage created at: $OUTPUT_APPIMAGE"

deactivate || true
