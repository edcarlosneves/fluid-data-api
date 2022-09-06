from decouple import config
from sqlalchemy import create_engine

from app.domain.fluid_repository import FluidRepository

POSTGRES_USER = config("POSTGRES_USER")
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD")
POSTGRES_DB = config("POSTGRES_DB")
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT")
DB_DIRVER = config("DB_DIRVER")


class PostgresFluidRepository(FluidRepository):
    def __init__(self):
        self.engine = create_engine(
            f"{DB_DIRVER}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}"
        )

    def _make_query(self, query_string):
        with self.engine.connect() as conn:
            fetch_query = conn.execute(query_string)
        return fetch_query

    def add(self, fluid):
        if self.get_fluid(fluid.fluid_id):
            raise Exception("Dupicated id")

        static_query = "INSERT INTO fluid_data(fluid_name, fluid_temperature, fluid_pressure, fluid_id) VALUES "
        dynamic_query = f"('{fluid.fluid_name}', {fluid.fluid_temperature}, {fluid.fluid_pressure}, '{fluid.fluid_id}');"
        query_string = static_query + dynamic_query
        self._make_query(query_string)

        return fluid

    def all(self):
        query_string = "SELECT * FROM fluid_data"
        fetch_query = self._make_query(query_string)

        return list(fetch_query)

    def get_fluid(self, fluid_id):
        query_string = f"SELECT * FROM fluid_data WHERE fluid_id='{fluid_id}'"
        fetch_query = self._make_query(query_string)
        return list(fetch_query)
