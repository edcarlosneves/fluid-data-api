CREATE TABLE fluid_data (
	fluid_name VARCHAR(255),
	fluid_temperature FLOAT,
	fluid_pressure FLOAT,
	fluid_id VARCHAR(36)
);

INSERT INTO fluid_data(fluid_name, fluid_temperature, fluid_pressure, fluid_id) VALUES ('Water', 23, 101000, 'aaa');