import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    gemini_api_key = os.getenv("gemini_api_key")
    
    
config_obj = Config()