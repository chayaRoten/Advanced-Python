from fastapi import FastAPI, Depends
import uvicorn
from controllers.taskController import task_router
from fastapi.staticfiles import StaticFiles
from controllers.userController import user_router

app = FastAPI()

app.include_router(task_router, prefix='/task')
app.include_router(user_router, prefix='/user')
app.mount("/static", StaticFiles(directory="../static"), name="static")


@app.on_event('startup')
async def print_something():
    print("mainController")

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="127.0.0.1")

