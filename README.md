

# <h1 align="center">LITReview</h1>
</br>
<p align="center">
    <img src="https://user.oc-static.com/upload/2020/09/18/16004297044411_P7.png" 
            alt="le logo de LITReview" 
            width="250" 
            height="200"/>
</p>


LITReview est une application permettant à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande. 

# Installation :

1. Placez-vous dans le répertoire qui contiendra le projet 
  
2. Récupérer le code venant de GitHub (faire un clone) :  
    ```
    git clone https://github.com/glgstyle/LITReview.git
    cd LITReview
    ```
3. Créer un environnement virtuel : 

    ```python -m venv env```

    ou avec powershell:

    ```virtualenv env```

4. Activer l'environnement :  

    ```source env/bin/activate ```

    ou avec powershell:
    
    ```env\bin\activate```

5. Installer les packages :

    ```pip install -r requirements.txt```  
    ```pip freeze``` (pour vérifier que les packages se sont bien installés)

# Utilisation

- Pour supprimer la base de données:

1. Supprimer le fichier db.sqlite3

2. Tapper dans la console la commande suivante:

    ```python manage.py migrate```


- Pour utiliser le site:

1. Démarrer le serveur avec la commande suivante:

    ```python manage.py runserver```  

2. Rendez vous à l'adresse suivante dans votre navigateur internet:

    http://127.0.0.1:8000/  


- Pour gérer l'interface d'aministration:

1. Créer un super user avec la commande suivante:

    ```python manage.py createsuperuser```

2. Saisir le nom d’utilisateur souhaité et appuyez sur entrée exemple:

    ```Username: admin```

3. Saisir l’adresse mail souhaitée exemple:

    ```Email address: admin@example.com```

4. L’étape finale est de saisir le mot de passe. On vous demande de le saisir deux fois, la seconde fois étant une confirmation de la première:

    ```Password: **********```

    ```Password (again): *********```
    
    ```Superuser created successfully.```

5. À présent, ouvrez un navigateur Web et allez à l’URL « /admin/ » de votre domaine local – par exemple, http://127.0.0.1:8000/admin/.
   Vous devriez voir l’écran de connexion à l’interface d’administration.
