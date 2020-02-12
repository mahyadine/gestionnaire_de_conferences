from model.connection import *
from controller.conferencier.speaker import *
from controller.conf.displayconf import *



if __name__=='__main__':


    
    choix=""     
    print("\033[32m\n----------------------------------------\n\033[0m")
    print('\033[32mBienvenue dans votre planning.\033[0m')
    print("\033[32m\n----------------------------------------\n\033[0m")
    while choix != "q":
       
        choix = input("\033[32m\n(p) Souhaitez vous gerer les conferenciers.\n(s) Souhaitez vous gerer les conferences.\n(q) Pour quitter.\nVotre choix :\033[0m").lower()
        if choix == "p":          
            gestionspeaker = GestionSpeaker()
            gestionspeaker.menu()

        if choix == "s":        
            gestionconf = GestionConf()
            gestionconf.menuconf()
      
        if choix == "q":
            print("A bientôt.")