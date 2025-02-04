import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "data_science_project"

file_list = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constant/__init__.py",
    "config.yml",
    "params.yml",
    "schema.yml",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
    "app.py"
]


for file_path in file_list:
    filepath = Path(file_path)
    filedir, filename = os.path.split(filepath)
    
    if filedir:
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating filepath: {filepath}")
    else:
        logging.info(f"{filename} is already exist")
        

logging.info(f"Project structure created!")