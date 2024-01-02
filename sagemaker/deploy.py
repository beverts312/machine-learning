from huggingface_hub import snapshot_download
from sagemaker import image_uris
from pathlib import Path
import os
from boto3 import client
import logging
import sys
import subprocess

from argparse import ArgumentParser

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

parser = ArgumentParser(description="Deploys Sagemaker app")
parser.add_argument("--bucket", default="bllama-models")
parser.add_argument("--load-model", action="store_true")
parser.add_argument("--model-name", default="TheBloke/Llama-2-7b-fp16")

args = parser.parse_args()

def load_model(model_name, bucket):
    local_model_path = Path(".")
    local_model_path.mkdir(exist_ok=True)
    allow_patterns = ["*.json", "*.txt", "*.model", "*.safetensors", "*.bin", "*.chk", "*.pth"]
    logging.info(f"Downloading model {model_name} to {local_model_path}")
    model_download_path = snapshot_download(
        repo_id=model_name, cache_dir=local_model_path, allow_patterns=allow_patterns
    )
    logging.info(f"Model downloaded to {model_download_path}")
    logging.info(f"Uploading model to s3://{bucket}/{model_name}/model/")
    s3_client = client("s3")
    for file in os.listdir(model_download_path):
        logging.info(f"Uploading {file}")
        s3_client.upload_file(
            Filename=os.path.join(model_download_path, file),
            Bucket=bucket,
            Key=f"{model_name}/{file}",
        )

def load_data_dir(model_name, bucket):
    logging.info("Packaging model")
    subprocess.run(["tar", "-czvf", "model.tar.gz", "llama-2-7b"])
    s3_client = client("s3")
    s3_client.upload_file(
        Filename="model.tar.gz",
        Bucket=bucket,
        Key=f"{model_name}/model.tar.gz",
    )
    subprocess.run(["rm", "model.tar.gz"])

if args.load_model:
    logging.info("Loading s3 with the model")
    load_model(args.model_name, args.bucket)
    load_data_dir(args.model_name, args.bucket)
else:
    logging.info("Skipping model upload")

logging.info("Build deployment parameters")
image_uri = image_uris.retrieve(framework="djl-deepspeed", region="us-east-1", version="0.23.0")
logging.info(f"Using image uri {image_uri}")

deployment_args = {
    "ImageUri": image_uri,
    "ModelBucket": args.bucket,
    "DataPath": f"{args.model_name}/model.tar.gz",
}
build_result = subprocess.run(["sam", "build"])
build_result.check_returncode()

params_string = " ".join([f"{k}={v}" for k, v in deployment_args.items()])
deploy_cmd = [
    "sam",
    "deploy",
    "--parameter-overrides",
    params_string,
]
deploy_result = subprocess.run(deploy_cmd)
deploy_result.check_returncode()