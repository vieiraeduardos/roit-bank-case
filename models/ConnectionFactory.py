from pymongo import MongoClient

class ConnectionFactory():
    def __init__(self):
        self.localhost = "localhost"
        self.port = 27017
        self.dataset_name = "images_db"

    def get_connection(self):
        connection = MongoClient(self.localhost, self.port)
        return connection[self.dataset_name]