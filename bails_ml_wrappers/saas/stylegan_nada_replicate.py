# https://replicate.com/rinongal/stylegan-nada
from bails_ml_wrappers.saas.replicate_base import ReplicateBase


class StyleganNadaReplicate(ReplicateBase):
    def __init__(self):
        super().__init__(
            "rinongal/stylegan-nada",
            "6b2af4ac56fa2384f8f86fc7620943d5fc7689dcbb6183733743a215296d0e30",
        )

    def apply_style(self, image_path, style):
        """
        Runs stylegan-nada on an image and downloads the result

        Args:
            image_path (str): path to input image
            style (str): style to apply to image can be one of:
               base, mona_lisa, modigliani, cubism, elf,
               sketch_hq, thomas, thanos, simpson, witcher,
               edvard_munch, ukiyoe, botero, shrek, joker,
               pixar, zombie, werewolf, groot, ssj, rick_morty_cartoon,
               anime, white_walker, zuckerberg, disney_princess, all
        """
        self.predict(
            image_path, {"output_style": style}, f"_stylegan_nada_{style}", "input"
        )
