from models.ConnectionFactory import ConnectionFactory

import datetime

class Images():
    def __init__(self, filename, text, data):
        self.filename = filename
        self.text = text
        self.data = data

    def insert(self):
        connection = ConnectionFactory().get_connection()

        image = {
            "filename": self.filename,
            "text": self.text,
            "data": self.data,
            "created_at": datetime.datetime.now()
        }

        images = connection.images

        image_id = images.insert_one(image).inserted_id

        return image_id