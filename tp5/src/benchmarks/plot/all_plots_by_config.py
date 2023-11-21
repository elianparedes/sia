import os

from src.Config import Config
from src.benchmarks.vae_latent_space_setup import vae_latent_space_setup

config = Config(os.path.join(os.pardir, "config.json"))
vae_latent_space_setup(config)
