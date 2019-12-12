import numpy as np
import requests
import time

def load_poisson(URL,lam,k):

    i_r_t=np.random.poisson(lam, k)

    requests.get(URL)

    for x in i_r_t:
        time.sleep(x)
        requests.get(URL)
        print(x)


IP = input("Enter the IP  ")
lam = float( input("Enter Lambda (rate) value   ") )
k = int ( input("Enter the number of times to call the URL   ") )

URL="http://192.168.99.100:8080/primecheck"
URL=URL[:7] +IP+ URL[21:]

load_poisson(URL,lam,k)
