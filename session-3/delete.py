import subprocess


image = input("enter the images to be deleted: ")
subprocess.call("docker rmi %s"%image,shell=True)



