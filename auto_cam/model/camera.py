import torch
import cv2
import time
import sqlite3
import pathlib
from auto_cam.model.models import db, Photo

# Windows 경로 오류 해결 코드
pathlib.PosixPath = pathlib.WindowsPath

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(cv2.CAP_DSHOW)
        if not self.video.isOpened():
            print("에러: 비디오를 찾을 수 없습니다.")
            exit()
    
    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()
        return ret, frame
    
    @staticmethod
    def save_frame_to_db(frame):
        try:
            print(f"DB에 이미지 저장중 ...")
            _, buffer = cv2.imencode('.jpg', frame)
            image_data = buffer.tobytes()

            conn = sqlite3.connect('./auto_cam.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Photo (img) VALUES (?)', (sqlite3.Binary(image_data),))
            conn.commit()
            conn.close()
            print("DB에 성공적으로 저장되었습니다.")
        except Exception as e:
            print(f"DB 저장 중 에러 발생: {e}")

    
    @staticmethod
    def delete_all_photos_from_db():
        try:
            conn = sqlite3.connect('./auto_cam.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM Photo')
            conn.commit()
            conn.close()
            print("모든 파일이 성공적으로 삭제되었습니다.")
        except Exception as e:
            print(f"데이터베이스에서 파일 삭제 중 에러 발생: {e}")

# 모델 로드
model = torch.hub.load('./yolov5', 'custom', './auto_cam/model/best.pt', source='local')

def object_detection():
    video_cam = VideoCamera()

    while True:
        ret, frame = video_cam.get_frame()

        if not ret:
            print("카메라를 연결할 수 없습니다.")
            break

        results = model(frame)

        if results.xyxy[0].shape[0] > 0:  
            for *box, conf, cls in results.xyxy[0]:  
                if conf > 0.80: 
                    label = f"{conf:.2f}"
                    cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 255, 0), 2)
                    cv2.putText(frame, label, (int(box[0]), int(box[1] - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    
                    # 프레임 저장 및 DB에 저장
                    video_cam.save_frame_to_db(frame)
                    time.sleep(2)

        frame_with_boxes = results.render()[0]

        ret, buffer = cv2.imencode('.jpg', frame_with_boxes)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

  
