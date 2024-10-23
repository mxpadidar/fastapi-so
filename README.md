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
