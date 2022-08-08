import json
from typing import Optional
from datetime import datetime
import asyncio
import typer
import alembic.config
from alembic.config import Config
from alembic import command
from settings import (
    POSTGRESQL_HOST,
    POSTGRESQL_PORT,
    POSTGRESQL_USER,
    POSTGRESQL_PASSWORD,
    POSTGRESQL_DATABASE,
    REDIS_HOST,
    REDIS_PORT,
    REDIS_DB,
    CORS_ALLOWED_ORIGINS,
    JWT_PREFIX,
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)

app = typer.Typer()


@app.command()
def say_hello():
    """
    Say hello to
    """
    nama = typer.prompt("what's your name: ")
    print(f"hello {nama}")


@app.command()
def refresh_initial():
    """
    Drop All Migration -> Migrate Database -> initial-data
    """
    alembic_args = ["downgrade", "base"]
    alembic.config.main(argv=alembic_args)
    alembic_args = ["upgrade", "head"]
    alembic.config.main(argv=alembic_args)


@app.command()
def show_migration_sql():
    """
    show migration sql command
    """
    alembic_cfg = Config("./alembic.ini")
    # command.downgrade(config=alembic_cfg, revision='base', sql=True)
    command.upgrade(config=alembic_cfg, revision="head", sql=True)

@app.command()
def show_settings(only: Optional[str] = None):
    """
    show current settings configuration

    --only show only some configuration, example POSTGRESQL, REDIS, JWT
    """
    if only == None or only == "ENVIRONTMENT":
        typer.echo(f"Environtment: ")
    if only == None or only == "POSTGRESQL":
        typer.echo(f"==POSTGRESQL CONF==")
        typer.echo(f"POSTGRESQL_HOST: {POSTGRESQL_HOST}")
        typer.echo(f"POSTGRESQL_PORT: {POSTGRESQL_PORT}")
        typer.echo(f"POSTGRESQL_USER: {POSTGRESQL_USER}")
        typer.echo(f"POSTGRESQL_PASSWORD: {POSTGRESQL_PASSWORD}")
        typer.echo(f"POSTGRESQL_DATABASE: {POSTGRESQL_DATABASE}")
    if only == None or only == "REDIS":
        typer.echo(f"==REDIS CONF==")
        typer.echo(f"REDIS_HOST: {REDIS_HOST}")
        typer.echo(f"REDIS_PORT: {REDIS_PORT}")
        typer.echo(f"REDIS_DB: {REDIS_DB}")
    if only == None or only == "CORS":
        typer.echo(f"==CORS==")
        typer.echo(f"CORS_ALLOWED_ORIGINS: {CORS_ALLOWED_ORIGINS}")
    if only == None or only == "JWT":
        typer.echo(f"==JWT==")
        typer.echo(f"JWT_PREFIX: {JWT_PREFIX}")
        typer.echo(f"SECRET_KEY: {SECRET_KEY}")
        typer.echo(f"ALGORITHM: {ALGORITHM}")
        typer.echo(f"ACCESS_TOKEN_EXPIRE_MINUTES: {ACCESS_TOKEN_EXPIRE_MINUTES}")
    if only == None or only == "EXTERNAL_API":
        typer.echo(f"==EXTERNAL API==")

if __name__ == "__main__":
    app()
