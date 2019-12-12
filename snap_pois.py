import numpy as np
import requests
import time


def snap_poisson(URL, lam, k):


    i=0
    i_r_t=np.random.poisson(lam, k)
    tic=time.perf_counter()
    requests.get(URL)

    global data_Tom1
    global data_Tom2

    data_pois_Tom1=[None]*10
    data_pois_Tom2=[None]*10


    for x in i_r_t:
        time.sleep(x)
        requests.get(URL)
        toc=time.perf_counter()

        if (toc-tic >= 90):
            tic=time.perf_counter()
            i=i+1
            JSON3_pois = requests.get(cad_URL1)
            JSON4_pois = requests.get(cad_URL2)

            data_pois_Tom1[i] = JSON3_pois.json()
            data_pois_Tom2[i] = JSON4_pois.json()
            print("Load generator still working")
        else :
            short=1


    if (short==1):
        time.sleep(90.01-(toc-tic))
        i=i+1
        JSON1_pois = requests.get(cad_URL1)
        JSON2_pois = requests.get(cad_URL2)

        data_pois_Tom1[i] = JSON1_pois.json()
        data_pois_Tom2[i] = JSON2_pois.json()
        print("Load Generator Finished \nJSON data saved in variables data_Tom1 and data_Tom2")

    data_Tom1=list(filter(None, data_norm_Tom1))
    data_Tom2=list(filter(None, data_norm_Tom2))

IP = input("Enter Host IP Address  ")
lam = float(input("Enter the rate (lambda) at which to call the URL  "))
k = int(input("Enter the number of times to call the URL  "))

cad_URL1='http://192.168.99.100:3000/api/v1.3/docker/jack_Tomcat.1'
cad_URL1=cad_URL1[:7] +IP+ cad_URL1[21:]
cad_URL2='http://192.168.99.100:3000/api/v1.3/docker/jack_Tomcat.2'
cad_URL2=cad_URL2[:7] +IP+ cad_URL2[21:]

URL="http://192.168.99.100:8080/primecheck"
URL=URL[:7] +IP+ URL[21:]

snap_poisson(URL,lam,k-1)
