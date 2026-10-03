"""Punto de entrada: ejecuta este archivo desde PyCharm (Run 'main')."""

import os

import certifi

# PyCharm abierto desde el Dock no hereda el PATH de la Terminal:
# añadimos las rutas de Homebrew para que se encuentre ffmpeg.
for ruta in ("/opt/homebrew/bin", "/usr/local/bin"):
    if os.path.isdir(ruta) and ruta not in os.environ.get("PATH", ""):
        os.environ["PATH"] = ruta + os.pathsep + os.environ.get("PATH", "")

# Certificados para HTTPS (evita SSL: CERTIFICATE_VERIFY_FAILED en macOS)
os.environ.setdefault("SSL_CERT_FILE", certifi.where())
os.environ.setdefault("REQUESTS_CA_BUNDLE", certifi.where())

from transcriptor.app import Transcriptor  # noqa: E402

if __name__ == "__main__":
    Transcriptor().mainloop()