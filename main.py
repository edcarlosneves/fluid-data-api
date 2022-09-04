from app.adapter.python_list_fluid_repository import PythonListFluidRepository
from app.domain.fluid import Fluid

import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

fluid_repository = PythonListFluidRepository()


@app.post("/fluid", response_model=Fluid)
def insert_fluid(fluid: Fluid):
    try:
        return fluid.save(fluid_repository)
    except:
        raise HTTPException(status_code=409, detail="Duplicated id")


@app.get("/fluids")
def fluids():
    return fluid_repository.all()


@app.get("/fluid/{fluid_id}")
def get_fluid(fluid_id):
    fluid = fluid_repository.get_fluid(fluid_id)
    if fluid:
        return fluid
    raise HTTPException(status_code=404, detail="Item not found")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
