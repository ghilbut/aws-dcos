# A. Preflight

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

# B. Create Network Environments

## 1. Create VPC

```bash
$ ansible-playbook -i inventories/{role}/ vpc_create.yml
```

## 2. Create OpenVPN

### 2-1. Create EC2 Instance

```bash
$ ansible-playbook -i inventories/{role}/ -e zone={zone} openvpn_create.yml
```

### 2-2. Setup Docker Environment

```bash
$ ansible-playbook -i inventories/{role}/ -e zone={zone} openvpn_docker.yml
```

### 2-3. Install and Run OpenVPN

From: [How to install OpenVPN with docker (Korean)](https://rampart81.github.io/post/openvpn_aws/)

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

$ docker run -v $OVPN_DATA:/etc/openvpn -d -p 1194:1194/udp --cap-add=NET_ADMIN --name openvpn kylemanna/openvpn:2.4
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

### 2-4. Modify client configuration

**download OpenVPN client configuation**

```bash
$ scp -i files/{role}.pem ubuntu@{ec2_public_ip}:/home/ubuntu/{name}.ovpn ~/Downloads/{name}.ovpn
```

**download client for MacOS X**

https://tunnelblick.net/

**before connected**
```
$ netstat -nr -f inet
Routing tables

Internet:
Destination        Gateway            Flags        Refs      Use   Netif Expire
default            192.168.0.1        UGSc           21        5     en0
127                127.0.0.1          UCS             0        0     lo0
127.0.0.1          127.0.0.1          UH              3  5444443     lo0
169.254            link#5             UCS             0        0     en0
192.168.0          link#5             UCS             0        0     en0
192.168.0.1/32     link#5             UCS             1        0     en0
192.168.0.1        90:9f:33:4a:79:7e  UHLWIir        21     2627     en0   1163
192.168.0.111/32   link#5             UCS             1        0     en0
192.168.0.111      78:4f:43:60:7f:72  UHLWI           0        1     lo0
224.0.0/4          link#5             UmCS            2        0     en0
224.0.0.251        1:0:5e:0:0:fb      UHmLWI          0        0     en0
239.255.255.250    1:0:5e:7f:ff:fa    UHmLWI          0      372     en0
255.255.255.255/32 link#5             UCS             0        0     en0
```

**after connected**
```
$ netstat -nr -f inet
Routing tables

Internet:
Destination        Gateway            Flags        Refs      Use   Netif Expire
0/1                192.168.255.5      UGSc            8        0   utun3
default            192.168.0.1        UGSc            6        5     en0
10                 192.168.255.5      UGSc            0        0   utun3
13.125.122.244/32  192.168.0.1        UGSc            1        0     en0
127                127.0.0.1          UCS             0        0     lo0
127.0.0.1          127.0.0.1          UH              4  5444391     lo0
128.0/1            192.168.255.5      UGSc            7        0   utun3
169.254            link#5             UCS             0        0     en0
192.168.0          link#5             UCS             0        0     en0
192.168.0.1/32     link#5             UCS             1        0     en0
192.168.0.1        90:9f:33:4a:79:7e  UHLWIir         4     2623     en0   1174
192.168.0.111/32   link#5             UCS             1        0     en0
192.168.0.111      78:4f:43:60:7f:72  UHLWI           0        1     lo0
192.168.255.1/32   192.168.255.5      UGSc            0        0   utun3
192.168.255.5      192.168.255.6      UHr            19        6   utun3
224.0.0/4          link#5             UmCS            2        0     en0
224.0.0.251        1:0:5e:0:0:fb      UHmLWI          0        0     en0
239.255.255.250    1:0:5e:7f:ff:fa    UHmLWI          0      372     en0
255.255.255.255/32 link#5             UCS             0        0     en0
```

**change route option**

From: [How to change route rules](https://serverfault.com/questions/631037/how-to-route-only-specific-openvpn-traffic-through-a-openvpn-based-on-ip-filteri)

```bash
$ vi {name}.ovpn
...
#redirect-gateway def1
route 10.0.0.0 255.0.0.0
```

```
$ netstat -nr -f inet
Routing tables

Internet:
Destination        Gateway            Flags        Refs      Use   Netif Expire
default            192.168.21.1       UGSc           39        3     en0
10                 192.168.255.5      UGSc            1        0   utun3
127                127.0.0.1          UCS             0        0     lo0
127.0.0.1          127.0.0.1          UH              4  5464157     lo0
169.254            link#5             UCS             0        0     en0
192.168.21         link#5             UCS             1        0     en0
192.168.21.1/32    link#5             UCS             1        0     en0
192.168.21.1       0:9:f:9:0:d        UHLWIir        41       61     en0   1191
192.168.21.64/32   link#5             UCS             0        0     en0
192.168.21.255     ff:ff:ff:ff:ff:ff  UHLWbI          0        1     en0
192.168.255.1/32   192.168.255.5      UGSc            0        0   utun3
192.168.255.5      192.168.255.6      UH              3        0   utun3
224.0.0/4          link#5             UmCS            2        0     en0
224.0.0.251        1:0:5e:0:0:fb      UHmLWI          0        0     en0
239.255.255.250    1:0:5e:7f:ff:fa    UHmLWI          0       12     en0
255.255.255.255/32 link#5             UCS             0        0     en0
```

```bash
$ ssh -i files/{role}.pem ubuntu@{ec2_private_ip}
```

----

# C. Remove Network Environments

## 1. Remove OpenVPN

```bash
$ ansible-playbook -i inventories/{role}/ -e zone={zone} openvpn_remove.yml
```

## 2. Remove VPC

```bash
$ ansible-playbook -i inventories/{role}/ vpc_remove.yml
```
