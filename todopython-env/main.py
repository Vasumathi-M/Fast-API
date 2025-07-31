from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

TodoList = {
    1: {
        "taskname": "VDSA",
        "taskdescription": "Watch atleast 3 videos per day",
        "assigneduser": "Vasu"
    },
    2: {
        "taskname": "Kunal Kushwaha",
        "taskdescription": "Watch atleast 1 video per day",
        "assigneduser": "Mathi"
    }
}

@app.get('/displaytasks')
def displayTasks():
    return TodoList


#pydantic model - adding
class createTaskModel(BaseModel):
    taskId: int
    taskname: str
    taskdescription: str
    assigneduser: str
    moreinfo: str | None = None

@app.post('/createtask')
def createTask(task: createTaskModel): 
    if not TodoList:
        new_id = 1
    else:
        new_id = max(TodoList.keys()) + 1

    # Convert task to dict and override taskId
    task_dict = task.model_dump()
    task_dict["taskId"] = new_id

    TodoList[new_id] = task_dict
    return {"msg": "Task created", "data": task_dict}


#pydantic model - updating
class Taskupdatemodel(BaseModel):
    taskname: Optional[str]=None
    taskdescription: Optional[str]=None
    assigneduser: Optional[str]=None
    moreinfo: Optional[str]=None

@app.put('/updatetaask/{task_id}')
def update_task(task_id:int,task:Taskupdatemodel):
    if task_id not in TodoList:
        return f"No task in this taskid={task_id}"
    #updating the new info 
    if task.taskname is not None:
        TodoList[task_id]['taskname']=task.taskname
    if task.taskdescription is not None:
        TodoList[task_id]['taskdescription']=task.taskdescription
    if task.moreinfo is not None:
        TodoList[task_id]['moreinfo']=task.moreinfo
    if task.assigneduser is not None:
        TodoList[task_id]['assigneduser']=task.assigneduser 
    return TodoList[task_id]


@app.delete('/deleteuser/{task_id}')
def deleteTask(task_id:int):
    if task_id not in TodoList:
        return f"No task found with taskid={task_id} to delete it"
    del TodoList[task_id] #deletes the id
    return f"succesfully deleted {task_id}"
    
