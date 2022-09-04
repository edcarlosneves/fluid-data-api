from app.domain.fluid_repository import FluidRepository


class PythonListFluidRepository(FluidRepository):
    def __init__(self):
        self.fluids = []

    def add(self, fluid):
        if self.get_fluid(fluid.fluid_id):
            raise Exception("Dupicated id")

        self.fluids.append(fluid)
        return fluid

    def all(self):
        return self.fluids

    def get_fluid(self, fluid_id):
        return [fluid for fluid in self.fluids if fluid.fluid_id == fluid_id]
