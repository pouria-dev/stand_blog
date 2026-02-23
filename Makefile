# ===============================
# Stand Blog - Makefile
# ===============================

PROJECT_NAME=stand_blog
VENV=venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
MANAGE=$(PYTHON) manage.py

# Load .env file if exists
ifneq (,$(wildcard .env))
    include .env
    export
endif

.DEFAULT_GOAL := help

# -------------------------------
# Help
# -------------------------------
help:
	@echo "Available commands:"
	@echo " make venv        Create virtual environment"
	@echo " make install     Install dependencies"
	@echo " make migrate     Apply migrations"
	@echo " make makemigrate Create migrations"
	@echo " make run         Run development server"
	@echo " make superuser   Create superuser"
	@echo " make test        Run tests"
	@echo " make collect     Collect static files"
	@echo " make clean       Clean cache files"

# -------------------------------
# Environment Setup
# -------------------------------
venv:
	python3 -m venv $(VENV)

install:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# -------------------------------
# Django Commands
# -------------------------------
run:
	$(MANAGE) runserver

migrate:
	$(MANAGE) migrate

makemigrate:
	$(MANAGE) makemigrations

superuser:
	$(MANAGE) createsuperuser

test:
	$(MANAGE) test

collect:
	$(MANAGE) collectstatic --noinput

shell:
	$(MANAGE) shell

# -------------------------------
# Cleanup
# -------------------------------
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete