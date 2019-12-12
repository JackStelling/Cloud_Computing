
from datetime import datetime as dt
import pandas

def wrangler(data_Tom1):

    #getting the stats out of the json data
    #Tomcat1
    stats1=[None]*len(data_Tom1)
    for i in range(0 , (len(data_Tom1))):
        stats1[i]=data_Tom1[i][list(data_Tom1[i].keys())[0]]['stats']

    time_list=[None]*len(stats1)
    for j in range(0, (len(stats1))):
        time_list[j] = [i['timestamp'] for i in stats1[j]]

    converted=[None]*len(time_list)
    TS=[None]*len(time_list)

    for j in range(0, len(time_list)):
        converted[j] = pd.to_datetime(time_list[j])
        TS[j]=converted[j].strftime("%H:%M:%S")

    # next get cpu data 
    cpu_total_list=[None]*len(stats1)
    for j in range(0, len(stats1)):
        cpu_total_list[j] = [i['cpu']['usage']['user'] for i in stats1[j]]

    cpu_user_list=[None]*len(stats1)
    for j in range(0, len(stats1)):
        cpu_user_list[j] = [i['cpu']['usage']['user'] for i in stats1[j]]

    #Now lets look at memory

    memory_total_list=[None]*len(stats1)
    for j in range(0, len(stats1)):
        memory_total_list[j] = [i['memory']['usage'] for i in stats1[j]]

    memory_max_list=[None]*len(stats1)
    for j in range(0, len(stats1)):
        memory_max_list[j] = [i['memory']['max_usage'] for i in stats1[j]]
