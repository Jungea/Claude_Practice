# claude_practice

Python 학습용 프로젝트. CLI TODO 앱과 FastAPI 웹 앱으로 구성.

## 구조

```
claude_practice/
├── cli/              # CLI TODO 앱 (JSON 파일 기반)
│   ├── todo.py       # 진입점, argparse
│   ├── actions.py    # add / list / status / delete 로직
│   └── storage.py    # todos.json 읽기/쓰기
│
└── app/              # FastAPI 웹 앱 (SQLite 기반)
    ├── main.py       # 앱 생성, 라우터, 엔드포인트
    ├── db.py         # SQLAlchemy 엔진/세션 설정
    ├── models.py     # DB 테이블 정의 (ORM)
    ├── schemas.py    # 요청/응답 데이터 검증 (Pydantic)
    └── crud.py       # DB 조작 함수
```

실행 방법은 각 폴더의 README를 참고하세요.
- CLI: [cli/README.md](cli/README.md)
- FastAPI: [app/README.md](app/README.md)
