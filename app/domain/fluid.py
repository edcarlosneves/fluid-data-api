import uuid
from dataclasses import dataclass, field


@dataclass
class Fluid:
    fluid_name: str
    fluid_temperature: float
    fluid_pressure: float
    fluid_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def save(self, fluid_repository):
        return fluid_repository.add(self)

    def __hash__(self):
        return hash(self.fluid_id)
