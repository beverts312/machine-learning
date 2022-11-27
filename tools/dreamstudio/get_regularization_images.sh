#!/bin/bash

dataset="person_ddim" #@param ["man_euler", "man_unsplash", "person_ddim", "woman_ddim", "blonde_woman"]
git clone https://github.com/djbielejeski/Stable-Diffusion-Regularization-Images-{dataset}.git

mkdir -p regularization_images/{dataset}
mv -v Stable-Diffusion-Regularization-Images-{dataset}/{dataset}/*.* regularization_images/{dataset}
rm -r Stable-Diffusion-Regularization-Images-{dataset}