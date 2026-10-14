import os

from dotenv import load_dotenv

# Lit le fichier .env et charge ses valeurs
load_dotenv()

# --- Required values (from .env) ---
GCP_PROJECT_ID = os.environ["GCP_PROJECT_ID"]
GCP_BUCKET_NAME = os.environ["GCP_BUCKET_NAME"]
RAW_DATASET_URI = os.environ["RAW_DATASET_URI"]

# --- Optional values (with defaults) ---
GCP_REGION = os.getenv("GCP_REGION", "europe-west2") # Vertex AI region
GCS_LOCATION = os.getenv("GCS_LOCATION", "eu") # GCS bucket location
PIPELINE_ROOT = os.getenv("PIPELINE_ROOT", f"gs://{GCP_BUCKET_NAME}/pipeline_root")

# --- Aliases for backwards compatibility ---
PROJECT_ID = GCP_PROJECT_ID
BUCKET_NAME = GCP_BUCKET_NAME
REGION = GCP_REGION
