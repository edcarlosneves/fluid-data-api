SHELL := /bin/bash # Use bash syntax
ARG := $(word 2, $(MAKECMDGOALS) )


runserver:
	python main.py

lint:
	pylint .

style:
	isort .
	black .