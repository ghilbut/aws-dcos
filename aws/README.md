# Pre-flight

```bash
$ mkdir -p inventories/{role}/files
$ tee inventories/{role}/files/aws.ini <<- 'EOF'
[credential]
access_key = {{ aws access key }}
secret_key = {{ aws access secret key }}
EOF
```

# Create/Remove Network Environments

## Create

```bash
$ ansible-playbook -i inventories/{role}/ vpc_create.yml
```

## Remove

```bash
$ ansible-playbook -i inventories/{role}/ vpc_remove.yml
```
