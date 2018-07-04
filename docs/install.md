## 在测试环境下搭建 autoAdmin

### install on Centos 7

#### 安装python 3.6

##### 1 安装依赖

```bash
sudo yum -y install openssl-devel readline-devel 
```



##### 2 下载并安装python

```bash
wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz
tar -xzf Python-3.6.6.tgz 
cd Python-3.6.6
./configure --prefix=/usr/local/python36
sudo make
sudo make install
```



##### 3 配置pip

```bash
sudo tee /etc/pip.conf <<EOF
[global]
index-url = http://pypi.douban.com/simple
trusted-host = pypi.douban.com
[list]
format=columns
EOF
```



##### 4 安装与初始化virtualenv

```bash
sudo /usr/local/python36/bin/pip3 install virtualenv
/usr/local/python36/bin/virtualenv ~/python36env
```



#### 安装数据库

##### 安装mariadb

```bash
sudo yum -y install mariadb mariadb-server mariadb-devel
```



##### 配置mariadb

修改/etc/my.cnf，在[mysqld]下面增加如下几行配置

```ini
[mysqld]
default-storage-engine = innodb
innodb_file_per_table           
collation-server = utf8_general_ci
init-connect = 'SET NAMES utf8'
character-set-server = utf8
```



##### 起动服务

```bash
sudo systemctl start mariadb
sudo systemctl enable mariadb
```



##### 初始化mariadb

这里设置root密码为 123456

```bash
mysql_secure_installation
```



##### 创建autoAdmin数据库

```bash
mysql -uroot -p123456 -e "create database devops CHARACTER SET utf8;"
```





#### 部署 autoAdmin

##### 下载源码

```bash
cd ~
git clone https://github.com/rfjer/autoAdmin.git
```



##### 安装依赖包

```
cd autoAdmin/
pip install -r requirements.txt 
```



##### 修改配置文件

配置文件路径在 autoAdmin/ops/settings.py 



配置mysql

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "devops",
        'USER': 'root',
        'PASSWORD': "123456",
        'HOST': "127.0.0.1",
        'PORT': "3306",
        'OPTIONS': {
            'init_command': "SET storage_engine=INNODB;SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```



##### 同步autoAdmin表结果

在操作之前需要在autoAdmin目录下创建一个logs的目录用于存放日志

```
mkdir logs
```



先生成user的迁移文件，然后同步

```bash
source ~/python36env/bin/activate
python manage.py makemigrations users
python manage.py migrate
```



接下来同步其它app的表结构

```python
python manage.py makemigrations cabinet idcs manufacturers menu products servers 
python manage.py migrate idcs
python manage.py migrate cabinet
python manage.py migrate manufacturers
python manage.py migrate products
python manage.py migrate menu
python manage.py migrate servers
```


##### 创建管理员用户
```python
python manage.py createsuperuser --username admin --email admin@domain.com
```


##### 起动服务

```
python manage.py runserver 0.0.0.0:8000
```



接下来就可以访问啦： 

http://your-ip:8000/    api root

http://your-ip:8000/docs/   api 文档



