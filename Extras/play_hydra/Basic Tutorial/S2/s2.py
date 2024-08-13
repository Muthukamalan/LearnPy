'''
Like typer, hydra CLI app
key feature 
    - is the ability to dynamically create a hierarchical configuration by composition  
    - override it through config files and the command line
    
'''
import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="conf", config_name="db_config")
def my_app(cfg : DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    
    assert cfg.db.encode==cfg.db['pass'], "In yaml, you mentioned encode=${pass} condition failed"


if __name__ == "__main__":
    my_app()



'''
python s2.py db.user=muthu +db.pwd=admin@098
# override + add 
db:
  driver: mysql
  user: muthu
  pass: secret
  pwd: admin@098



python s2.py db.user=muthu,kamalan
python s2.py -m db.user=muthu,kamalan ++db.pass=nosecret
'''

# Use ++ to override a config value if it's already in the config, or add it otherwise
