.PHONY: install-dependencies start-app create-migration apply-migrations rollback-migration run-tests test-coverage docker-up docker-down run-precommit view-structure

# Install project dependencies using Poetry
install-dependencies:
	@poetry install --no-root

# Run the FastAPI application
start-app:
	@cd src && poetry run python main.py

# Create a new Alembic migration with a custom message
create-migration:
	@read -p "Enter migration message: " message; \
	poetry run alembic revision --autogenerate -m "$$message"

# Apply the latest database migrations
apply-migrations:
	@poetry run alembic upgrade head

# Rollback the last applied migration
rollback-migration:
	@poetry run alembic downgrade -1
	@echo "Consider manually removing the migration file if necessary."

# Run tests and show code coverage report
test-coverage:
	@poetry run pytest --cov=src --cov-report=html tests/

# Bring up Docker services using docker-compose
docker-up:
	@docker-compose up -d

# Take down Docker services using docker-compose
docker-down:
	@docker-compose down

# Run all pre-commit hooks on all files
run-precommit:
	@git add .
	@poetry run pre-commit run -a

# Display the project structure, excluding unnecessary files
view-structure:
	@tree -a -I ".venv|.git|.data|__pycache__|.mypy_cache|*.pyc|*.pyo|alembic|htmlcov|*.egg-info|*.egg|*.tox|*.pytest_cache|*.mypy"
