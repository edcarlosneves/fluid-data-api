from xml.dom import NotFoundErr
from app.domain.fluid import Fluid
from app.domain.fluid_repository_interface import FluidRepository


class ListFluidRepository(FluidRepository):
    def __init__(self):
        self.fluids = []

    def add(self, fluid):
        self.fluids.append(fluid)
        return fluid

    def get_fluid(self, fluid_id):
        return [fluid for fluid in self.fluids if fluid.fluid_id == fluid_id]

    def all(self):
        return self.fluids
