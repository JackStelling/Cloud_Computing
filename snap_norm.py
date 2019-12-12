import numpy as np
import requests
import time


def snap_norm(URL, mean, sd, k):

    i=0
    i_r_t=abs(np.random.normal(mean,sd,k))
    # limitation becuase of negative times.
    tic=time.perf_counter()
    requests.get(URL)
    global data1
    global data2
    data_norm_Tom1=[None]*10
    data_norm_Tom2=[None]*10


    for x in i_r_t:
        time.sleep(x)
        requests.get(URL)
        toc=time.perf_counter()

        if (toc-tic >= 90):
            tic=time.perf_counter()
            i=i+1
            JSON3_norm = requests.get("http://192.168.99.100:3000/api/v1.3/docker/jack_Tomcat.1")
            JSON4_norm = requests.get("http://192.168.99.100:3000/api/v1.3/docker/jack_Tomcat.2")

            data_norm_Tom1[i] = JSON3_norm.json()
            data_norm_Tom2[i] = JSON4_norm.json()
            print("working")
        else :
            short=1


    if (short==1):
        time.sleep(90.01-(toc-tic))
        i=i+1
        JSON1_norm = requests.get("http://192.168.99.100:3000/api/v1.3/docker/jack_Tomcat.1")
        JSON2_norm = requests.get("http://192.168.99.100:3000/api/v1.3/docker/jack_Tomcat.2")

        data_norm_Tom1[i] = JSON1_norm.json()
        data_norm_Tom2[i] = JSON2_norm.json()
        print("yay")

    data1=list(filter(None, data_norm_Tom1))
    data2=list(filter(None, data_norm_Tom2))

m = float(input("Enter Mean  "))
s_d = float(input("Enter Standard Deviation  "))
n = int(input("Enter the number of times to call the URL  "))

snap_norm("http://192.168.99.100:8080/primecheck",m,s_d,n-1)
