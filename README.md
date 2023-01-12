# Oc-P3 : Générer des fichiers pdf à partir de python
---
![assets](img/logo_dev4u.png) | ![assets/img](img/logo_learnhome.png)

## Objectif
Ce programme est un utilitaire pour générer les fichiers pdf demandés dans le cadre de la formation 
proposée par [OpenClassRooms](https://openclassrooms.com/fr/) : Développeur d'applications Python
Il s'agit d'effectuer l'analyse et le design d'une application qui permettra de mettre en relation 
des enfants en difficulté scolaire avec des tuteurs bénévoles.

## Fonctionnement
Les fichiers sont générés dans un répertoire nommé output par défaut

## Installation
```bash
# Creer l'environnement virtuel
python -m venv env
source env/bin/activate

# cloner le projet
git clone https://github.com/Slb59/Oc-P3.git
cd Oc-P3

# installer les dépendances
pip install -r requirements.txt

# executer le programme
python ocp3.py
```
---

## Utilisation
Vous pouvez lancer le programme sans paramètre. Par défaut les fichiers sont générés dans un répertoire "output"
```shell
python ocp3.py
```
Il est aussi possible de précisez le répertoire de destination
Il est possible de préciser les répertoires de destination
```shell
python scrape.py --output mon_rep
```

