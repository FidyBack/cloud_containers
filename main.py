# A criação de seções, recursos e instâncias foi baseada na documentação oficial do boto3: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
import boto3
from scripts import juju_script, docker_script
from credentials import keys

# Definition of some important variables
main_region = "us-east-1"
ubuntu20_ami = "ami-09e67e426f25ce0d7"      # Ubuntu 20.04
inst_type = "t2.micro"
key_name = "instancesKey"
sec_group_id = "sg-0600eeadf42d0e6fd"       # WebServer

# Session 
main_session = boto3.session.Session(
    aws_access_key_id = keys.ACCESS_KEY,
    aws_secret_access_key = keys.SECRET_KEY,
    region_name = main_region
)

# Resource and instances inicialization
ec2 = main_session.resource('ec2')

print("Iniciando Instâncias...")

user_script = f'''#!/bin/bash
cd /home/ubuntu/
sudo apt update && sudo apt upgrade -y
sudo snap install juju --classic

cat << EOF > juju_script.txt
{juju_script.script}
EOF
chmod +x juju_script.txt

cat << EOF > docker_script.txt
{docker_script.script}
EOF
chmod +x docker_script.txt


'''

inst_cluster = ec2.create_instances(
    ImageId = ubuntu20_ami,
    InstanceType = inst_type,
    KeyName = key_name,
    MaxCount = 1,
    MinCount = 1,
    SecurityGroupIds = [sec_group_id],
    UserData = user_script,
    # Monitoring = ,
    TagSpecifications = [{
        "ResourceType" : "instance",
        "Tags" : [{"Key" : "Name", "Value" : "docker"}]
    }]
)

print(f"A instância com ID {inst_cluster[0].id} está sendo iniciada")