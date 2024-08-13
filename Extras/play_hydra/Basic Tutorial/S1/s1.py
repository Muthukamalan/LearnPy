'''
Like typer, hydra CLI app
key feature is the ability to dynamically create a hierarchical configuration by composition and override it through config files and the command line
'''
import hydra
from omegaconf import DictConfig, OmegaConf
from hydra.core.hydra_config import HydraConfig

@hydra.main(version_base=None)
def total_config(cfg:DictConfig)->None:
    '''
        hydra creates an empty cfg obj, fill with run time (by prepending `+`)
    '''
    print("*"*100)
    print(OmegaConf.to_yaml(cfg))
    print("*"*100)
    print(OmegaConf.to_container(cfg))
    print("*"*100)
    print(HydraConfig.get().runtime.output_dir)




if __name__ == "__main__":
    total_config()

    # cfg= OmegaConf.load("*****.yaml")
    # print(cfg)





'''
$ python s1.py +db.user=muthu +terminal.shell=sh  +version=1
********************************************************************************
| db:
|   user: muthu
| terminal:
|  shell: sh
| version: 1
********************************************************************************
| {'db': {'user': 'muthu'}, 'terminal': {'shell': 'sh'}, 'version': 1}
********************************************************************************
'''
