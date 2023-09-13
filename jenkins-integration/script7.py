import jenkins

j = jenkins.Jenkins("http://localhost:8080","admin","admin")

i = 1
while i <= 10:
    j.copy_job("sample%d"%i,"newsample%d"%i)
    i = i + 1

