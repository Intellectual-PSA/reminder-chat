import datetime

class Interaction:
    def __init__(self, date, message, from_person, to_person):
        self.date = date
        self.message = message
        self.from_person = from_person
        self.to_person = to_person

    def __str__(self):
        return f"Date: {self.date.strftime('%Y-%m-%d %H:%M:%S')}, From: {self.from_person}, To: {self.to_person}, Message: {self.message}"

class CommunicationLog:
    def __init__(self):
        self.log = []

    def add_interaction(self, message, from_person, to_person):
        interaction = Interaction(datetime.datetime.now(), message, from_person, to_person)
        self.log.append(interaction)
        print(f"Added interaction: {interaction}")

    def get_interactions(self, person_name):
        person_interactions = [str(interaction) for interaction in self.log if interaction.from_person == person_name or interaction.to_person == person_name]
        return person_interactions

# Sample usage
if __name__ == "__main__":
    comm_log = CommunicationLog()

    comm_log.add_interaction("Did you take my medication?", "Dad", "John")
    comm_log.add_interaction("No, I did not take your medication. It's in the usual spot.", "John", "Dad")
    comm_log.add_interaction("I can't find it. You must have taken it.", "Dad", "John")

    john_interactions = comm_log.get_interactions("John")

    for interaction in john_interactions:
        print(interaction)
