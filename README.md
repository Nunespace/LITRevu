# Application web LITRevu
***
Cette application permet de demander ou publier des critiques de livres ou d’articles. 



## Fonctionnalités de l'application

L’application présente trois cas d’utilisation principaux :
- la publication des critiques de livres ou d’articles ;
- la demande des critiques sur un livre ou sur un article particulier ;
- la recherche d’articles et de livres intéressants à lire, en se basant sur les critiques des autres.


## Installation

## Prérequis

**Python** doit être préalablement installé.

Si vous travaillez dans un environnement Linux ou MacOS : Python est en principe déjà installé. Pour le vérifier, ouvrez votre terminal et tapez : `python --version` ou `python3 --version`

Si Python n'est pas installé, vous pouvez le télécharger à l'adresse suivante : 
[Télécharger Python3](https://www.python.org/downloads)

Vous aurez aussi besoin de l'installateur de paquets de Python **pip** qui est compris par défaut si vous disposez d'une version de Python >= 3.4. Vous pouvez vérifier qu'il est disponible via votre ligne de commande, en saisissant : `pip --version`

Vous aurez aussi besoin de **Git** pour cloner l'application sur votre ordinateur. Vérifier son installation en tapant   `git --version`
Sinon, choisissez et téléchargez la version de Git qui correspond à votre installation : MacOS, Windows ou Linux/Unix en cliquant sur le lien suivant : [télécharger git](https://git-scm.com/downloads)
 <sub>Puis exécutez le fichier que vous venez de télécharger. Appuyez sur _Suivant_ à chaque fenêtre puis sur _Installer_. Lors de l’installation, laissez toutes les options par défaut, elles conviennent bien. 
Git Bash est l’interface permettant d’utiliser Git en ligne de commande.


### 1° Installation de l'application web

1. Ouvrez le terminal et tapez :
```
$ git clone https://github.com/Nunespace/LITRevu.git
```
Vous pouvez également télécharger le code en temps qu'archive zip : [Projet_LITRevu](https://github.com/Nunespace/LITRevu/archive/refs/heads/main.zip)


2. Placez-vous dans le répertoire LITRevu :

```
$ CD LITRevu
ou
$ CD chemin .../LITRevu
```

3. Créez votre environnement virtuel : 

```
python3 -m venv env 
```

ou[^1]

```
python -m venv env 
```

4. Activer votre environnement virtuel

> sous mac ou Linux :
```
$ source env/bin/activate  
```
> sous Windows, la commande sera :
```
$ env\Scripts\activate.bat
```

5. Puis installez les paquets répertoriés dans le fichier requirements.txt :
```
$ pip install -r requirements.txt
```
[^1]: selon la version de Python installée sur votre PC.

### 2° Exécution de l'application web

1. Activer votre environnement virtuel (Voir Installation 4. ci-dessus)

2. Lancer le serveur en local[^2]
```
$ python manage.py runserver 
```

3. Ouvrez votre navigateur et taper l'url suivante : http://127.0.0.1:8000/

   ou cliquer sur ce lien : [Site_LITRevu](http://127.0.0.1:8000/)


[^2]: tapez Ctrl-C pour arrêter le serveur


## Administration du site 

1. Créer votre accès superutilisateur pour la gestion du site en tapant:
```
$ python manage.py createsuperuser
``` 

2. Suivez les instructions après avoir choisi un identifiant(username) et un mot de passe

3. Après avoir exécuter l'application (voir 2° ci-dessus), taper l'url suivante dans votre navigateur : http://127.0.0.1:8000/admin/

ou cliquer sur ce lien : [Site_LITRevu](http://127.0.0.1:8000/admin/)

4. Entrer votre identifiant et votre mot de passe pour accéder au site d'administration de Django : ce site permet de gérer toutes les opérations CRUD sur les données de l'application.









