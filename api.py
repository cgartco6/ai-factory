from fastapi import FastAPI
from planner import Planner
from core.queue import enqueue
from worker_runner import handle_job
from assembler import Assembler


app = FastAPI()

planner = Planner()
assembler = Assembler()


@app.post("/run")
def run(goal: str):

    plan = planner.create_plan(goal)

    jobs = []

    for scene in plan["scenes"]:
        job = enqueue(handle_job, scene)
        jobs.append(job.id)

    return {
        "status": "queued",
        "jobs": jobs,
        "plan": plan
    }
