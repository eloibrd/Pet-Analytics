from influxdb import InfluxDBClient

from app.core.config import config


def influx_client() -> InfluxDBClient:
    """Provides the influx db client for the current environment.

    Returns:
        InfluxDBClient: Influx client to use to make requests to database.
    """
    # TODO: add switch case for production to configure ssl and authentication
    return InfluxDBClient(host=config.INFLUX_HOST, port=config.INFLUX_PORT)
