import uuid

from app.domain.fluid import Fluid


def test_fluid_existing_fluid_id():
    fluid_id = str(uuid.uuid4())
    fluid_name = "Water"
    fluid_temperature = 45
    fluid_pressure = 101.325
    fluid = Fluid(
        fluid_id=fluid_id,
        fluid_name="Water",
        fluid_temperature=45,
        fluid_pressure=101.325,
    )

    assert fluid.fluid_id == fluid_id


def test_fluid_without_fluid_id():
    fluid_name = "Water"
    fluid_temperature = 45
    fluid_pressure = 101.325
    fluid = Fluid(
        fluid_name="Water",
        fluid_temperature=45,
        fluid_pressure=101.325,
    )

    assert uuid.UUID(fluid.fluid_id)
