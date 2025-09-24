#!/usr/bin/env python3
"""
Auto Documentation Updater
Detecta archivos .md y .ipynb nuevos y actualiza la documentación automáticamente
"""

import os
import re
import yaml
import subprocess
from pathlib import Path
from datetime import datetime
import argparse

class DocumentationUpdater:
    def __init__(self, repo_path="."):
        self.repo_path = Path(repo_path)
        self.docs_path = self.repo_path / "docs"
        self.mkdocs_config = self.repo_path / "mkdocs.yml"

    def find_new_files(self):
        """Encuentra archivos nuevos no trackeados por git"""
        try:
            # Archivos no trackeados
            result = subprocess.run(
                ['git', 'ls-files', '--others', '--exclude-standard'],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                print("❌ Error ejecutando git ls-files")
                return []

            untracked_files = result.stdout.strip().split('\n')

            # Filtrar solo archivos .md y .ipynb en docs/
            new_docs = [
                f for f in untracked_files
                if f.startswith('docs/') and f.endswith(('.md', '.ipynb'))
            ]

            return new_docs

        except Exception as e:
            print(f"❌ Error buscando archivos nuevos: {e}")
            return []

    def categorize_file(self, filepath):
        """No categoriza automáticamente - el usuario coloca archivos manualmente"""
        # Simplemente retorna None para indicar que no se debe categorizar automáticamente
        return None

    def generate_title(self, filepath):
        """Genera título legible del nombre de archivo"""
        filename = os.path.basename(filepath)
        name = filename.replace('.md', '').replace('.ipynb', '')

        # Limpiar y formatear
        name = re.sub(r'[-_]', ' ', name)
        name = re.sub(r'\d+[-_]', '', name)  # Remover prefijos numéricos
        name = name.strip().title()

        return name

    def update_mkdocs_nav(self, new_files):
        """Solo reporta archivos nuevos sin modificar navegación"""
        if not new_files:
            return False

        print(f"Se detectaron {len(new_files)} archivos nuevos:")
        for filepath in new_files:
            rel_path = str(Path(filepath).relative_to('docs'))
            title = self.generate_title(filepath)
            print(f"  - {title}: {rel_path}")

        print("\nArchivos listos para ser agregados manualmente a mkdocs.yml")
        return False  # No hace cambios automáticos

    def commit_changes(self, new_files):
        """Crea commit con los cambios"""
        try:
            # Configurar git (si es necesario)
            subprocess.run(['git', 'add', 'docs/', 'mkdocs.yml'],
                         cwd=self.repo_path, check=True)

            # Crear mensaje descriptivo
            current_date = datetime.now().strftime('%Y-%m-%d')
            file_list = '\n'.join(f"  • {f}" for f in new_files)

            commit_message = f"""Nuevos documentos agregados ({current_date})

• {len(new_files)} archivos nuevos detectados
• Navegación actualizada

Archivos agregados:
{file_list}"""

            # Commit
            subprocess.run(['git', 'commit', '-m', commit_message],
                         cwd=self.repo_path, check=True)

            print("Commit creado exitosamente")
            return True

        except subprocess.CalledProcessError as e:
            print(f"Error creando commit: {e}")
            return False

    def commit_new_files_only(self, new_files):
        """Crea commit solo con archivos nuevos, sin modificar mkdocs.yml"""
        try:
            # Agregar solo archivos nuevos
            subprocess.run(['git', 'add'] + new_files,
                         cwd=self.repo_path, check=True)

            # Crear mensaje descriptivo
            current_date = datetime.now().strftime('%Y-%m-%d')
            file_list = '\n'.join(f"  • {f}" for f in new_files)

            commit_message = f"""Nuevos documentos agregados ({current_date})

• {len(new_files)} archivos nuevos detectados
• Listos para agregar manualmente a navegación

Archivos agregados:
{file_list}"""

            # Commit
            subprocess.run(['git', 'commit', '-m', commit_message],
                         cwd=self.repo_path, check=True)

            print("Commit creado exitosamente")
            return True

        except subprocess.CalledProcessError as e:
            print(f"Error creando commit: {e}")
            return False

    def push_changes(self):
        """Push cambios al repositorio remoto"""
        try:
            subprocess.run(['git', 'push'], cwd=self.repo_path, check=True)
            print("🚀 Cambios enviados al repositorio remoto")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Error enviando cambios: {e}")
            return False

    def run(self, auto_push=True):
        """Ejecuta el proceso completo de actualización"""
        print("Iniciando escaneo de documentacion...")

        new_files = self.find_new_files()

        if not new_files:
            print("No se encontraron archivos nuevos")
            return

        print(f"Encontrados {len(new_files)} archivos nuevos:")
        for f in new_files:
            print(f"  - {f}")

        # Solo reportar archivos, no modificar navegación automáticamente
        self.update_mkdocs_nav(new_files)

        # Crear commit solo con los archivos nuevos, sin modificar mkdocs.yml
        if self.commit_new_files_only(new_files):
            if auto_push:
                self.push_changes()


def main():
    parser = argparse.ArgumentParser(description='Auto-actualizar documentación')
    parser.add_argument('--no-push', action='store_true',
                       help='No hacer push automático')
    parser.add_argument('--repo-path', default='.',
                       help='Ruta del repositorio')

    args = parser.parse_args()

    updater = DocumentationUpdater(args.repo_path)
    updater.run(auto_push=not args.no_push)


if __name__ == '__main__':
    main()