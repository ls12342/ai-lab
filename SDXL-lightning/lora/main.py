import torch
from diffusers import StableDiffusionXLPipeline, EulerDiscreteScheduler
from huggingface_hub import hf_hub_download

base = "stabilityai/stable-diffusion-xl-base-1.0"
repo = "ByteDance/SDXL-Lightning"
# Use the correct ckpt for your step setting!
ckpt = "sdxl_lightning_4step_lora.safetensors"

# Load model.
pipe = StableDiffusionXLPipeline.from_pretrained(
    base, torch_dtype=torch.float16, variant="fp16").to("cuda")
pipe.load_lora_weights(hf_hub_download(repo, ckpt))
pipe.fuse_lora()

# Ensure sampler uses "trailing" timesteps.
pipe.scheduler = EulerDiscreteScheduler.from_config(
    pipe.scheduler.config, timestep_spacing="trailing")

prompt = ""
# Ensure using the same inference steps as the loaded model and CFG set to 0.
pipe(prompt, num_inference_steps=4,
     guidance_scale=0).images[0].save(prompt + ".png")
