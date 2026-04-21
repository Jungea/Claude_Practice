# TODO CLI

터미널에서 할 일을 관리하는 간단한 CLI 프로그램입니다.

---

## 실행 방법

Python 3이 설치되어 있으면 별도 설치 없이 바로 실행할 수 있습니다.

```bash
python3 todo.py <명령어>
```

---

## 지원 기능

| 명령어 | 설명 | 예시 |
|--------|------|------|
| `add` | 할 일 추가 | `python3 todo.py add 책 읽기` |
| `add` (옵션 포함) | 우선순위·마감일 지정 | `python3 todo.py add 보고서 작성 --priority high --due 2026-04-25` |
| `list` | 목록 보기 | `python3 todo.py list` |
| `list` (필터) | 상태·우선순위 필터 | `python3 todo.py list --status todo --priority high` |
| `status` | 상태 변경 | `python3 todo.py status 1 in_progress` |
| `delete` | 항목 삭제 | `python3 todo.py delete 1` |

### add 옵션

| 옵션 | 값 | 기본값 |
|---|---|---|
| `--priority` | `high` / `medium` / `low` | `medium` |
| `--due` | `YYYY-MM-DD` | 없음 |

### list 필터 옵션

| 옵션 | 값 |
|---|---|
| `--status` | `todo` / `in_progress` / `done` |
| `--priority` | `high` / `medium` / `low` |

### status 값

| 값 | 의미 |
|---|---|
| `todo` | 미완료 |
| `in_progress` | 진행 중 |
| `done` | 완료 |

---

## 출력 형식

```
[상태][중요도] 번호. 제목  마감일
```

| 기호 | 의미 |
|---|---|
| `[ ]` | 미완료 |
| `[~]` | 진행 중 |
| `[x]` | 완료 |
| `[!]` | 높은 우선순위 |
| `[-]` | 보통 우선순위 |
| `[v]` | 낮은 우선순위 |

**실행 예시**

```
[ ][!] 1. 보고서 작성  2026-04-25
[~][-] 2. 코드 리뷰
[x][-] 3. 운동하기

[ 오늘 마감 ]
  [!] 1. 보고서 작성
```

목록은 done 항목이 마지막, 그 안에서 우선순위 높은 순으로 정렬됩니다.
마감일이 지난 항목은 `[마감초과]` 표시가 붙습니다.
오늘 마감인 미완료 항목은 목록 하단에 별도로 모아서 표시됩니다.

---

## 파일 구조

```
01-todo-cli/
├── todo.py       # 진입점 — 명령어 파싱 및 실행 (argparse)
├── actions.py    # 기능 로직 — add, list, set_status, delete
├── storage.py    # 데이터 — JSON 파일 읽기/쓰기
└── todos.json    # 할 일 저장 파일 (자동 생성)
```

---

## 저장 방식

할 일은 `todos.json` 파일에 저장됩니다. 프로그램을 종료해도 데이터가 유지됩니다.

```json
[
  {
    "id": 1,
    "title": "보고서 작성",
    "status": "todo",
    "priority": "high",
    "due": "2026-04-25",
    "created_at": "2026-04-20"
  }
]
```

각 항목의 구성:

| 필드 | 설명 |
|---|---|
| `id` | 고유 번호 (자동 증가) |
| `title` | 할 일 내용 |
| `status` | 상태 (`todo` / `in_progress` / `done`) |
| `priority` | 우선순위 (`high` / `medium` / `low`) |
| `due` | 마감일 (`YYYY-MM-DD`, 선택) |
| `created_at` | 생성일 (자동 기록) |
