# 🐧 joonapdf

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![Linux](https://img.shields.io/badge/platform-linux-orange?style=flat-square)
![Status](https://img.shields.io/badge/status-beta-yellow?style=flat-square)

---

## 🚀 Descripción

**`joonapdf`** es una **herramienta CLI en Python** para convertir archivos **`.docx`** a **PDF** usando **LibreOffice** en modo *headless* (sin interfaz gráfica).

Con solo un comando puedes transformar uno o varios documentos Word en PDFs profesionales y ordenados, con instalación automática y silenciosa de LibreOffice, todo mientras ves un spinner de progreso y mensajes coloridos con íconos para una experiencia súper amigable.

---

## ✨ Características principales

- 📝 Conversión masiva de archivos `.docx` a PDF en una sola ejecución.
- ⚙️ Instalación y desinstalación automática de LibreOffice sin molestar.
- 📁 Los PDFs generados se guardan automáticamente en una carpeta **`joonapdf`** dentro del escritorio del usuario.
- 🎨 Mensajes con colores e íconos para una experiencia visual agradable y clara.
- 🐧 Diseñado para funcionar en **Linux** (Ubuntu y derivados, probado).

---

## 🔧 Requisitos

- Python 3.8 o superior 🐍
- LibreOffice (si no está instalado, el script lo instala por ti) 🧙‍♂️
- Sistema operativo Linux (Ubuntu y derivados recomendados) 🐧

---

## ⚡ Instalación rápida

```bash
git clone https://github.com/tuusuario/joonapdf.git
cd joonapdf
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # si agregas paquetes externos
pip install .
