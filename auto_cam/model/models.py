from auto_cam import db


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.LargeBinary)

    def __init__(self, img_data):
        self.img = img_data
