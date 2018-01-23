# Pre-flight

```bash
$ mkdir -p inventories/{role}/files
$ tee inventories/{role}/files/aws.ini <<- 'EOF'
[credential]
access_key = {{ aws access key }}
secret_key = {{ aws access secret key }}
EOF
```

```bash
$ cp ~/Downloads/{role}.pem files/{role}.pem
```

# Create Network Environments

## Create VPC

```bash
$ ansible-playbook -i inventories/{role}/ vpc_create.yml
```

## Create OpenVPN

### Create EC2 Instance

```bash
$ ansible-playbook -i inventories/{role}/ -e zone={zone} openvpn_create.yml
```

### Setup Docker Environment

```bash
$ ansible-playbook -i inventories/{role}/ -e zone={zone} openvpn_docker.yml
```

### Install and Run OpenVPN

https://rampart81.github.io/post/openvpn_aws/

```bash
$ ssh -i files/{role}.pem ubuntu@{ec2_public_ip}
```

```bash
$ sudo vi /etc/environment
...
OVPN_DATA="/home/ubuntu/openvpn/"

$ source /etc/environment
$ echo $OVPN_DATA
```

```bash
$ docker run -v $OVPN_DATA:/etc/openvpn --rm kylemanna/openvpn:2.4 ovpn_genconfig -u udp://{hostname}
$ docker run -v $OVPN_DATA:/etc/openvpn --rm -it kylemanna/openvpn:2.4 ovpn_initpki
...
Enter PEM pass phrase: ********
Verifying - Enter PEM pass phrase: ********
...
Common Name (eg: your user, host, or server name) [Easy-RSA CA]: ↵
...
Enter pass phrase for /etc/openvpn/pki/private/ca.key: ********
...
Enter pass phrase for /etc/openvpn/pki/private/ca.key: ********

$ docker run -v $OVPN_DATA:/etc/openvpn -d -p 1194:1194/udp --cap-add=NET_ADMIN kylemanna/openvpn:2.4
```

```bash
$ docker run -v $OVPN_DATA:/etc/openvpn --rm -it kylemanna/openvpn:2.4 easyrsa build-client-full {name} nopass
...
Enter pass phrase for /etc/openvpn/pki/private/ca.key: ********

$ docker run -v $OVPN_DATA:/etc/openvpn --rm kylemanna/openvpn:2.4 ovpn_getclient {name} > {name}.ovpn
```

```bash
$ exit
```

```bash
$ scp -i files/platform.pem ubuntu@13.125.122.244:/home/ubuntu/{name}.ovpn ~/Downloads/{name}.ovpn
```

https://tunnelblick.net/

```bash
$ ssh -i files/{role}.pem ubuntu@{ec2_private_ip}
```

# Remove Network Environments

## Remove OpenVPN

```bash
$ ansible-playbook -i inventories/{role}/ -e zone={zone} openvpn_remove.yml
```

## Remove VPC

```bash
$ ansible-playbook -i inventories/{role}/ vpc_remove.yml
```
