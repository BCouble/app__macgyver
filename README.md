
install python 3 and pygame 1.9.4

Projet 3 : Aider Mac GYVER à s’échapper.

Initialisation du projet :
Création du Repo :
https://github.com/BCouble/app__macgyver.git
Installation et configuration de l’environnement virtuel avec pygame.

Structure des fichiers et vue d’ensemble :
L’application comprend sept fichiers « .py », un fichier csv pour la map et les fichiers des images.
Pour les fichiers .py : 
-	Les cinq classes : maze.py, macgyver.py, item.py, gardian.py et interaction.py
-	Les constantes : constante.py
-	Le fichier principal : mgLabyrinth.py
-	La map : dans « assets/map/ » maze.csv
-	Les images : dans « assets/images/ »
Les classes sont construite dans cette logique :
1 – les premières fonctions gèrent la matrice, la logique de classe. (Contrôleur)
2 – dans un second plan nous avons la gestion de l’affichage. (Vue)
Le fichier principal structure et logique :
Cinq fonctions et la fonction main : 
-	Les cinq fonctions : 
o	« init_window » pour la fenêtre de jeu, 
o	« init_game » pour initialiser la partie, 
o	« move_player » pour les déplacements du héros, 
o	« rebuild_windows » pour rafraichir l’écran et l’avancé de la partie,
o	« management_interaction » pour gérer les rencontres entre le héros, les objets et le gardien touffu.

-	La fonction main (deux boucle while) : 
o	La première : Attend que le joueur démarre la partie et initialise le jeu avec la touche « s » envoie dans la deuxième boucle
o	La seconde : Attend que le joueur se déplace, ramasse les objets, gère la rencontre avec le gardien touffu (renvoie à la première boucle après la rencontre avec le gardien).

« J’ai fait évoluer le fichier principal au fil du temps en construisant les classes. »






Etape 1 : 
Création du labyrinthe
J’ai commencé par lire la formation sur pygame, puis je suis aussi allé voir comment d’autre élèves OCR avait réalisé le projet.
Pour réaliser la map j’ai utilisé un fichier maze.csv enregistré dans « \assets\map », à la lecture du fichier la classe maze fabrique une liste à double entrée (la matrice).
Le fichier csv utilise 4 symboles qui seront convertis en sprite:
-	Le départ : D,
-	Les chemins : #,
-	Les murs : M,¬
-	L’arrivé : G (gardien)

Etape 2 :
Pour la création de Mac GYVER, j’ai créé la classe macgyver, elle gère l’image et sa position pour les déplacements du héros.
Pour la création du gardien touffu, j’ai créé la classe gardian, ce n’est pas vraiment utile pour le moment, mais si l’envie d’implémenter une ronde nous pourrions nous servir de cette classe.

Etape 3 :
Création des objets à partir d’une liste dans le fichier des constantes :
Nous récupérons la liste pour ajouter la position aléatoire, nous vérifions que les objets ne se superpose pas et nous construisons une nouvelle liste qui servira pour l’affichage des objets.
Problématique : 
Vérification du bon fonctionnement de la fonction que vérifie si les objets ne se superpose pas : J’ai dû créer un second fichier « csv » avec très peu de chemin pour vérifier cette fonction.

Etape 4 : 
Implémentation des interactions :
	1 – Avec le gardien : lorsque le héros rencontre le gardien la fonction renvoie l’écran de victoire si l’inventaire est plein ou de défaite dans le cas contraire.
Une option pour refaire une partie.
	2 – Avec les objets : lorsque le héros ramasse un objet en passant dessus la fonction remplit en même temps l’inventaire.
	3 – Création de la Seringue : lorsque l’inventaire est plein nous créons la seringue.
