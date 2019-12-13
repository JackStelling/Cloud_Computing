import numpy as np
import requests
import time
from datetime import datetime as dt
import pandas as pd
import pymongo
from pymongo import MongoClient

def snap_normal(URL, mean, sd, k):


    i=0
    i_r_t=abs(np.random.normal(mean,sd,k))
    # limitation becuase of negative times.
    tic=time.perf_counter()
    requests.get(URL)

    global data_Tom1
    global data_Tom2
    global IP
    global m
    global s_d
    global n
    global df1
    global df2

    data_norm_Tom1=[None]*10
    data_norm_Tom2=[None]*10


    for x in i_r_t:
        time.sleep(x)
        requests.get(URL)
        toc=time.perf_counter()

        if (toc-tic >= 90):
            tic=time.perf_counter()
            i=i+1
            JSON3_norm = requests.get(cad_URL1)
            JSON4_norm = requests.get(cad_URL2)

            data_norm_Tom1[i] = JSON3_norm.json()
            data_norm_Tom2[i] = JSON4_norm.json()
            print("Load generator still working")
        else :
            short=1


    if (short==1):
        time.sleep(90.01-(toc-tic))
        i=i+1
        JSON1_norm = requests.get(cad_URL1)
        JSON2_norm = requests.get(cad_URL2)

        data_norm_Tom1[i] = JSON1_norm.json()
        data_norm_Tom2[i] = JSON2_norm.json()
        print("Load Generator Finished \nJSON data saved in variables data_Tom1 and data_Tom2")

    data_Tom1=list(filter(None, data_norm_Tom1))
    data_Tom2=list(filter(None, data_norm_Tom2))

IP = input("Enter Host IP Address  ")
m = float(input("Enter Mean  "))
s_d = float(input("Enter Standard Deviation  "))
n = int(input("Enter the number of times to call the URL  "))

cad_URL1='http://192.168.99.100:3000/api/v1.3/docker/jack_Tomcat.1'
cad_URL1=cad_URL1[:7] +IP+ cad_URL1[21:]
cad_URL2='http://192.168.99.100:3000/api/v1.3/docker/jack_Tomcat.2'
cad_URL2=cad_URL2[:7] +IP+ cad_URL2[21:]

URL="http://192.168.99.100:8080/primecheck"
URL=URL[:7] +IP+ URL[21:]

snap_normal(URL,m,s_d,n-1)


#Tomcat1
stats1=[None]*len(data_Tom1)
for i in range(0 , (len(data_Tom1))):
    stats1[i]=data_Tom1[i][list(data_Tom1[i].keys())[0]]['stats']

time_list=[None]*len(stats1)
for j in range(0, (len(stats1))):
    time_list[j] = [i['timestamp'] for i in stats1[j]]

# next get cpu data
cpu_total_list=[None]*len(stats1)
for j in range(0, len(stats1)):
    cpu_total_list[j] = [i['cpu']['usage']['total'] for i in stats1[j]]

cpu_user_list=[None]*len(stats1)
for j in range(0, len(stats1)):
    cpu_user_list[j] = [i['cpu']['usage']['user'] for i in stats1[j]]

#Now lets look at memory

memory_usage_list=[None]*len(stats1)
for j in range(0, len(stats1)):
    memory_usage_list[j] = [i['memory']['usage'] for i in stats1[j]]

memory_max_list=[None]*len(stats1)
for j in range(0, len(stats1)):
    memory_max_list[j] = [i['memory']['max_usage'] for i in stats1[j]]

# these steps are going to join our lists and preserve the order if
# we have multiple jsons.

mem_usage=[]
for i in range(0, len(stats1)):
    mem_usage+=memory_usage_list[i]

mem_max=[]
for i in range(0, len(stats1)):
    mem_max+=memory_max_list[i]

cpu_total=[]
for i in range(0, len(stats1)):
    cpu_total+=cpu_total_list[i]

cpu_user=[]
for i in range(0, len(stats1)):
    cpu_user+=cpu_user_list[i]

