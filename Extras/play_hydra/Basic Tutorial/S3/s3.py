from omegaconf import DictConfig, OmegaConf
import hydra

@hydra.main(version_base=None, config_path="config", config_name="config")
def my_app(cfg: DictConfig):
    assert cfg.node.loompa == 10          # attribute style access
    assert cfg["node"]["loompa"] == 10    # dictionary style access

    assert cfg.node.zippity == 10         # Value interpolation
    assert isinstance(cfg.node.zippity, int)  # Value interpolation type
    assert cfg.node.do == "oompa 10"      # string interpolation
    
    # cfg.node.waldo = 12345
    cfg.node.waldo                        # raises an exception should define before we run
    print(OmegaConf.to_yaml(cfg))

if __name__ == "__main__":
    my_app()