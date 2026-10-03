from fastapi import FastAPI      #这个FastAPI是用来创建一个FastAPI实例
from pydantic import BaseModel     #这个BaseModel是用来定义数据模型的    pydantic是一个用于数据验证和转换的库
from storage import save_experiments, load_experiments
from models import Experiment #这个Experiment是用来定义实验数据的模型的

app = FastAPI()

class ExperimentModel(BaseModel):
    exp_id: str
    temperature: float
    pressure: float
    catalyst: str
    yield_rate: float

@app.post("/add_experiment")       #这个装饰器是用来定义一个POST请求的路由
def add_experiment(exp: ExperimentModel):
    """接收化工数据，写入数据库"""
    experiments = load_experiments()
    experiments.append(Experiment(
        exp_id=exp.exp_id, temperature=exp.temperature,
        pressure=exp.pressure, catalyst=exp.catalyst, yield_rate=exp.yield_rate
    ))
    save_experiments(experiments)   #这个函数是用来将实验数据写入数据库
    return {"status": "success", "message": "化工实验数据添加成功"}