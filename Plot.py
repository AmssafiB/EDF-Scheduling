#!/usr/bin/python
# Importing the matplotlb.pyplot 
import matplotlib.pyplot as plt 
import random
import collections 

#random digits to random colors 
def randomDigits(digits):
    lower = 10**(digits-1)
    upper = 10**digits - 1
    return random.randint(lower, upper)

def Plot(data,core_id,l):
    # Declaring a figure "gnt" 
    fig, gnt = plt.subplots() 
    # Setting Y-axis limits 
    gnt.set_ylim(0, 7) 
    # Setting X-axis limits 
    gnt.set_xlim(0, l) 
    # Setting labels for x-axis and y-axis 
    gnt.set_xlabel('Time') 
    gnt.set_ylabel('Tasks') 

    # Setting ticks on y-axis and Labelling tickes of y-axis 
    yticks=[]
    yticklabels=[]
    i=0
    for key in data:
        #[1,2,3,4]
        yticks.append(len(data)-i)
        #[T3,T2,T1,T0]
        yticklabels.append('T'+str(key))
        i+=1

    gnt.set_yticks(yticks) 
    gnt.set_yticklabels(yticklabels) 

    # Setting graph attribute 
    gnt.grid(True) 
    
    # using defaultdict() 
    # to initialize multiple lists 
    mul_list_dict = collections.defaultdict(list) 
    i=0
    for key in data:
        for y in data[key]:
            #mul_list_dict['list1'] =((0,1),(1,1),(2,1),(3,1)) 1 is for the time    
            mul_list_dict['list'+str(key)].append((y,1))
        gnt.broken_barh(mul_list_dict['list'+str(key)], (len(data)-i, 1),facecolors ='#'+str(randomDigits(6))) 
        i+=1
    
    # Plot the schedule for a core i 

    plt.savefig('EDF'+str(core_id)+'.png')
