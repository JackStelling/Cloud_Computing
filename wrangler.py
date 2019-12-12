from datetime import datetime as dt
import pandas

def wrangler(data_Tom1, data_Tom2):

    #getting the stats out of the json data

    global dict1
    global dict2


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
    TS=converted.strftime("%H:%M:%S")

    dict1 = {'Time Stamps': TS, 'CPU Total': cpu_total, 'CPU User': cpu_user, 'Memory Usage': mem_usage, 'Memory Max': mem_max}


    #Tomcat2
    stats2=[None]*len(data_Tom2)
    for i in range(0 , (len(data_Tom1))):
        stats1[i]=data_Tom2[i][list(data_Tom2[i].keys())[0]]['stats']

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

    converted = pd.to_datetime(timestamp)
    TS=converted.strftime("%H:%M:%S")

    dict2 = {'Time Stamps': TS, 'CPU Total': cpu_total, 'CPU User': cpu_user, 'Memory Usage': mem_usage, 'Memory Max': mem_max}
