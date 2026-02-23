# ===============================
# Stand Blog - GNU Makefile
# ===============================

PROJECT_NAME = stand_blog
PYTHON = python3
MANAGE = $(PYTHON) manage.py
VENV = venv
PIP = $(VENV)/bin/pip
ACTIVATE = . $(VENV)/bin/activate

.DEFAULT_GOAL := help

# -------------------------------
# Help
# -------------------------------
help:
	@echo "Available commands:"
	@echo "  make venv        Create virtual environment"
	@echo "  make install     Install dependencies"
	@echo "  make migrate     Apply migrations"
	@echo "  make makemigrate Create new migrations"
	@echo "  make run         Run development server"
	@echo "  make superuser   Create superuser"
	@echo "  make test        Run tests"
	@echo "  make collect     Collect static files"
	@echo "  make clean       Remove __pycache__ and pyc files"

# -------------------------------
# Virtual Environment
# -------------------------------
venv:
	$(PYTHON) -m venv $(VENV)

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

# -------------------------------
# Cleaning
# -------------------------------
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete