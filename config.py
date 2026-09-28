import os
from dotenv import load_dotenv

load_dotenv()

EDUCATION_BOT_NAME = os.getenv("BOT_NAME", "EduBuddy")
