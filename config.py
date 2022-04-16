import os
from dotenv import load_dotenv


load_dotenv()

DATE_FORMAT = "YYYY-MM-DD"

URL = "https://api.pdst.fm/graph/analytics"

PUBLISHER_ID = os.getenv("PODSIGHTS_PUBLISHER_ID", None)

HEADERS = {
    "ID": os.getenv("PODSIGHTS_API_ID"),
    "SECRET": os.getenv("PODSIGHTS_API_KEY"),
}
