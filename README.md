# __FR__

les drones DJI tello (petit drone intérieur pour enfants) ont une manette spéciale pour pouvoir les piloter sans toucher au smartphone, c'est le gamesir T1d. Le problème avec cette manette qui est très joli, on ne peut pas utiliser en dehors du pilotage de drone*, ce qui n'est pas cool quand on est maker bricoleur.

je me suis lancé les défis de trouver une solution pour utiliser le drone avec ne m'importe qu'appareils avec un bluetooth (ordinateur pour le moment). Des recherches sur le web m’ont permis de trouver ce site avec un code [original ](https://www.hsli.top/%E5%A4%A7%E7%96%86%E7%89%B9%E6%B4%9BTELLO%E6%89%8B%E6%9F%84%E7%9B%96%E4%B8%96%E5%B0%8F%E9%B8%A1Gamesir-T1D%E8%93%9D%E7%89%99%E8%BF%9E%E6%8E%A5%E7%A0%B4%E8%A7%A3DIY.html")  qui était en python 2, j'ai ajouté quelques modifications pour le mettre en python3, puis ajouter quelques fonctionnalités pour pouvoir simuler les touches du clavier 

ce code a été testé que sur Linux, je supporte qu'il aille marcher sur les autres systèmes d'exploitation (Mac os et Windows) 


## les besoins 

### logiciels

- python 3
- bluepy
- pynput 

### matériels 

- gamesir T1d 
- ordinateur avec bluetooth BLE 

## Installation sur linux/windows/Mac 
__assurez-vous que vous avez déjà installé python sur votre ordinateur  lien pour le faire au cas où__ [installer python3](https://www.python.org/downloads/) et vérifier que vous avez pip3 aussi 

- 1 télécharger ce dépôt actuel, faites extraction des fichiers puis ouvrent votre terminal et allez dans le dossier que vous venez d'extraire .

sur linux ca donne ca	
	
	cd /home/$USER/"le repertoire ou vous avez extrait le zip"

- 2 lancer la commande suivante:

		pip3 install -r requirements.txt


- 3 ouvrir le code avec votre éditeur et à la 9éme ligne remplacer l'adresse Mac bluetooth par celui de votre manette  (il est mentionné sur l'étiquette de la manette).


- 4 vous pouvez excuter le script (ou apportez des modification)

		python3 src/Gamecontrol.py 


## A vous d'améliorer le script

ce code est basique c'est à vous avec la librairie comme pynput de le compléter, c'était juste un Proof of concept, mais il y a  plein de possibilité. dans cet exemple j'ai juste configuré les 4 touches de directions mais vous pouvez compléter le reste il suffit juste de décommenter la partie debug du code, allumer la manette et voir sur le terminal le numéro qui s'affiche quand vos appuez sur une touche et en conséquence utilisée une condition (if) pour configurer d'autres touches 
		
Si vous avez besoin d'aide, contactez nous!
Email: diallo@bloctechno.com


# __EN__

the DJI tello drones (small indoor drone for children) have a special controller to be able to pilot them without touching the smartphone, it's the gamesir T1d. The problem with this joystick is that it's very pretty, you can't use it outside of drone piloting*, which is not cool when you're a do-it-yourself maker.

I challenged myself to find a solution to use the drone with any device with a bluetooth (computer for the moment). Research on the web has allowed me to find this site with a code [original ](https://www.hsli.top/%E5%A4%A7%E7%96%86%E7%89%B9%E6%B4%9BTELLO%E6%89%8B%E6%9F%84%E7%9B%96%E4%B8%96%E5%B0%8F%E9%B8%A1Gamesir-T1D%E8%93%9D%E7%89%99%E8%BF%9E%E6%8E%A5%E7%A0%B4%E8%A7%A3DIY.html") which was in python 2, I added some modifications to put it in python 3, then added some features to be able to simulate the keyboard keys 

this code has been tested only on Linux, I support that it will work on other operating systems (Mac os and Windows) 

## the needs 

### software

- python 3
- bluepy
- pynput 

### hardware 

- gamesir T1d 
- computer with bluetooth BLE 

## Installation on linux/windows/Mac 
__make sure you have already installed python on your computer link to do so in case__ [install python3](https://www.python.org/downloads/) and check that you have pip3 too 


- 1 download this current repository, extract the files then open your terminal and go to the folder you just extracted .

on linux it looks like this	
	
	cd /home/$USER/"the directory where you extracted the zip".

- 2 run the following command:

		pip3 install -r requirements.txt

- 3 open the code with your editor and on the 9th line replace the Mac bluetooth address by the one of your controller (it is mentioned on the label of the controller).

- 4 you can run the script (or make changes)
	
		python3 src/Gamecontrol.py 


## It's up to you to improve the script

this code is basic it's up to you with the library as a pynput to complete it, it was just a Proof of concept, but there are plenty of possibilities. in this example I just configured the 4 direction keys but you can complete the rest just uncomment the debug part of the code, turn on the joystick and see on the terminal the number that appears when you press a key and consequently used a condition (if) to configure other keys. 
		
If you need help, contact us!
Email: diallo@bloctechno.com


