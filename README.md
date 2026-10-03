# Transcriptor Whisper

Aplicación de escritorio (Tkinter) que transcribe a texto el audio de un vídeo de
YouTube o de un archivo local, usando el modelo Whisper en tu propio equipo.

## Estructura

```
transcriptor-whisper/
├── main.py                  # Punto de entrada
├── requirements.txt         # openai-whisper, yt-dlp
├── setup_mac.sh             # Instalación automática en macOS
├── transcriptor/
│   ├── __init__.py
│   ├── app.py               # Interfaz gráfica
│   ├── config.py            # Modelos, idiomas, carpeta de salida
│   ├── descarga.py          # Descarga del audio con yt-dlp
│   └── transcripcion.py     # Whisper y guardado del .txt
└── .idea/runConfigurations/Transcriptor.xml   # Configuración de ejecución de PyCharm
```

## Instalación (macOS)

1. Descomprime el zip donde quieras.
2. Abre Terminal en esa carpeta y ejecuta: `bash setup_mac.sh`
   (instala ffmpeg, Python y Tkinter con Homebrew y crea el entorno `.venv`).
3. En PyCharm: *File → Open…* y elige la carpeta `transcriptor-whisper`.
4. Si PyCharm no detecta el intérprete: *Settings → Project → Python Interpreter →
   Add Interpreter → Existing* y elige `.venv/bin/python`.
5. Arriba a la derecha selecciona la configuración **Transcriptor** y pulsa ▶.

## Uso

- Pega la URL del vídeo de YouTube **o** elige un archivo de audio/vídeo.
- Elige el modelo (`small` es buen equilibrio; `medium` más preciso pero más lento).
- Pulsa **Transcribir**. El texto aparece en la ventana y se guarda en
  `~/Downloads/Transcripciones/<título>.txt`.

La primera vez que uses cada modelo se descarga (small ≈ 460 MB, medium ≈ 1,5 GB).

## Problemas frecuentes

| Error | Solución |
|---|---|
| `No module named '_tkinter'` | El intérprete no es el de Homebrew. Repite `setup_mac.sh` y usa `.venv`. |
| `ffmpeg not found` | `brew install ffmpeg` y reinicia PyCharm. |
| `Sign in to confirm…` / `Unable to extract` | YouTube ha cambiado algo: `pip install -U yt-dlp` en la Terminal de PyCharm. |

## Aviso

Las condiciones de uso de YouTube no permiten descargar contenido con herramientas
externas. Úsalo con tus propios vídeos o para consulta personal.
