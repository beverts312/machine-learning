---
title: Maxim
type: docs
description: |
    This tool can denoise, dehaze, deblur, derain, and enhance images.
    The tool being wrapped is google-research/maxim.
---

Docker tooling for [google-research/maxim](https://github.com/google-research/maxim).
Put input images in `../../volumes/working/input`.
Run `docker-compose run ml $OPERATION` where `$OPERATION` is one of: `Denoising`, `Deblurring`, `Dehazing-Indoor`, `Deshazing-Outdoor`, `Deraining-Streak`, `Deraining-Drop`, `Enhancement`.