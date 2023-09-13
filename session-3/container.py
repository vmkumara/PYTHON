import subprocess

image = input("enter image name: ")
container = input("enter container name: ")
detach = input("do you want to run in detached mode (y/n): ")


if detach == 'y':
    subprocess.call("docker run --name %s -d %s"%(container,image),shell=True)
elif detach == 'n':
    subprocess.call("docker run --name %s %s"%(container,image),shell=True)
else:
    print("invalid option")


