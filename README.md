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
```

# How to install DC/OS on AWS with Ansible

[go to wiki page](https://github.com/ghilbut/aws-dcos/wiki)
