import subprocess

subprocess.call("free -m | grep Mem | awk '{ print $3 }' > file1",shell=True)

mem = int(open("file1","r").read())
if mem > 250 and mem < 500:
    subprocess.call("docker service scale webserver=3",shell=True)
elif mem > 500 and mem < 750:
    subprocess.call("docker service scale webserver=6",shell=True)
else:
    subprocess.call("docker service scale webserver=9",shell=True)

