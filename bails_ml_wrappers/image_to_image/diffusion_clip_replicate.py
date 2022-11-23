# https://replicate.com/gwang-kim/diffusionclip
from script_helpers.replicate_base import ReplicateBase


class DiffusionClipReplicate(ReplicateBase):
    def __init__(self):
        super().__init__(
            "gwang-kim/diffusionclip",
            "a64682eb3defe354c15ffdd1afb0790c7644d83e8439964d1249f24ac9e998ad",
        )

    def imagenet_apply(self, image_path, edit_type):
        """
        Runs diffusionclip on an image using imagenet and downloads the result

        Args:
            image_path (str): path to image to apply diffusionclip to
            edit_type (str): style to applu to image can be one of:
                Watercolor art
                Pointillism art
                Painting by Gogh
                Cubism art
        """
        self.diffusion_clip_apply(
            image_path, "ImageNet style transfer", edit_type
        )

    def human_face_apply(self, image_path, edit_type):
        """
        Runs diffusionclip on an image using human face manipulation and downloads the result

        Args:
            image_path (str): path to image to apply diffusionclip to
            edit_type (str): style to applu to image can be one of:
                Pixar
                Neanderthal
                Sketch
                Painting by Gogh
                Tanned
                With makeup
                Without makeup
                Female → Male
        """
        self.diffusion_clip_apply(
            image_path, "Human face manipulation", edit_type
        )

    def dog_face_apply(self, image_path, edit_type):
        """
        Runs diffusionclip on an image using dog face manipulation and downloads the result

        Args:
            image_path (str): path to image to apply diffusionclip to
            edit_type (str): style to applu to image can be one of:
                Bear
                Hamster
                Yorkshire Terrier
                Nicolas Cage
                Zombie
                Venom
                Painting by Gogh
        """
        self.diffusion_clip_apply(
            image_path, "Dog face manipulation", edit_type
        )

    def diffusion_clip_apply(self, image_path, manipulation_type, edit_type):
        new_file_suffix = (
            f"diffusionclip_{manipulation_type}_{edit_type}".lower().replace(
                " ", "_"
            )
        )
        self.predict(
            image_path,
            {
                "edit_type": f"{manipulation_type} - {edit_type}",
                "manipulation": manipulation_type,
                "degree_of_change": 1,
                "n_test_steps": 50,
            },
            new_file_suffix,
        )
