# joonapdf

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Descripción

`joonapdf` es una herramienta de línea de comandos en Python para convertir archivos `.docx` a PDF usando LibreOffice en modo headless. 

Permite instalar y desinstalar LibreOffice automáticamente con indicadores visuales, y guarda los PDFs generados en una carpeta llamada `joonapdf` en el escritorio del usuario.

## Características

- Conversión de múltiples archivos `.docx` a PDF en una sola ejecución.
- Instalación y desinstalación automática y silenciosa de LibreOffice con spinner de progreso.
- Guarda los PDFs generados en una carpeta dedicada en el escritorio.
- Mensajes de estado con colores e íconos para mejor experiencia de usuario.

## Requisitos

- Python 3.8 o superior
- LibreOffice (la herramienta puede instalarlo automáticamente si no está presente)
- Sistema operativo Linux (probado en Ubuntu y derivados)

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/tuusuario/joonapdf.git
cd joonapdf

