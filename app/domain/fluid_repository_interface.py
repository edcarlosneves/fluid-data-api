from abc import ABCMeta, abstractmethod

from app.domain.fluid import Fluid


class FluidRepository(metaclass=ABCMeta):
    @abstractmethod
    def add(self, fluid):
        raise NotImplementedError

    @abstractmethod
    def all(self):
        raise NotImplementedError

    @abstractmethod
    def get_fluid(self, fluid_id):
        raise NotImplementedError
