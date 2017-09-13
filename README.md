# Common

## git with ssh key
```bash
$ tee ~/.ssh/config << EOF
Host github.com
     Hostname github.com
     IdentityFile ~/.ssh/github_rsa
     User git
EOF
$ chmod 600 ~/.ssh/config
```

## git-lfs (git large file storage)

### Install
```bash
$ cd /tmp
$ curl -OL https://github.com/git-lfs/git-lfs/releases/download/v2.2.1/git-lfs-linux-amd64-2.2.1.tar.gz
$ tar -vxzf git-lfs-linux-amd64-2.2.1.tar.gz
$ cd git-lfs-2.2.1
$ sudo ./install.sh
$ git lfs install
```

### Manage large file types
```bash
$ cd /project/dir
$ git lfs track "*.tar.bz"
$ git lfs track "*.tgz"
$ git lfs track "*.zip"
$ git add .gitattributes
```

# Ubuntu 16.04 LTS

## Install python 2.7

```bash
$ sudo apt-get update
$ sudo apt-get install -y python2.7
$ sudo ln -s /usr/bin/python2.7 /usr/bin/python
```

## Install Ansible v2.3.1.0-1

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
