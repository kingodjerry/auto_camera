# 행동감지 자동촬영 카메라 WebAPP

## 문제
2024 여름, 하노이로 휴가를 떠나기로 하는데…! <br>
단체 사진을 찍고 싶지만 찍어달라고 부탁하기도 싫고(신뢰 zero), 타이머 설정도 귀찮아서 <br>
행동을 감지하여(포즈를 취하면) 자동 촬영되는 카메라를 제작하기로 했다. <br>

## 기능
1. 웹캠과 카메라 화면 연결
2. 행동감지 : 브이(Peace sign)
3. 행동 감지 시 사진 촬영
4. DB에 사진 저장 <br>

## 사용 기술 및 모델, 데이터셋
**Language** : python, JS <br>
**Framework** : flask <br>
**AI model** : YOLOv5 <br>
**Dataset** : https://universe.roboflow.com/watermark-dqqep/peace_sign_v2 (train : 2664, test 72, val : 76)  <br>
**DB** : SQLite <br>
**Configuration Settings** : Colab, VScode, git, github <br>

## 파일 구조
```
📦Auto_cam
 ┣ 📂auto_cam
 ┃ ┣ 📂model
 ┃ ┃ ┣ 📜best.pt (custom model)
 ┃ ┃ ┣ 📜camera.py (Cam & Object detection)
 ┃ ┃ ┗ 📜models.py (DB)
 ┃ ┣ 📂static
 ┃ ┃ ┣ 📜index.css
 ┃ ┃ ┗ 📜index.js
 ┃ ┣ 📂templates
 ┃ ┃ ┗ 📜index.html
 ┃ ┣ 📂views
 ┃ ┃ ┗ 📜main_views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂migrations
 ┣ 📂yolov5 (git clone)
 ┗ 📜auto_cam.db
```

## 기술 설명
YOLOv5은 Object detection(객체 인식) 분야에서 널리 사용되는 딥러닝 모델로, 이미지나 동영상에서 객체를 빠르게 탐지하고 분류하는 데 특화된 모델이다. YOLOv5는 YOLO 시리즈의 다섯 번째 버전으로, 이전 버전에 비해 개선된 성능과 효율성을 제공한다. 
<br>
- **높은 속도와 정확성**
- **경량화** : 모델의 크기가 작아 다양한 하드웨어에서 작동할수 있어, 모바일 디바이스에서도 사용가능하다.
- **사용 편의성** : 모델을 쉽게 트레이닝하고 배포할 수 있도록 다양한 툴과 프레임워크를 지원한다.
- YOLOv5는 보안, 자율주행, 로봇공학, 드론, 의료 영상 등 다양한 분야에서 활용되고 있다.
<br>
해당 프로젝트에서는 브이(Peace) 포즈를 인식하면 사진이 자동 촬영되도록 기존의 YOLOv5를 Fine-tuning 하였다.

## 성능
Prediction : 0.967 / Recall : 0.949 / mAP50 : 0.973 <br>

<div>  
  <img src="https://github.com/kingodjerry/auto_camera/assets/143167244/c8532b3c-7f11-4d96-8767-ad1d590b2c10" width="50%"><img src="https://github.com/kingodjerry/auto_camera/assets/143167244/35a19183-fbb3-42a1-ae3c-ff3debbb4fff" width="50%"> 
</div>

<img width=100% src="https://github.com/kingodjerry/auto_camera/assets/143167244/d57d5b81-1362-4c57-9ec4-8bd53a1d4c22"></img>

## 테스트 화면

<div>
<img width=33% height=100% src="https://github.com/kingodjerry/auto_camera/assets/143167244/6defd17b-5ae3-4844-8cb6-3f01f07358b6"></img><img width=33% height=100% src="https://github.com/kingodjerry/auto_camera/assets/143167244/7cddcc5a-67de-4e31-b395-6d1b25bdeb64"></img><img width=34% height=100% src="https://github.com/kingodjerry/auto_camera/assets/143167244/c65b67dd-e4aa-4358-bb69-52ce0695bf1e"></img>
</div>

## 실행 화면
![image](https://github.com/kingodjerry/auto_camera/assets/143167244/f54aebaf-dbea-4a7c-9cd2-dbe46198e5e8)

