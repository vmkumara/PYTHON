import subprocess

subprocess.call("docker network create --driver bridge intelliqit",shell=True)

subprocess.call("docker run --name mydb -d --network intelliqit -e MYSQL_ROOT_PASSWORD=intelliqit mysql:5",shell=True)

subprocess.call("docker run --name mywordpress -p 8888:80 --network intelliqit -d wordpress",shell=True)


