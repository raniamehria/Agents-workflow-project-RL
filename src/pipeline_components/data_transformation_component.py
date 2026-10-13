from kfp import dsl
from kfp.dsl import OutputPath


@dsl.component(
    base_image="python:3.11-slim",
    packages_to_install=["pandas", "gcsfs", "datasets"],
)
def data_transformation_component(
    raw_dataset_uri: str,
    train_dataset_path: OutputPath("Dataset"),
    test_dataset_path: OutputPath("Dataset"),
    test_size: float = 0.1,
    seed: int = 42,
):
    """Lit le dataset Yoda, le met en format conversation, le découpe et l'écrit."""
    import json
    import logging

    import pandas as pd
    from datasets import Dataset

    logging.basicConfig(level=logging.INFO, force=True)
    logger = logging.getLogger("data_transformation")

    def to_conversation(example: dict) -> dict:
        return {
            "messages": [
                {"role": "user", "content": example["sentence"]},
                {"role": "assistant", "content": example["translation_extra"]},
            ]
        }

    def save_dataset_as_csv(dataset: Dataset, path: str) -> None:
        rows = [json.dumps(conversation) for conversation in dataset["messages"]]
        pd.DataFrame({"messages": rows}).to_csv(path, index=False)

    logger.info("Loading raw dataset from %s", raw_dataset_uri)
    df = pd.read_csv(raw_dataset_uri)
    logger.info("Loaded %d rows with columns %s", len(df), list(df.columns))

    dataset = Dataset.from_pandas(df)
    dataset = dataset.map(to_conversation, remove_columns=dataset.column_names)
    logger.info("Formatted %d conversations", len(dataset))

    splits = dataset.train_test_split(test_size=test_size, seed=seed)
    train_dataset, test_dataset = splits["train"], splits["test"]
    logger.info("Split into %d train / %d test rows", len(train_dataset), len(test_dataset))

    save_dataset_as_csv(train_dataset, train_dataset_path)
    save_dataset_as_csv(test_dataset, test_dataset_path)
    logger.info("Saved train to %s and test to %s", train_dataset_path, test_dataset_path)


if __name__ == "__main__":
    from src.constants import RAW_DATASET_URI

    data_transformation_component.python_func(
        raw_dataset_uri=RAW_DATASET_URI,
        train_dataset_path="train_local.csv",
        test_dataset_path="test_local.csv",
    )