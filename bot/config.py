from dotenv import dotenv_values

config = dotenv_values(".env")
REDIS_HOST = config["REDIS_HOST"]
REDIS_PORT = config["REDIS_PORT"]
WEATHER_TOKEN = config["WEATHER_TOKEN"]


# import os
# REDIS_HOST = os.environ.get("REDIS_HOST")
# REDIS_PORT = os.environ.get("REDIS_PORT")
