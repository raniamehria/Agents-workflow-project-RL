from kfp import dsl # kfp: KubeFlowPipeline, dsl: Domain-Specific Language

from pipeline_components.data_transformation_component import (
	data_transformation_component,
)

# phi-3: SML(Small Language Model) created by Microsoft
@dsl.pipeline(
	name="luli-rania-yoda-phi3-transformation",
	description="Pipeline that transforms the Yoda dataset for Phi-3 fine-tuning",
)
def model_training_pipeline(
	raw_dataset_uri: str = "gs://lmr-llmops/yoda_sentences.csv",
	test_size: float = 0.2,
	seed: int = 42,
) -> None:
	"""A simple pipeline containing a single data transformation component.
	Args:
		raw_dataset_uri: URI of the raw CSV on GCS.
		test_size: Fraction of the dataset to use as the test split.
		seed: Random seed for reproducibility.
	"""
	data_transformation_component(
		raw_dataset_uri=raw_dataset_uri,
		test_size=test_size,
		seed=seed,
	)

