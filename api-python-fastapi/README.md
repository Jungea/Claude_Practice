# Todo FastAPI

SQLite 기반 Todo REST API 서버.

## 설치 및 실행

```bash
pip install fastapi uvicorn sqlalchemy
cd app
uvicorn main:app --reload
```

Swagger UI: `http://localhost:8000/docs`

## 엔드포인트

| 엔드포인트 | 메서드 | 설명 |
|-----------|--------|------|
| `/health` | GET | 서버 상태 확인 |
| `/todos` | GET | 목록 조회 (status/priority 필터) |
| `/todos` | POST | 새 항목 추가 |
| `/todos/{id}/status` | PATCH | 상태 변경 |
| `/todos/{id}` | DELETE | 삭제 |

## 파일 구조

```
app/
├── main.py      # 앱 생성, 라우터, 엔드포인트
├── db.py        # SQLAlchemy 엔진/세션 설정
├── models.py    # DB 테이블 정의 (ORM)
├── schemas.py   # 요청/응답 데이터 검증 (Pydantic)
└── crud.py      # DB 조작 함수
```
