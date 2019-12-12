import numpy as np
import requests
import time

def snap_poisson(URL, lam, k):

    i_r_t=np.random.poisson(lam, k)
    tic=time.perf_counter()
    requests.get(URL)

    for x in i_r_t:
        time.sleep(x)
        requests.get(URL)
        print(x)
        toc=time.perf_counter()

        if (toc-tic >= 90):
            tic=time.perf_counter()
            JSON1_pois = requests.get("http://192.168.99.100:3000/api/v1.3/docker/jack_Tomcat.1")
            JSON2_pois = requests.get("http://192.168.99.100:3000/api/v1.3/docker/jack_Tomcat.2")

            data_pois1 = JSON1_pois.json()
            data_pois2 = JSON2_pois.json()
            print("working")
        else :
            short=1


    if (short==1):

        JSON1_pois = requests.get("http://192.168.99.100:3000/api/v1.3/docker/jack_Tomcat.1")
        JSON2_pois = requests.get("http://192.168.99.100:3000/api/v1.3/docker/jack_Tomcat.2")

        data_pois1 = JSON1_pois.json()
        data_pois2 = JSON2_pois.json()
        print("yay")

    return (data_pois1, data_pois2)

#def main()

#URL = input("Enter the localhost URL")
#lam = input("Enter Lambda (rate) value")
#k = input("Enter the number of times to call the URL")

#snap_poisson(URL,lamb,k) # Do we need quotations?
data = snap_poisson("http://192.168.99.100:8080/primecheck", 2.5, 10)
