from flask import Blueprint, render_template, Response, jsonify, request
from auto_cam.model.camera import object_detection, VideoCamera
from auto_cam.model.models import Photo
import base64


views_blueprint = Blueprint('views', __name__, url_prefix='/')

@views_blueprint.route("/")
def index():
    return render_template("index.html")

@views_blueprint.route("/video_feed")
def video_feed():
    return Response(object_detection(), mimetype="multipart/x-mixed-replace; boundary=frame")

@views_blueprint.route('/photos', methods=['GET'])
def get_photos():
    photos = Photo.query.all()
    photos_list = [{'id': photo.id, 'img': base64.b64encode(photo.img).decode('utf-8')} for photo in photos]
    return jsonify(photos_list)

@views_blueprint.route('/reset_photos', methods=['POST'])
def reset_photos():
    try:
        VideoCamera.delete_all_photos_from_db()
        return jsonify({"message": "모든 사진이 삭제되었습니다."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500