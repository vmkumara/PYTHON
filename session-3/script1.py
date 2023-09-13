import subprocess


image = input("enter the images to be downloaded: ")
subprocess.call("docker pull %s"%image,shell=True)


