from model.connection import *
from model.entities import *

class CreateConf():

    def __init__(self):
        self.choice = connection()
        self.title = None
        self.resume = None
        self.date = None
        self.hour = None
        self.create_date = None
        self.speak_id = None
        self.id = None

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

    def delete(self):
        """"method for delte user account after connect to bdd"""
        self.choice.initialize_connection()
        self.id =  input("Veullez entrer id de la conferecence : ")
        self.choice.cursor.execute("DELETE FROM conf WHERE id = %s;", (self.id,))
        self.choice.connection.commit()
        self.choice.close_connection()
        print(" Le conference a bien etait supprimé ")

    def show(self):
        """method for show account"""
        sql = """SELECT * FROM conf, speaker WHERE speaker_id= speak_id"""
        self.choice.initialize_connection()
        self.choice.cursor.execute(sql)
        test = self.choice.cursor.fetchall()
        self.choice.close_connection()
        for key, value in enumerate(test):
            test[key] = Hydra(value)
        return test

    def show_conference(self):
        test = self.show()
        if test:
            for i in test:
                print (i)