import subprocess

subprocess.call('docker container ls | grep tomcat | cut -d " " -f 1 > file1',shell=True)

myfile = open("file1",'r')
cont_ids = myfile.readlines()

i = 0
while i < len(cont_ids):
    id = cont_ids[i]
    subprocess.call("docker rm -f %s"%id,shell=True)
    i = i + 2
