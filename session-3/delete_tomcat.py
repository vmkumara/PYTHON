import subprocess


subprocess.call("docker rm -f $(docker container ls | grep tomcat | cut -d ' ' -f 1)",shell=True)


