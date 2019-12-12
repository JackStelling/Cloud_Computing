import numpy as np
import requests
import time


def load_normal(URL, mean, sd, k):

    i_r_t=abs(np.random.normal(mean,sd,k))
    # limitation becuase of negative times.

    requests.get(URL)

    for x in i_r_t:
        time.sleep(x)
        requests.get(URL)
        #print(x)

IP = input("Enter the current IP Address  ")
m = float(input("Enter Mean  "))
s_d = float(input("Enter Standard Deviation  "))
n = int(input("Enter the number of times to call the URL  "))

URL="http://192.168.99.100:8080/primecheck"
URL=URL[:7] +IP+ URL[21:]

load_normal(URL,m,s_d,n)
