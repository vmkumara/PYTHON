import subprocess

image = input("enter the image name: ")
service = input("enter some name for the service: ")
ports = input("enter the port mapping: ")
replicas = int(input("enter the replicas count: "))

subprocess.call("docker service create --name %s -p %s --replicas %d %s"%(service,ports,replicas,image),shell=True)



