from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "personal-agent")
ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")