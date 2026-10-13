"""Smoke test for GCP setup: Vertex AI + Cloud Storage."""

import os
import sys

from dotenv import load_dotenv
from google.cloud import aiplatform, storage

# Load variables from .env into the environment
load_dotenv()

PROJECT_ID = os.getenv("GCP_PROJECT_ID")
REGION = os.getenv("GCP_REGION")
BUCKET_NAME = os.getenv("GCP_BUCKET_NAME")


def check_env_vars() -> None:
    """Ensure all required environment variables are present."""
    missing = [
        name
        for name, value in {
            "GCP_PROJECT_ID": PROJECT_ID,
            "GCP_REGION": REGION,
            "GCP_BUCKET_NAME": BUCKET_NAME,
        }.items()
        if not value
    ]
    if missing:
        print(f"❌ Missing environment variables: {', '.join(missing)}")
        print("   Did you copy .env.example to .env and fill it in?")
        sys.exit(1)
    print(f"✅ Environment variables loaded (project={PROJECT_ID}, region={REGION}).")


def check_vertex_ai() -> None:
    """Initialize a Vertex AI client for the given project and location."""
    try:
        aiplatform.init(project=PROJECT_ID, location=REGION)
        print(f"✅ Vertex AI initialized for project '{PROJECT_ID}' in '{REGION}'.")
    except Exception as exc:  # noqa: BLE001
        print(f"❌ Failed to initialize Vertex AI: {exc}")
        sys.exit(1)


def check_gcs_bucket() -> None:
    """Access the GCS bucket and list its contents."""
    try:
        client = storage.Client(project=PROJECT_ID)
        bucket = client.get_bucket(BUCKET_NAME)
        blobs = list(bucket.list_blobs(max_results=10))
        print(f"✅ Accessed GCS bucket '{BUCKET_NAME}'.")
        if blobs:
            print(f"   Found {len(blobs)} object(s) (showing up to 10):")
            for blob in blobs:
                print(f"     - {blob.name}")
        else:
            print("   Bucket is empty.")
    except Exception as exc:  # noqa: BLE001
        print(f"❌ Failed to access GCS bucket '{BUCKET_NAME}': {exc}")
        sys.exit(1)


def main() -> None:
    print("Running GCP setup smoke test...\n")
    check_env_vars()
    check_vertex_ai()
    check_gcs_bucket()
    print("\n🎉 All checks passed. Your GCP setup is ready!")


if __name__ == "__main__":
    main()