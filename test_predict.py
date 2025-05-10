import requests
import time
import random
from PIL import Image

# 1x1 픽셀짜리 흰색 이미지 생성
image = Image.new("RGB", (1, 1), (255, 255, 255))
image.save("dummy.png")

URL = "http://localhost:8000/predict"
NUM_REQUESTS = 30

for i in range(NUM_REQUESTS):
    label = random.randint(0, 9)

    # dummy image payload (빈 파일로 충분)
    files = {'file': ('dummy.png', open('dummy.png', 'rb'), 'image/png')}
    data = {'label': 3}

    try:
        response = requests.post(URL, files=files, data=data)
        print(f"[{i+1:02}] Status: {response.status_code}, Response: {response.json()}")
    except Exception as e:
        print(f"[{i+1:02}] ❌ Request failed: {e}")

    time.sleep(1)  # 1초 간격으로 요청 전송
