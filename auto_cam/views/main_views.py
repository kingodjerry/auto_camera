from flask import Blueprint, render_template, Response, jsonify
from auto_cam.model.detection import generate_frames
from auto_cam.model.models import Photo

views_blueprint = Blueprint('views', __name__, url_prefix='/')

@views_blueprint.route("/")
def index():
    return render_template("index.html")

@views_blueprint.route("/video_feed")
def video_feed():
    return Response(generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")

@views_blueprint.route('/photos', methods=['GET'])
def get_photos():
    photos = Photo.query.all()
    photos_list = [{'id': photo.id, 'filename': photo.filename, 'filepath': photo.filepath} for photo in photos]
    return jsonify(photos_list)
