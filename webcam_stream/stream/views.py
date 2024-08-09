# 뷰 정의! 웹캠 영상 처리 함수, 템플릿 렌더링 함수 포함
import cv2
from django.http import StreamingHttpResponse, JsonResponse
from django.views.decorators import gzip
from django.shortcuts import render
import random

def get_frame():
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1) 

        _, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@gzip.gzip_page
def live_stream(request):
    return StreamingHttpResponse(get_frame(), content_type="multipart/x-mixed-replace;boundary=frame")

def index(request):
    return render(request, 'stream/index.html')

def get_object_location(request):
    # 예시 좌표 생성 (실제로는 depth 카메라에서 얻은 좌표를 사용),
    object_location = {
        'lat': random.uniform(37.322558865511766, 37.32258357851774),  # 예시 위도
        'lng': random.uniform(127.12747748239246, 127.12753816657904) 
    }
    return JsonResponse(object_location)


def get_object_location2(request):
    # 예시 좌표 생성 (실제로는 depth 카메라에서 얻은 좌표를 사용),
    object_location = {
        'lat': random.uniform(37.320440, 37.320687),  # 예시 위도
        'lng': random.uniform(127.126437, 127.126781) 
    }
    return JsonResponse(object_location)
