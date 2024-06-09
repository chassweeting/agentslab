SHELL := /bin/bash
export PYTHONPATH := .

serve:
	@echo "Running the FastAPI APIs"
	cd src && poetry run uvicorn backend.main:app --host 0.0.0.0 --reload && cd ..


test:
	@echo "Running tests"
	poetry run python -m pytest --cov=src/backend --cov-report=term-missing
