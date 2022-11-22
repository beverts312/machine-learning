# https://replicate.com/wonjongg/stylecarigan
from bails_ml_wrappers.saas.replicate_base import ReplicateBase


class StylecariganReplicate(ReplicateBase):
    def __init__(self):
        super().__init__(
            "wonjongg/stylecarigan",
            "9f3f7680a746791fb05c52523883403b3cfa663ad87371db24760f255a2a0247",
        )

    def generate_caricature(self, image_path, num_outputs=1):
        self.predict(
            image_path,
            {"num_samples": num_outputs},
            f"_caricature_{num_outputs}",
        )
