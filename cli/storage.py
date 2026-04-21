import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "todos.json"


def load_todos():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE) as f:
        todos = json.load(f)
    for todo in todos:
        if "done" in todo:
            todo["status"] = "done" if todo.pop("done") else "todo"
    return todos


def save_todos(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2, ensure_ascii=False)
