import docker

client=docker.from_env()

#client.images.pull('nclcloudcomputing/javabenchmarkapp')
client.containers.run("nclcloudcomputing/javabenchmarkapp", detach=True, ports={'192.168.99.100':8080})
