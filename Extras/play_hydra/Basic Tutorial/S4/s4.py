'''
Composition Example

alternate btw two database

├── conf
│   ├── config.yaml
│   ├── db
│   │   ├── mysql.yaml
│   │   └── postgresql.yaml
│   └── __init__.py
└── my_app.py
'''
import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="conf", config_name="config")
def my_app(cfg : DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    print(type(cfg),dir(cfg))
    print(type(cfg._content),cfg._content)

if __name__ == "__main__":
    my_app()


'''
reproduceabilty 
$ python s4.py --config-dir=outputs/2024-08-11/01-57-11/.hydra/ --config-name=config
'''

'''
python s4.py --multirun model.a=1,3 model.b=45,6723
'''



'''
python main.py db.user=muthu +db.pwd=admin@098
db:
  driver: mysql
  user: muthu
  pass: secret
  pwd: admin@098
'''


'''
main is powered by Hydra.

== Configuration groups ==
Compose your configuration from those groups (group=option)

db: mysql, postgresql


== Config ==
Override anything in the config (foo.bar=value)

db:
  driver: mysql
  user: muthu
  pass: 123
  url:
    dev: mysql.dev
    test: mysql.test
    prod: mysql.com


Powered by Hydra (https://hydra.cc)
Use --hydra-help to view Hydra specific help
'''