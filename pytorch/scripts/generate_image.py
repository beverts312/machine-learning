from diffusers import StableDiffusionPipeline
import torch

checkpoint_name = "v1-5-pruned-emaonly.ckpt"


base_path = "/home/mluser/checkpoints"
pipe = StableDiffusionPipeline.from_pretrained(f"{base_path}/{checkpoint_name}", torch_dtype=torch.float16, revision="fp16")
pipe = pipe.to("cuda")

prompt = "a photo of an astronaut riding a horse on mars"
image = pipe(prompt).images[0]  
    
image.save("astronaut_rides_horse.png")