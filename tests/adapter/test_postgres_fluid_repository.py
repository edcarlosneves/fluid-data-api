from app.adapter.postgres_fluid_repository import PostgresFluidRepository
from app.domain import fluid
from app.domain.fluid import Fluid

water = Fluid(fluid_name="Water", fluid_temperature=45, fluid_pressure=101.325)
methane = Fluid(fluid_name="Methane", fluid_temperature=45, fluid_pressure=101.325)


def test_fluid_save():
    fluid_repository = PostgresFluidRepository()

    assert water.save(fluid_repository).fluid_id == water.fluid_id
    assert methane.save(fluid_repository).fluid_id == methane.fluid_id


def test_fluid_repository_all():
    fluid_repository = PostgresFluidRepository()

    water.save(fluid_repository)
    methane.save(fluid_repository)

    assert set(fluid_repository.all()) == {water, methane}


def test_fluid_repository_get_fluid():
    fluid_repository = PostgresFluidRepository()

    water.save(fluid_repository)
    methane.save(fluid_repository)

    assert fluid_repository.get_fluid(water.fluid_id) == water
    assert fluid_repository.get_fluid(methane.fluid_id) == methane
