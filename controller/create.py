from model.connection import *
from model.hydra import *

class CreateSpeaker():

    def __init__(self,):
        self.choice = connection()
        self.fristname = None
        self.name = None
        self.description = None
        self.job = None
        self.status = True
        self.speaker_id = None
        
        

    def create(self,):
        self.choice.initialize_connection()
        self.fristname = input("Entrer votre prénom :").lower()
        self.name = input("Entrer votre nom :").lower()
        self.job = input("Veuillez renseigner votre métier :").lower()
        self.description = input("Entrer une description :").lower()
        self.choice.cursor.execute("INSERT INTO speaker(fristname, name, job, description) VALUES"
                                  "(%s, %s, %s, %s)" ,(self.fristname, self.name, self.job, self.description))
        self.choice.connection.commit()
        self.choice.close_connection()
        print(" Le conferencier a bien etait enregistré ")


    def delete(self):
        """"method for delte user account after connect to bdd"""
        self.choice.initialize_connection()
        self.speaker_id =  input("Veullez entrer id speaker : ")
        self.choice.cursor.execute("DELETE FROM speaker WHERE speaker_id = %s;", (self.speaker_id,))
        self.choice.connection.commit()
        self.choice.close_connection()
        print(" Le conferencier a bien etait supprimé ")

    def show(self):
        """method for show account"""
        sql = """SELECT * FROM speaker"""
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


    