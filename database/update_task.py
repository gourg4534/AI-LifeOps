from database.connection import SessionLocal
from database.models import Task


def complete_task(task_id):
    db = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if task:
        task.completed = True
        db.commit()
        db.refresh(task)

        print("Task completed successfully!")
        print("Task ID:", task.id)
        print("Completed:", task.completed)
    else:
        print("Task not found!")

    db.close()


if __name__ == "__main__":
    complete_task(1)
    