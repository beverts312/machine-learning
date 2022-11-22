# https://replicate.com/mchong6/jojogan
from bails_ml_wrappers.saas.replicate_base import ReplicateBase


class JojoganReplicate(ReplicateBase):
    def __init__(self):
        super().__init__(
            "mchong6/jojogan",
            "9a535b24c359049e4e7c44a976a6a54e3a1a348650084b23545fe7b55de95c2d",
        )

    def apply_style(self, image_path, style):
        """
        Runs jojogan on an image and downloads the result

        Args:
            image_path (str): path to input image
            style (str): style to apply to image can be one of:
                art
                arcane_multi
                arcane_jinx
                arcance_caitlyn
                sketch_multi
                jojo
                jojo_yasuho
                disney
        """
        self.predict(
            image_path, {"pretrained": style, "alpha": 1}, f"_jojogan_{style}", "input_face"
        )
