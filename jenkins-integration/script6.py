import jenkins

j = jenkins.Jenkins("http://localhost:8080","admin","admin")

i = 1
while i <= 10:
    j.create_job("sample%d"%i,jenkins.EMPTY_CONFIG_XML)
    i = i + 1

