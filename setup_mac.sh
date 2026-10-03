#!/bin/bash
# Instala las dependencias del sistema y crea el entorno virtual del proyecto.
# Uso: abre Terminal en esta carpeta y ejecuta:  bash setup_mac.sh
set -e

if ! command -v brew >/dev/null 2>&1; then
  echo "Homebrew no está instalado. Instálalo desde https://brew.sh y vuelve a ejecutar."
  exit 1
fi

echo "==> Instalando ffmpeg, Python y Tkinter con Homebrew…"
brew install ffmpeg python python-tk

PY="$(brew --prefix)/bin/python3"
echo "==> Creando entorno virtual en .venv con $PY"
"$PY" -m venv .venv
source .venv/bin/activate

echo "==> Instalando dependencias de Python…"
pip install --upgrade pip
pip install -U -r requirements.txt

echo
echo "Listo. Abre esta carpeta en PyCharm y ejecuta la configuración 'Transcriptor'."
