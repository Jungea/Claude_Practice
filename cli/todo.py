import argparse
from actions import add, list_todos, set_status, delete


def main():
    parser = argparse.ArgumentParser(prog="todo")
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("add")
    p_add.add_argument("title", nargs="+")
    p_add.add_argument("--priority", choices=["high", "medium", "low"], default="medium")
    p_add.add_argument("--due")

    p_list = sub.add_parser("list")
    p_list.add_argument("--status", choices=["todo", "in_progress", "done"])
    p_list.add_argument("--priority", choices=["high", "medium", "low"])

    p_status = sub.add_parser("status")
    p_status.add_argument("id", type=int)
    p_status.add_argument("value", choices=["todo", "in_progress", "done"])

    p_del = sub.add_parser("delete")
    p_del.add_argument("id", type=int)

    args = parser.parse_args()

    if args.command == "add":
        add(" ".join(args.title), priority=args.priority, due=args.due)
    elif args.command == "list":
        list_todos(status=args.status, priority=args.priority)
    elif args.command == "status":
        set_status(args.id, args.value)
    elif args.command == "delete":
        delete(args.id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
