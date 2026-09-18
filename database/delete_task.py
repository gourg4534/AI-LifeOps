from database.connection import SessionLocal
from database.models import Task


def delete_task(task_id):
    db = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if task:
        db.delete(task)
        db.commit()

        print("Task deleted successfully!")
        print("Deleted Task ID:", task_id)
    else:
        print("Task not found!")

    db.close()


if __name__ == "__main__":
    delete_task(1)
    