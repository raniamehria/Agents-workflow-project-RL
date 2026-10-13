import os

from dotenv import load_dotenv

# Lit le fichier .env et charge ses valeurs
load_dotenv()

GCP_PROJECT_ID = os.environ["GCP_PROJECT_ID"]
GCP_REGION = os.environ["GCP_REGION"]
GCP_BUCKET_NAME = os.environ["GCP_BUCKET_NAME"]


load_dotenv()

PROJECT_ID = os.environ["GCP_PROJECT_ID"]
BUCKET_NAME = os.environ["GCP_BUCKET_NAME"]
RAW_DATA_GCS_URI = os.environ["RAW_DATA_GCS_URI"]

REGION = os.getenv("GCP_REGION", "europe-west2") # Vertex AI region
GCS_LOCATION = os.getenv("GCS_LOCATION", "eu") # GCS bucket location (multi-region ok)

# Chemin complet du fichier Yoda dans le bucket
RAW_DATASET_URI = f"gs://{GCP_BUCKET_NAME}/yoda_sentences.csv"
