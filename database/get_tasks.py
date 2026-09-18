from database.connection import SessionLocal
from database.models import Task


def get_tasks():
    db = SessionLocal()

    tasks = db.query(Task).all()

    for task in tasks:
        print("ID:", task.id)
        print("Title:", task.title)
        print("Description:", task.description)
        print("Completed:", task.completed)
        print("-" * 40)

    db.close()


if __name__ == "__main__":
    get_tasks()