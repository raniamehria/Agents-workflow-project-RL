import json

import pandas as pd
from datasets import Dataset


def load_data(gcs_path: str) -> pd.DataFrame:
    """Lit le fichier CSV depuis Google Cloud Storage."""
    df = pd.read_csv(gcs_path)
    return df


def to_conversation(example: dict) -> dict:
    """Transforme une ligne du fichier en mini-conversation user -> assistant."""
    return {
        "messages": [
            {"role": "user", "content": example["sentence"]},
            {"role": "assistant", "content": example["translation_extra"]},
        ]
    }


def format_dataset(df: pd.DataFrame) -> Dataset:
    """Convertit le tableau pandas en Dataset Hugging Face au format conversation."""
    dataset = Dataset.from_pandas(df)
    dataset = dataset.map(to_conversation, remove_columns=dataset.column_names)
    return dataset


def split_dataset(dataset: Dataset, test_size: float = 0.1, seed: int = 42):
    """Découpe le Dataset en deux : un paquet train et un paquet test."""
    splits = dataset.train_test_split(test_size=test_size, seed=seed)
    return splits["train"], splits["test"]


def save_dataset_as_csv(dataset: Dataset, path: str) -> None:
    """Écrit un Dataset en CSV, chaque conversation étant stockée en JSON."""
    rows = [json.dumps(conversation) for conversation in dataset["messages"]]
    pd.DataFrame({"messages": rows}).to_csv(path, index=False)


def save_datasets(train_dataset: Dataset, test_dataset: Dataset, train_path: str, test_path: str) -> None:
    """Écrit les deux paquets dans des fichiers CSV."""
    save_dataset_as_csv(train_dataset, train_path)
    save_dataset_as_csv(test_dataset, test_path)


if __name__ == "__main__":
    from src.constants import RAW_DATASET_URI

    df = load_data(RAW_DATASET_URI)
    dataset = format_dataset(df)
    train_dataset, test_dataset = split_dataset(dataset)
    print("Train :", len(train_dataset))
    print("Test :", len(test_dataset))
    save_datasets(train_dataset, test_dataset, "train_local.csv", "test_local.csv")