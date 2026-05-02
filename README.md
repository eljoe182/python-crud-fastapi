<div align="center">

# Python CRUD

![Python](https://img.shields.io/badge/python-3.12-blue?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green?style=flat-square)

**REST API built with FastAPI for product management (MySQL), AWS S3 bucket introspection, health checks, and structured logging.**

</div>

---

## Overview

This service exposes HTTP endpoints for CRUD operations on **products** persisted in **MySQL**, a lightweight **AWS S3** helper to list objects in a bucket, and a **health** probe for orchestration. It follows a **context-oriented layout** (products, AWS, health) with use cases, repositories, and dependency wiring via small injection modules. Request logging and basic metrics-style timing are applied through Starlette middleware.

> [!TIP]
> Copy `.env.sample` to `.env` at the project root and fill in database and AWS values before running locally or with Docker.

## Features

- **Product API** — Create, read, update, delete, and list products (Pydantic schemas, SQLAlchemy + PyMySQL).
- **AWS integration** — List files in an S3 bucket (boto3; credentials and region from environment).
- **Health check** — Simple `GET` endpoint for liveness.
- **Observability** — JSON-friendly logging and middleware that records request URL, method, headers, and processing time.
- **Container-ready** — `Dockerfile` and `docker-compose.yaml` for the app and MySQL 8.

## Prerequisites

- **Python 3.12**
- **Poetry** (recommended) or `pip` with `requirements.txt`
- **MySQL 8** (local or via Docker Compose)
- **AWS credentials** (for S3 list; use real keys or a compatible local stack as appropriate)

## Quick start (local)

1. **Install dependencies**

   ```bash
   poetry install
   ```

   Or with pip:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure environment**

   ```bash
   cp .env.sample .env
   # Edit .env: DB_* and AWS_* as needed
   ```

3. **Run the application**

   ```bash
   python -m app.server
   ```

   The server reads `PORT` from the environment (default in code is `3000` if unset). Align `.env` with the port you expect (e.g. `8000` to match Docker).

4. **OpenAPI docs**

   Once running, interactive docs are available at `/docs` (Swagger UI) and `/redoc`.

## Environment variables

| Variable | Purpose |
|----------|---------|
| `APP_NAME` | Application label (optional for your deployment metadata). |
| `PORT` | HTTP listen port. |
| `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_DATABASE` | MySQL connection. |
| `AWS_REGION`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` | AWS SDK authentication. |
| `AWS_BUCKET_NAME`, `AWS_URL_S3` | Default bucket context and S3 URL base (see `context/aws`). |

> [!NOTE]
> On startup, `app.server` initializes the database and creates the product table via the SQLAlchemy entity setup. Ensure MySQL is reachable before starting the app.

## API summary

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/health-check/` | Liveness response (`{"status": "ok"}`). |
| `GET` | `/product/get-all` | List products. |
| `POST` | `/product/store` | Create a product (body: name, description, price, is_active). |
| `GET` | `/product/get-by-id/{id}` | Fetch product by id. |
| `PUT` | `/product/update/{id}` | Partial update (optional fields in body). |
| `DELETE` | `/product/delete/{id}` | Delete product. |
| `GET` | `/aws/list-files/{bucket_name}` | List objects for the given bucket name. |

Prefix paths are mounted as defined in `app/server.py` (no global `/api/v1` prefix unless you add one).

## Docker

Build and run the stack (MySQL + app) from the repository root:

```bash
docker compose up --build
```

The application service is mapped to **port 8000** in `docker-compose.yaml`. Provide a `.env` file compatible with the variables listed above so the app and MySQL service receive `DB_PASSWORD`, `DB_DATABASE`, etc.

## Testing

Tests use **pytest** with paths configured in `pyproject.toml`:

```bash
pytest
```

Unit tests cover product use cases and repository behavior (including AWS-related tests where mocks such as **moto** are used).

## Project layout (high level)

```text
app/                    # FastAPI app, server entry, environment loading
context/
  products/             # Product domain, application use cases, infrastructure
  aws/                  # AWS list-files flow
  health/               # Health route
shared/                 # Middleware, persistence (MySQL, AWS client), shared models
tests/                  # pytest unit tests
```

---

<p align="center">
  Built with <a href="https://fastapi.tiangolo.com/">FastAPI</a> and <a href="https://www.sqlalchemy.org/">SQLAlchemy</a>.
</p>
