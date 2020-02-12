from model.connection import *

class CreateConf():

    def __init__(self):
        self.choice = connection()
        self.title = None
        self.resume = None
        self.date = None
        self.hour = None
        self.create_date = None
        self.speak_id = None

    def create(self,):
        self.choice.initialize_connection()
        self.title = input("Entrer un titre :").lower()
        self.resume = input("Entrer un resumé :").lower()
        self.date = input("Veuillez renseigner une date :").lower()
        self.hour = input("Veuillez renseigner une heure:").lower()
        self.speak_id = input("Veuillez entrer l'id du conferencier : ")
        self.choice.cursor.execute("INSERT INTO conf(title, resume, date, hour, speak_id) VALUES"
                                  "(%s, %s, %s, %s, %s)" ,(self.title, self.resume, self.date, self.hour, self.speak_id))
        self.choice.connection.commit()
        self.choice.close_connection()
        print(" La conference a bien etait ajouté ")