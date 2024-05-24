from auto_cam import db


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
    filepath = db.Column(db.String(255))

    def __init__(self, filename, filepath):
        self.filename = filename
        self.filepath = filepath
