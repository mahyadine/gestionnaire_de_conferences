
class Hydra():
    def __init__(self, i=False):
        self.title = None
        self.resume = None
        self.date = None
        self.hour = None
        self.create_date = None
        self.speak_id = None
        self.id = None
        self.fristname = None
        self.name = None
        if i:
            self.hydrat(i)

    def hydrat(self, i):
        for key, value in i.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        return """\033[36m Le titre: {}\n Le resume: {}\n La date : {}\n L'heure : {}\n Speak_id : {}\n id : {}\n Le nom du conferencier : {}\n Le prenom du conferencier : {}\n~~~~~~~~~~~~~~~~~~~~\033[0m""".format(self.title, self.resume, self.date, self.hour, self.speak_id, self.id, self.fristname, self.name)