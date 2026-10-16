import sys
from pathlib import Path

from google.cloud import aiplatform
from kfp import compiler

# add src in import path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from constants import PIPELINE_ROOT, PROJECT_ID, RAW_DATASET_URI, REGION
from pipelines.model_training_pipeline import model_training_pipeline

def main() -> None:
	# compile the pipeline in yaml
	package_path = "pipeline.yaml"
	compiler.Compiler().compile(
		pipeline_func=model_training_pipeline,
		package_path=package_path,
	)
	print(f"Compiled pipeline to: {package_path}")

	# initialize Vertex AI
	aiplatform.init(project=PROJECT_ID, location=REGION)
	print(f"Initialized Vertex AI: project={PROJECT_ID}, region={REGION}")

	# Create a PipelineJob
	job = aiplatform.PipelineJob(
		display_name="lmr-yoda-phi3-transformation",
		template_path=package_path,
		pipeline_root=PIPELINE_ROOT,
		parameter_values={
			"raw_dataset_uri": RAW_DATASET_URI,
			"test_size": 0.2,
			"seed": 42,
		},
		enable_caching=True
	)

	# Submit in Vertex AI
	job.submit()
	print(f"Pipeline job submitted: {job.name}")

	# print console link
	print(f"Console: {job._dashboard_uri()}")

if __name__ == "__main__":
	main()