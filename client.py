import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

_ = load_dotenv(find_dotenv())

client = OpenAI(api_key=os.getenv("OPEN_AI_KEY_FOR_STUDIES"))

model = "gpt-4o-mini"
