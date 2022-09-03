from app.domain.fluid_repository import FluidRepository


class InMemoryFluidRepository(FluidRepository):
    def __init__(self):
        self.fluids = []

    def add(self, fluid):
        self.fluids.append(fluid)
        return fluid

    def all(self):
        return self.fluids

    def get_fluid(self, fluid_id):
        return [fluid for fluid in self.fluids if fluid.fluid_id == fluid_id]
