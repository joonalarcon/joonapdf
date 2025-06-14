#!/usr/bin/env python3

import sys
import os
import subprocess
import shutil
import threading
import itertools
import time

def print_success(msg):
    print(f"\033[1;32m✅ {msg}\033[0m")  # Verde negrita con check

def print_error(msg):
    print(f"\033[1;31m❌ {msg}\033[0m")  # Rojo negrita con cruz

def print_info(msg):
    print(f"\033[1;34mℹ️ {msg}\033[0m")  # Azul negrita con info

def print_spinner(msg):
    print(f"\033[1;33m🔄 {msg}\033[0m")  # Amarillo negrita con flecha giratoria

def print_question(msg):
    print(f"\033[1;36m❓ {msg}\033[0m")  # Cyan negrita con signo de pregunta

def show_spinner(task_func, message):
    spinner = itertools.cycle(['-', '\\', '|', '/'])
    done = {"status": False}

    def wrapper():
        try:
            task_func()
            done["status"] = True
        except subprocess.CalledProcessError:
            done["status"] = False

    thread = threading.Thread(target=wrapper)
    print_spinner(message)
    thread.start()
    while thread.is_alive():
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
    thread.join()
    return done["status"]

def is_libreoffice_installed():
    return shutil.which("libreoffice") is not None

def install_libreoffice():
    def task():
        subprocess.run(["sudo", "apt", "update", "-qq"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["sudo", "apt", "install", "-y", "libreoffice"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    success = show_spinner(task, "Instalando LibreOffice...")
    if success:
        print_success("\nLibreOffice se instaló correctamente.")
    else:
        print_error("\nError al instalar LibreOffice. Intenta instalarlo manualmente.")
    return success

def uninstall_libreoffice():
    def task():
        subprocess.run(["sudo", "apt", "remove", "--purge", "-y", "libreoffice*"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    success = show_spinner(task, "Desinstalando LibreOffice...")
    if success:
        print_success("\nLibreOffice se desinstaló correctamente.")
    else:
        print_error("\nHubo un error al desinstalar LibreOffice.")

def get_desktop_dir():
    try:
        return subprocess.check_output(["xdg-user-dir", "DESKTOP"]).decode().strip()
    except Exception:
        return os.path.expanduser("~/Desktop")

def convert_with_libreoffice(file_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    try:
        subprocess.run([
            "libreoffice",
            "--headless",
            "--convert-to", "pdf",
            file_path,
            "--outdir", output_dir
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        pdf_name = os.path.basename(file_path).replace('.docx', '.pdf')
        full_pdf_path = os.path.join(output_dir, pdf_name)
        print_success(f"PDF generado: {pdf_name}")
        print_info(f"El archivo PDF fue creado en:\n  {full_pdf_path}")
    except subprocess.CalledProcessError as e:
        print_error(f"Error al convertir con LibreOffice: {e}")
        sys.exit(1)

def offer_uninstall_libreoffice():
    print_question("¿Desea desinstalar LibreOffice ahora? (s/n): ")
    answer = input().strip().lower()
    if answer in ("s", "y"):
        uninstall_libreoffice()
    else:
        print_info("Dejar LibreOffice instalado permitirá generar futuros documentos PDF mucho más rápido.")

def main():
    if not is_libreoffice_installed():
        print_error("LibreOffice no está instalado. Es una herramienta crucial para generar PDF.")
        print_question("¿Desea instalar LibreOffice ahora? (s/n): ")
        answer = input().strip().lower()
        if answer in ("s", "y"):
            if not install_libreoffice():
                sys.exit(1)
        else:
            print_error("LibreOffice es necesario para continuar. Abortando.")
            sys.exit(1)

    if len(sys.argv) < 2:
        print_error("Uso: python3 word2pdf.py archivo.docx [otro.docx...]")
        sys.exit(1)

    desktop_dir = get_desktop_dir()
    output_dir = os.path.join(desktop_dir, "joonapdf")

    for file in sys.argv[1:]:
        if not file.endswith(".docx"):
            print_error(f"Formato incorrecto (no .docx): {file}")
            continue
        if not os.path.exists(file):
            print_error(f"Archivo no encontrado: {file}")
            continue
        convert_with_libreoffice(file, output_dir)

    offer_uninstall_libreoffice()

if __name__ == "__main__":
    main()
