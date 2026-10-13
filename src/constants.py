import os

from dotenv import load_dotenv

# Lit le fichier .env et charge ses valeurs
load_dotenv()

GCP_PROJECT_ID = os.environ["GCP_PROJECT_ID"]
GCP_REGION = os.environ["GCP_REGION"]
GCP_BUCKET_NAME = os.environ["GCP_BUCKET_NAME"]

# Chemin complet du fichier Yoda dans le bucket
RAW_DATASET_URI = f"gs://{GCP_BUCKET_NAME}/yoda_sentences.csv"