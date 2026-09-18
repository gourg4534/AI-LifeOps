from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.dependencies import get_db
from database import crud
from backend.schemas import TaskCreate, TaskUpdate, TaskResponse


router = APIRouter()


@router.post("/tasks", response_model=TaskResponse)
def create_task(
    task_data: TaskCreate,
    db: Session = Depends(get_db)
):
    task = crud.create_task(
        db=db,
        title=task_data.title,
        description=task_data.description
    )

    return task

@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db)
):
    tasks = crud.get_tasks(db=db)

    return tasks

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db)
):
    task = crud.update_task(
        db=db,
        task_id=task_id,
        completed=task_data.completed
    )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task

@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = crud.delete_task(
        db=db,
        task_id=task_id
    )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted successfully",
        "task_id": task_id
    }