from datetime import date
from storage import load_todos, save_todos


def add(title, priority="medium", due=None):
    todos = load_todos()
    next_id = max((t["id"] for t in todos), default=0) + 1
    todos.append({
        "id": next_id,
        "title": title,
        "status": "todo",
        "priority": priority,
        "due": due,
        "created_at": date.today().isoformat(),
    })
    save_todos(todos)
    print(f"추가됨: {title}")


PRIORITY_LABEL = {"high": "!", "medium": "-", "low": "v"}
STATUS_LABEL   = {"todo": " ", "in_progress": "~", "done": "x"}
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}
STATUS_ORDER   = {"todo": 0, "in_progress": 0, "done": 1}


def list_todos(status=None, priority=None):
    todos = load_todos()
    if status:
        todos = [t for t in todos if t.get("status") == status]
    if priority:
        todos = [t for t in todos if t.get("priority") == priority]
    todos.sort(key=lambda t: (
        STATUS_ORDER.get(t.get("status", "todo"), 0),
        PRIORITY_ORDER.get(t.get("priority", "medium"), 1),
    ))
    if not todos:
        print("할 일이 없습니다.")
        return
    today = date.today().isoformat()
    for t in todos:
        s = STATUS_LABEL.get(t.get("status", "todo"), " ")
        p = PRIORITY_LABEL.get(t.get("priority", "medium"), "-")
        due = t.get("due") or ""
        overdue = " [마감초과]" if due and due < today else ""
        print(f"[{s}][{p}] {t['id']}. {t['title']}  {due}{overdue}")

    today_due = [t for t in todos if t.get("due") == today and t.get("status") != "done"]
    if today_due:
        print("\n[ 오늘 마감 ]")
        for t in today_due:
            p = PRIORITY_LABEL.get(t.get("priority", "medium"), "-")
            print(f"  [{p}] {t['id']}. {t['title']}")


def set_status(todo_id, status):
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["status"] = status
            save_todos(todos)
            print(f"[{status}] {todo['title']}")
            return
    print(f"오류: {todo_id}번 항목이 없습니다.")


def delete(todo_id):
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            save_todos(todos)
            print(f"삭제됨: {todo['title']}")
            return
    print(f"오류: {todo_id}번 항목이 없습니다.")
