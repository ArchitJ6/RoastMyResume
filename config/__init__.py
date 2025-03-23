from dotenv import load_dotenv
import boto3
import google.generativeai as genai
import os

# =======================
# Configuration Settings
# =======================

# Load environment variables from .env file
load_dotenv()

# Configure Google's Generative AI (Gemini) with API key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Configure AWS S3
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION'),
    verify=True,  # Enable SSL verification
    use_ssl=True,  # Use SSL/TLS for connections
    config=boto3.session.Config(
        signature_version='s3v4',
        retries={'max_attempts': 3},
    )
)
S3_BUCKET = os.getenv('S3_BUCKET_NAME')
S3_USERS_KEY = 'users/credentials.json'