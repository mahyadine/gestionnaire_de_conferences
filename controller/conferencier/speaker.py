from model.connection import *
from controller.conferencier.speaker import *
from controller.conferencier.create import *


class GestionSpeaker():

    def menu(self):
    
        choix=""     
        print("\033[35m\n----------------------------------------\n\033[0m")
        print('\033[35mBienvenue dans la gestion des conferenciers.\033[0m')
        print("\033[35m\n----------------------------------------\n\033[0m")
        while choix != "q":
        
            choix = input("\033[34m\n(p) Souhaitez vous creer un conferencier.\n(s) Souhaitez vous supprimer un conferencier.\n(v) Pour visualiser les conferenciers.\n(q) Pour quitter.\nVotre choix :\033[0m").lower()
            if choix == "p":          
                log = CreateSpeaker()
                log.create()

            if choix == "s":        
                log = CreateSpeaker()
                log.delete()

            if choix == "v":
                log = CreateSpeaker()
                log.show_conference()
        
            if choix == "q":
                print("A bientôt.")