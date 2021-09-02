#first Fit algorithm
def First_fit(cores,tasks):
    for task in tasks:
        for core in cores:
            if core.utilisation+task.utilisation<=1:
                core.add_task(task)
                break
    return cores

#worst Fit algorithm
def Worst_fit(cores,tasks):
    for task in tasks:
        #worst Fit algorithm needs to sort cores utilisation so we can put the incoming task in the emptiest
        for core in sorted(cores, key=lambda core: core.utilisation):
            if core.utilisation+task.utilisation<=1:
                core.add_task(task)
                break
    return cores
#Best Fit algorithm
def Best_fit(cores,tasks):
    for task in tasks:
        #Best Fit algorithm needs to sort descending cores utilisation so we can put the incoming task in the fulliest
        for core in sorted(cores, key=lambda core: core.utilisation,reverse=True):
            if core.utilisation+task.utilisation<=1:
                core.add_task(task)
                break
    return cores
#Next Fit algorithm
#start from core 1 and check if core 0 still have space ,and so on
def Next_fit(cores,tasks):
   
    j=1
    for task in tasks:
            if  cores[j-1].utilisation+task.utilisation<=1:
                cores[j-1].add_task(task)
            else:
                cores[j].add_task(task)
                j+=1
            
    return cores