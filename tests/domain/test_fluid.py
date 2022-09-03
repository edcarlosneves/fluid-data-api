import uuid
from app.domain.fluid import Fluid


def test_fluid_existing_fluid_id():
    fluid_id = str(uuid.uuid4())
