# objective
- By using **Typer** CLI-Application Build Tool to setup BuyBox Report API Automation 



# setup

For setup in Poetry, please refer [link](https://muthukamalan.github.io/posts/pythonenv/)
```sh
pip install requests typer 
```


# project structure
```sh
Walmart BuyBox Report API/
├── README.md
├── main.py
├── logfile
├── assets
├── reports
├── scripts
│   └── cleanup.sh
└── src
    ├── authenication.py
    ├── download_report.py
    ├── gen_report.py
    ├── __init__.py
    ├── status_check.py
    └── utils.py
```


# commands
- request 
```sh
python main.py request
```

- status
```sh
python main.py status
```

- download 
```sh
python main.py download
```
