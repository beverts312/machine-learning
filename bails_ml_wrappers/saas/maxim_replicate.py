# https://replicate.com/google-research/maxim
from bails_ml_wrappers.saas.replicate_base import ReplicateBase


class MaximReplicate(ReplicateBase):
    def __init__(self):
        super().__init__(
            "google-research/maxim",
            "494ca4d578293b4b93945115601b6a38190519da18467556ca223d219c3af9f9",
        )

    def enhance(self, image_path, operation):
        """
        Runs maxim on an image and and downloads the result

        Args:
            image_path (str): path to image to enhance
            operation (str): operation to perform on image can be one of
                Denoising
                Deblurring (GoPro)
                Deblurring (REDS)
                Deblurring (RealBlur_R)
                Deblurring (RealBlur_J)
                Deraining (Rain streak)
                Deraining (Rain drop)
                Dehazing (Indoor)
                Dehazing (Outdoor)
                Enhancement (Low-light)
                Enhancement (Retouching)
        """
        operation_suffix = (
            operation.replace(" ", "_").replace("(", "").replace(")", "")
        )
        self.predict(
            image_path, {"model": f"Image {operation}"}, operation_suffix
        )
