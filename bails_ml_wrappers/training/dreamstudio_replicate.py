# https://replicate.com/blog/dreambooth-api
import os
import zipfile

import requests

zip_file_name = "data.zip"
base_headers = {"Authorization": f"Token {os.environ['REPLICATE_API_TOKEN']}"}

username = input("Replicate username: ")
model_name = input("Model name: ")
input_dir = input("Input directory: ")
class_prompt = input("Class prompt (for examole 'a photo of a person'): ")
instnace_prompt = input(
    "Instance prompt (for example 'a photo of bge person'): "
)

print("Zipping input dir")
data_zip = zipfile.ZipFile(zip_file_name, "w")
for dirname, subdirs, files in os.walk(input_dir):
    data_zip.write(dirname)
    for filename in files:
        data_zip.write(os.path.join(dirname, filename))
data_zip.close()

print("Get upload url")
get_url_res = upload_res = requests.post(
    "https://dreambooth-api-experimental.replicate.com/v1/upload/data.zip",
    headers=base_headers,
)
print(f"Status code: {get_url_res.status_code}")

print("Upload data")
upload_res = requests.put(
    get_url_res.json()["upload_url"],
    headers={"Content-Type": "application/zip"},
    data=open(zip_file_name, "rb"),
)
print(f"Status code: {upload_res.status_code}")

print("Kick off training job")
training_res = requests.post(
    "https://dreambooth-api-experimental.replicate.com/v1/trainings",
    headers={
        **base_headers,
        "Content-Type": "application/json",
    },
    json={
        "input": {
            "instance_prompt": instnace_prompt,
            "class_prompt": class_prompt,
            "instance_Data": upload_res.json()["serving_url"],
            "max_train_steps": 2000,
        },
        "model": f"{username}/{model_name}",
    },
)
print(f"Status code: {training_res.status_code}")
print(training_res.text)