timestamp=[]
for i in range(0, len(stats1)):
    timestamp+=time_list[i]

converted = pd.to_datetime(timestamp)
TS1=converted.strftime("%H:%M:%S")

# making a column of the parameters
mean=[None]*len(timestamp)
stan_dev=[None]*len(timestamp)
num=[None]*len(timestamp)
for i in range(0, len(timestamp)):
    mean[i]=m
    stan_dev[i]=s_d
    num[i]=n


dict1 = {'Time Stamps': TS1,
         'CPU Total': cpu_total,
         'CPU User': cpu_user,
         'Memory Usage': mem_usage,
         'Memory Max': mem_max,
         'Mean': m,
         'Standard Deviation': s_d,
         "Number of URL calls" :n
        }

df1 = pd.DataFrame(dict1)

CPUdiff=df1['CPU User'].diff()
df1['CPU User Difference'] = CPUdiff
datadict1 = df1.set_index('Time Stamps').T.to_dict('df1')



#Tomcat2 -------
stats2=[None]*len(data_Tom2)
for i in range(0 , (len(data_Tom2))):
    stats2[i]=data_Tom2[i][list(data_Tom2[i].keys())[0]]['stats']

time_list=[None]*len(stats2)
for j in range(0, (len(stats2))):
    time_list[j] = [i['timestamp'] for i in stats2[j]]

# next get cpu data
cpu_total_list=[None]*len(stats2)
for j in range(0, len(stats2)):
    cpu_total_list[j] = [i['cpu']['usage']['total'] for i in stats2[j]]

cpu_user_list=[None]*len(stats2)
for j in range(0, len(stats2)):
    cpu_user_list[j] = [i['cpu']['usage']['user'] for i in stats2[j]]

#Now lets look at memory

memory_usage_list=[None]*len(stats2)
for j in range(0, len(stats2)):
    memory_usage_list[j] = [i['memory']['usage'] for i in stats2[j]]

memory_max_list=[None]*len(stats2)
for j in range(0, len(stats2)):
    memory_max_list[j] = [i['memory']['max_usage'] for i in stats2[j]]

# these steps are going to join our lists and preserve the order if
# we have multiple jsons.

mem_usage=[]
for i in range(0, len(stats2)):
    mem_usage+=memory_usage_list[i]

mem_max=[]
for i in range(0, len(stats2)):
    mem_max+=memory_max_list[i]

cpu_total=[]
for i in range(0, len(stats2)):
    cpu_total+=cpu_total_list[i]

cpu_user=[]
for i in range(0, len(stats2)):
    cpu_user+=cpu_user_list[i]

timestamp=[]
for i in range(0, len(stats2)):
    timestamp+=time_list[i]

converted2 = pd.to_datetime(timestamp)
TS2=converted.strftime("%H:%M:%S")

dict2 = {'Time Stamps': TS2, 'CPU Total': cpu_total, 'CPU User': cpu_user, 'Memory Usage': mem_usage, 'Memory Max': mem_max}
dict2 = {'Time Stamps': TS2,
         'CPU Total': cpu_total,
         'CPU User': cpu_user,
         'Memory Usage': mem_usage,
         'Memory Max': mem_max,
         'Mean': m,
         'Standard Deviation': s_d,
         "Number of URL calls" :n
        }

df2 = pd.DataFrame(dict2)

CPUdiff=df2['CPU User'].diff()
df2['CPU User Difference'] = CPUdiff
datadict2 = df2.set_index('Time Stamps').T.to_dict('df2')


# saving to csv ----------------
m=str(m)
s_d=str(s_d)
n=str(n)

file1 ='/Cloud_Computing/CSV/T1_mean_sd_k.csv'
file1=file1[:24] +m+ file1[28:29]+s_d+file1[31:32]+n+file1[33:]


file2 ='/Cloud_Computing/CSV/T2_mean_sd_k.csv'
file2=file2[:24] +m+ file2[28:29]+s_d+file2[31:32]+n+file2[33:]

df1.to_csv(file1, index=None, header=True)
df2.to_csv(file2, index=None, header=True)
