import os

API_KEY = os.environ.get("API_KEY_STRIPE")
PUBLISH_KEY = os.environ.get("PUBLISH_KEY")

print(PUBLISH_KEY)