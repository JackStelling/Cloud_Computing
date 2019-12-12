import numpy as np
import requests
import time

def load_poisson(URL,lam,k):

    i_r_t=np.random.poisson(lam, k)

    requests.get(URL)

    for x in i_r_t:
        time.sleep(x)
        requests.get(URL)
        #print(x)


URL = input("Enter URL e.g http://<AWScloud I.P>:8080/primecheck   ")
lam = float( input("Enter Lambda (rate) value   ") )
k = int ( input("Enter the number of times to call the URL   ") )

load_poisson(URL,lam,k)
