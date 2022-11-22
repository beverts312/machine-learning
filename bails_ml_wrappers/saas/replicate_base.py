import replicate
import requests


class ReplicateBase:
    def __init__(self, model, model_version):
        self.model = replicate.models.get(model).versions.get(model_version)

    def predict(
        self,
        image_path,
        model_args,
        new_file_suffix="_replicate",
        input_key="image",
    ):
        output = self.model.predict(
            **{input_key: open(image_path, "rb")}, **model_args
        )
        res = requests.get(output, stream=True)
        image_ext = image_path.split(".")[-1]
        new_image_path = image_path.replace(
            f".{image_ext}", f"{new_file_suffix}.png"
        )
        with open(new_image_path, "wb") as f:
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
