import time
import random
from fastapi import FastAPI, UploadFile, Request, Form
from fastapi.responses import Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST


app = FastAPI()

# ✅ Prometheus Metrics 선언
REQUEST_COUNT = Counter("request_count", "Total number of requests", ["endpoint", "method", "http_status"])
REQUEST_LATENCY = Histogram("request_latency_seconds", "Request latency", ["endpoint"])
INFERENCE_TIME = Histogram("model_inference_seconds", "Model inference time")
PREDICTION_CORRECT = Counter("prediction_correct_count", "Number of correct predictions")
PREDICTION_INCORRECT = Counter("prediction_incorrect_count", "Number of incorrect predictions")

# ✅ Dummy model inference 함수 (랜덤 예측)
def dummy_model_inference(image_data):
    predicted_label = random.randint(0, 9)
    confidence = round(random.uniform(0.6, 1.0), 4)
    return predicted_label, confidence

# ✅ /metrics endpoint
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

# ✅ /predict endpoint
@app.post("/predict")
async def predict(file: UploadFile, label: int = Form(...)):
    start_time = time.time()

    # 이미지 로딩 (실제로는 사용 안 함)
    await file.read()

    # ⏱ 추론 시작
    inference_start = time.time()
    predicted_label, confidence = dummy_model_inference(None)
    inference_duration = time.time() - inference_start
    duration = time.time() - start_time

    # ✅ 메트릭 기록
    REQUEST_COUNT.labels(endpoint="/predict", method="POST", http_status=200).inc()
    REQUEST_LATENCY.labels(endpoint="/predict").observe(duration)
    INFERENCE_TIME.observe(inference_duration)

    if predicted_label == label:
        PREDICTION_CORRECT.inc()
    else:
        PREDICTION_INCORRECT.inc()

    return {"prediction": predicted_label, "confidence": confidence}
