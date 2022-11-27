---
title: Real Esrgan
type: docs
description: |
    This tool enhances images in a number of ways, the tool being wrapped is xinntao/Real-ESRGAN
---

Docker tooling for [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN). Upscales images and fixes faces (using gfpgan).

Options:
* `-s` - Scale factor (default: 4)
* `--face_enhance` - Enhance face using GFPGAN (default: False)
* `--fp32` - Use fp32 precision during inference. Default: fp16 (half precision).

[Run on Replicate](https://replicate.com/nightmareai/real-esrgan)