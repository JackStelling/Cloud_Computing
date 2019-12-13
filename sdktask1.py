import docker

client=docker.from_env()
IP=input("Enter IP address:  ")

client.containers.run("nclcloudcomputing/javabenchmarkapp", detach=True, ports={IP:8080} )
