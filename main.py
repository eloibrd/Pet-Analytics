import os

import click
import uvicorn

from app.core.config import config


# Use click to read cmd line args
@click.command()
# Read env
@click.option(
    "--env",
    type=click.Choice(["local", "prod"], case_sensitive=False),
    default="local",
)
def main(env: str):
    """Application entry point.

    Runs a uvicorn web server starting the fastapi app.
    """

    # set ENV environment variable
    os.environ["ENV"] = env
    print(
        f"STARTUP: Running app in {env} mode. Debug enabled : {str(config.DEBUG)}. \n"
    )
    uvicorn.run(
        app="app.app:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=True if config.ENV != "production" else False,
        workers=1,
    )


if __name__ == "__main__":
    main()
