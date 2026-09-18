from database.connection import SessionLocal
from database.models import Task


def create_task():
    db = SessionLocal()

    task = Task(
        title="Learn Python for AI Engineering",
        description="Complete Python fundamentals and practice coding.",
        completed=False
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    print("Task created successfully!")
    print("Task ID:", task.id)
    print("Task Title:", task.title)

    db.close()


if __name__ == "__main__":
    create_task()
    