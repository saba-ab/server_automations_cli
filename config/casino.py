from dotenv import load_dotenv
import os
load_dotenv()

HOST = os.getenv("HOST")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
DIRECTORY = os.getenv("DIRECTORY")
