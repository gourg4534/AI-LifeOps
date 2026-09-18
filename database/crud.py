from sqlalchemy.orm import Session
from database.models import Task


def create_task(
    db: Session,
    title: str,
    description: str | None = None
):
    task = Task(
        title=title,
        description=description,
        completed=False
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def get_tasks(db: Session):
    return db.query(Task).all()


def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def update_task(db: Session, task_id: int, completed: bool):
    task = get_task(db, task_id)

    if task:
        task.completed = completed
        db.commit()
        db.refresh(task)

    return task


def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)

    if task:
        db.delete(task)
        db.commit()

    return task
