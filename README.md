# 🧠 FastAPI + Prometheus 예측 API 서버

이 프로젝트는 **FastAPI**로 구축된 예측 API에 **Prometheus** 메트릭 수집 기능을 통합한 예제입니다.  
간단한 추론 시뮬레이션과 성능 메트릭 수집이 포함되어 있습니다.

## 📦 구성 요소

- `FastAPI`: API 서버
- `Prometheus`: 메트릭 수집 및 시각화
- `Docker Compose`: 전체 서비스 컨테이너화

## 🚀 실행 방법

### 1. Docker Compose로 실행

```bash
docker compose up --build
```

### 2. 테스트 스크립트 실행

```bash
python test_predict.py
```
