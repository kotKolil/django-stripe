import os

#getting api keys
API_KEY = os.environ.get("API_KEY_STRIPE")
PUBLISH_KEY = os.environ.get("PUBLISH_KEY")

#getting database variables
w = os.environ.get("POSTGRES_HOST")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
