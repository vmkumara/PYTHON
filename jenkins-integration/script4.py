import jenkins

j = jenkins.Jenkins("http://localhost:8080","admin","admin")

j.copy_job("develop2","newdevelop2")

