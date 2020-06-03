# myems-cleaning
MyEMS Cleaning Service 

MyEMS 数据清洗服务


### Introduction

This service is a component of MyEMS and it cleans the historical data. 



### Prerequisites

mysql.connector


### Installation
    
Download and install MySQL Connector:
```
    $ cd ~/tools
    $ wget https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-8.0.20.tar.gz
    $ tar xzf mysql-connector-python-8.0.20.tar.gz
    $ cd ~/tools/mysql-connector-python-8.0.20
    $ sudo python3 setup.py install
```

Install myems-cleaning service
```bash
    $ cd ~
    $ git clone https://github.com/myems/myesm-cleaning.git
    $ sudo cp -R ~/myems-cleaning /myems-cleaning
    $ cd /myems-cleaning
    $ sudo git checkout master (or the release tag)
```
Open config file and edit database configuration
```bash
    $ sudo nano config.py
```
Setup systemd service:
```bash
    $ sudo cp myems-cleaning.service /lib/systemd/system/
```
Enable the service:
```bash
    $ sudo systemctl enable myems-cleaning.service
```
Start the service:
```bash
    $ sudo systemctl start myems-cleaning.service
```

### References

1. https://myems.io
2. https://dev.mysql.com/doc/connector-python/en/