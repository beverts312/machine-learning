# https://replicate.com/nightmareai/real-esrgan
from script_helpers.replicate_base import ReplicateBase


class RealEsrganReplicate(ReplicateBase):
    def __init__(self):
        super().__init__(
            "nightmareai/real-esrgan",
            "42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b",
        )

    def enhance(self, image_path, scale=4, face_enhance=False):
        self.predict(
            image_path,
            {"scale": scale, "face_enhance": face_enhance},
            f"_ersgan_{scale}",
        )
