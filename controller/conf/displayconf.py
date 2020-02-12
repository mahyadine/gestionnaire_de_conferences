from model.connection import *
from controller.conf.gestionconf import *


class GestionConf():

    def menuconf(self):
    
        choix=""     
        print("\033[38m\n----------------------------------------\n\033[0m")
        print('\033[38mBienvenue dans le gestionnaire des conferences.\033[0m')
        print("\033[38m\n----------------------------------------\n\033[0m")
        while choix != "q":
        
            choix = input("\033[34m\n(p) Souhaitez vous creer une conference.\n(s) Souhaitez vous supprimer une conference.\n(v) Pour visualiser les conferences.\n(q) Pour quitter.\nVotre choix :\033[0m").lower()
            if choix == "p":          
                ajout = CreateConf()
                ajout.create()

            if choix == "s":        
                ajout = CreateConf()
                ajout.delete()

            if choix == "v":
                pass
        
            if choix == "q":
                print("A bientôt.")