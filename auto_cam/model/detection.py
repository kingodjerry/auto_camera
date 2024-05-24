import torch
import cv2
import time
import os
from .models import Photo, db

# windows path error 해결 코드
import pathlib
pathlib.PosixPath = pathlib.WindowsPath

# 모델 로드
model = torch.hub.load('./yolov5', 'custom', './auto_cam/model/best.pt', source='local')

def generate_frames():
    cap = cv2.VideoCapture(0)  # 기본 카메라 사용
    if not cap.isOpened():
        print("에러 : 비디오를 찾을 수 없습니다.")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # custom 모델로 추론
        results = model(frame)

        # 정확도가 90% 이상인 경우 프레임 저장
        if results.xyxy[0].shape[0] > 0:  # 감지된 객체가 있는 경우
            for *box, conf, cls in results.xyxy[0]:  # 각 감지된 객체에 대해
                if conf > 0.50:  # 정확도가 90% 이상인 경우
                    name = f"captured_frame_{int(time.time())}.jpg"
                    path = os.path.join('static/photos', name)
                    cv2.imwrite(path, frame)
                    print(f"프레임 캡처 및 저장: {name}")
                    time.sleep(2)

                    # 데이터베이스에 저장
                    new_photo = Photo(filename=name, filepath=path)
                    db.session.add(new_photo)
                    db.session.commit()

        frame_with_boxes = results.render()[0]

        # 프레임을 JPEG 형식으로 인코딩
        ret, buffer = cv2.imencode('.jpg', frame_with_boxes)
        frame = buffer.tobytes()

        # 인코딩된 프레임을 한 번에 하나씩 반환
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()
