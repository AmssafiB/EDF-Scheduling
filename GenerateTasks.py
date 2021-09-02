import random
from Utils import Task
def Generate_tasks(n):
    Lst=[]
    for i in range(0,n):
        #in case if we want asynchronous system
        #offset=random.randint(0,300)
        offset=0
        period=random.randint(1,300)
        WCET=random.randint(1,period)
        #in case if we want constraint deadline
        #deadline=random.randint(WCET,period)
        deadline=period
        Lst.append(Task(i,offset,WCET,deadline,period))
    return Lst