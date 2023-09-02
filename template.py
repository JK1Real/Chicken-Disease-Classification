import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')

projectname='cnnClassifier'

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{projectname}/__init__.py",
    f"src/{projectname}/components/__init__.py",
    f"src/{projectname}/utils/__init__.py",
    f"src/{projectname}/config/__init__.py",
    f"src/{projectname}/config/configuration.py",
    f"src/{projectname}/pipeline/__init__.py",
    f"src/{projectname}/entity/__init__.py",
    f"src/{projectname}/constants/__init__.py",
    "conig/config.yaml",
    "dvc.yaml",
    "params.yml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"
 
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating the file directory: {filedir} for the file name: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0) :
        with open(filepath,'w'):
            pass
            logging.info(f"Creating empty file:{filepath}")
    else:
        logging.info(f"{filename} already exists")