import sys
sys.path.append('{{cookiecutter.project_dir}}')

import hydra
from omegaconf import DictConfig


@hydra.main(config_path="../config", config_name="main", version_base=None)
def main(cfg: DictConfig):
    pass


if __name__ == "__main__":
    main()
