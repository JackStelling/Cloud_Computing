import numpy as np
import requests
import time
from datetime import datetime as dt
import pandas as pd
import pymongo
from pymongo import MongoClient



def snap_poisson(URL, rate, n):

    global data_Tom1
    global data_Tom2
    global IP
    global lam
    global k
    global df1
    global df2


    i=0
    i_r_t=np.random.poisson(lam, k)
    tic=time.perf_counter()
    requests.get(URL)

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

    data_Tom1=list(filter(None, data_pois_Tom1))
    data_Tom2=list(filter(None, data_pois_Tom2))

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
    cpu_total_list[j] = [i['cpu']['usage']['user'] for i in stats1[j]]

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
lamb=[None]*len(timestamp)
num=[None]*len(timestamp)
for i in range(0, len(timestamp)):
    lamb[i]=lam
    num[i]=k


dict1 = {'Time Stamps': TS1,
         'CPU Total': cpu_total,
         'CPU User': cpu_user,
         'Memory Usage': mem_usage,
         'Memory Max': mem_max,
         'Lambda': lamb,
         "Number of URL calls" :num
        }

df1 = pd.DataFrame(dict1)

CPUdiff=df1['CPU Total'].diff()
df1['CPU Total Difference'] = CPUdiff
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
    cpu_total_list[j] = [i['cpu']['usage']['user'] for i in stats2[j]]

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
         'Lambda': lamb,
         "Number of URL calls" :num
        }

df2 = pd.DataFrame(dict2)

CPUdiff=df2['CPU Total'].diff()
df2['CPU Total Difference'] = CPUdiff
datadict2 = df2.set_index('Time Stamps').T.to_dict('df2')


#Now to save in MongoDB
myclient = pymongo.MongoClient(IP,8081)
mydb=myclient["Tomcat_Data_Pois"]
mycol=mydb['Tomcat_Data1']
mycol.insert_one(datadict1)
mycol=mydb['Tomcat_Data2']
mycol.insert_one(datadict2)
