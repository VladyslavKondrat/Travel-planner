FROM python:3.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Setting up Python and uv environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

WORKDIR /app

COPY pyproject.toml uv.lock ./

# Sync dependencies
RUN uv sync --frozen --no-install-project --no-dev

# Now copy the rest of the application code
COPY . .

RUN uv sync --frozen --no-dev

EXPOSE 8000

# Use `uv run` to launch in env
CMD ["uv", "run", "manage.py", "runserver", "0.0.0.0:8000"]