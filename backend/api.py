from fastapi import FastAPI
from backend.planner import Planner
from swarm.queue import enqueue
from swarm.worker import run_task
from backend.storage import Storage
from backend.assembler import Assembler


app = FastAPI()

planner = Planner()
storage = Storage()
assembler = Assembler()


@app.post("/run")
def run(goal: str):

    plan = planner.create_plan(goal)

    jobs = []

    for scene in plan["scenes"]:
        job = enqueue(run_task, scene)
        jobs.append(job.id)

    return {
        "status": "queued",
        "jobs": jobs,
        "plan": plan
    }


@app.post("/assemble")
def assemble():

    # placeholder local assembly step
    return {
        "status": "assembled",
        "file": "outputs/final.mp4"
    }
