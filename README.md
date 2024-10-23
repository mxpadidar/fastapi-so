# FastAPI Scaffold Project

## Overview

This project is a scaffold for building a FastAPI application with clean architecture. It includes features like user authentication, registration, and structured layers (entities, services, repositories, etc.) to ensure modularity and scalability.

## Features

- **FastAPI** for high-performance APIs
- **PostgreSQL** for the database
- **Poetry** for dependency management
- **SQLAlchemy** for database ORM
- **Alembic** for database migrations
- **Docker** for containerization
- **PyTest** for testing
- **Pre-commit** to enforce code standards

## Project Structure

```bash
├── alembic.ini                     # Alembic configuration for DB migrations
├── docker-compose.yaml             # Docker Compose setup for running the project
├── .env.example                    # Example environment variables
├── src/
│   ├── account/                    # Account-related logic (user, auth, etc.)
│   │   ├── entities/               # Database models/entities
│   │   ├── entrypoints/            # Routes and schemas
│   │   ├── handlers/               # Business logic handlers
│   │   ├── orm/                    # ORM (SQLAlchemy) tables and mappings
│   │   ├── repositories/           # Database interactions/repositories
│   │   └── services/               # Services for authentication, registration, etc.
│   ├── core/                       # Core functionality (DB, settings, logging, etc.)
│   └── main.py                     # Application entry point
├── tests/                          # Test suite for unit and integration tests
└── README.md                       # Project documentation
```

## Prerequisites

### **Python 3.13.0+**

To install Python 3.13.0 from source on Linux, follow these steps:

```bash
# Install the required build tools and dependencies
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev

# Download the Python 3.13.0 source code
wget https://www.python.org/ftp/python/3.13.0/Python-3.13.0.tgz

# Extract the tarball
tar -xvf Python-3.13.0.tgz

# Change to the extracted directory
cd Python-3.13.0

# Configure the build for optimizations
./configure --enable-optimizations

# Compile the source using all available CPU cores
make -j $(nproc)

# Install Python (without overwriting the system version)
sudo make altinstall
```

### **Poetry**

Poetry is used for dependency management. To install Poetry, run:

```bash
# Install using the official installer script
curl -sSL https://install.python-poetry.org | python3 --upgrade

# Add Poetry to your shell configuration file (e.g., .bashrc, .zshrc)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# Reload your shell or run:
source ~/.bashrc
```

## Generating Secrets

```python
# Generate a bcrypt password salt
import bcrypt

salt = bcrypt.gensalt()

# Generate an authentication secret
import secrets

auth_secret = secrets.token_urlsafe(32)
```

## Getting Started

This repository is set up as a **GitHub Template**, which means you can use it to easily generate your own project without copying any commit history or `.git` metadata.

### Using the Repository as a Template

1. **Click on "Use this template"**:
   - At the top of the repository page, click the green **"Use this template"** button.

2. **Create a New Repository**:
   - GitHub will prompt you to name your new repository. Enter a unique repository name and optionally a description.
   - Choose whether the new repository should be public or private.

3. **Clone Your New Repository**:
   - Once GitHub has created the new repository for you, clone it to your local machine:
     ```bash
     git clone git@github.com:your-username/your-new-repo.git
     cd your-new-repo
     ```

4. **Set Up the Project**:
   - Follow these steps to set up the project on your local machine:

   ```bash
   # Install libpq5 for PostgreSQL support with psycopg 3
   sudo apt install libpq5

   # Create a virtual environment and install dependencies using Poetry
   poetry env use python3.13
   poetry install --no-root

   # Rename the `.env.example` to `.env` and update the environment variables:
   mv .env.example .env

   # Run Docker Services
   docker compose up -d

   # Apply Database Migrations using Alembic
   poetry run alembic upgrade head

   # Start the FastAPI Application
   cd src
   poetry run python main.py
   ```

By following these steps, you’ll generate a clean, fully-functional FastAPI project and be ready to start developing immediately!
