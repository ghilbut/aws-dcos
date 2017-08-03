# Ubuntu 16.04 LTS

## Install python 2.7

```bash
$ sudo apt-get update
$ sudo apt-get install -y python2.7
$ sudo ln -s /usr/bin/python2.7 /usr/bin/python
```

## Install Ansible v2.3.1.0-1 for AWS

```bash
$ sudo apt-get install -y python-setuptools build-essential python-dev libffi-dev libssl-dev
$ cd /tmp
$ curl -OL https://github.com/ansible/ansible/archive/v2.3.1.0-1.tar.gz
$ tar -vxzf v2.3.1.0-1.tar.gz
$ cd ansible-2.3.1.0-1/
$ sudo python setup.py install
```

## Install boto 2.48.0

```bash
$ cd /tmp
$ curl -OL https://github.com/boto/boto/archive/2.48.0.tar.gz
$ tar -vxzf 2.48.0.tar.gz
$ cd boto-2.48.0/
$ sudo python setup.py install
```

## Install boto3 1.4.5

```bash
$ cd /tmp
$ curl -OL https://github.com/boto/boto3/archive/1.4.5.tar.gz
$ tar -vxzf 1.4.5.tar.gz
$ cd boto3-1.4.5/
$ sudo python setup.py install
```
