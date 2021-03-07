from dotenv import load_dotenv
import os, sys
import logging

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logger = logging.getLogger("Snowball_GR")

SESSION_KEY="notsecretdevkey"
# SESSION_KEY = os.environ['SESSION_KEY']