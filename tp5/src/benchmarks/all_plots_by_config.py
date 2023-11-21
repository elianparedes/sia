import os

from src.Config import Config
from src.benchmarks.vae_latent_space_setup import vae_latent_space_setup
from src.benchmarks.denoising import denoising
from src.benchmarks.ae_true_error_setup import ae_true_error_setup
from src.benchmarks.ae_pixel_error_setup import ae_pixel_true_error_setup

PLOTS_MAP = {
    "vae_latent_space_setup": vae_latent_space_setup,
    "denoising": denoising,
    "ae_true_error_setup": ae_true_error_setup,
    "ae_pixel_true_error_setup": ae_pixel_true_error_setup
}

config = Config(os.path.join(os.pardir, "config.json"))
config_run = config.run
for plot in config_run:
    plot_f = PLOTS_MAP[plot]
    plot_f(config)
