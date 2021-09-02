from Utils import *
from Heuristic import *
from EDF import *
from Plot import *
from GenerateTasks import *
import argparse
import random

#check if m and l are positive Integer
def positive_number(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue

#list of argument accepted
def get_parser(he):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("input")
    parser.add_argument("-h",choices=['ff', 'nf', 'bf','wf'], required=True)
    parser.add_argument("-s",choices=['du', 'iu'], required=True)
    parser.add_argument("-l",type=positive_number, required=True)
    parser.add_argument("-m",type=positive_number, required=True) 
    #Geanerate Tasks
    parser.add_argument("-g",type=positive_number)
    return parser

#the main function
def main(argv):
    #load tasks from the input file
    LstTasks=[]
    if argv.g:
        LstTasks=Generate_tasks(argv.g)
    else :
        try:
            #argv.input :input file name
            TaskFile = open(argv.input, 'r') 
            Lines = TaskFile.readlines() 
            #id of tasks
            id = 0
            # Strips the newline character 
            for line in Lines:
                LstTasks.append(Task(id,line.split(" ")[0],line.split(" ")[1],line.split(" ")[2],line.split(" ")[3]))
                id+=1
        except IOError:
            print("Error: Tasks File does not exists")
            exit(0)
    for t in LstTasks:
        t.show()


    #initialise system of tasks
    sys=System(LstTasks)
    #test the feasibility of the system

    if sys.get_utilisation() <= argv.m and sys.get_Umax() <=1:
        #initialise processors
        cores= []
        for i in range(0,argv.m):
            cores.append(Core(i))
        
        #check the Heuristic option
        partitioned_cores=[]
        if argv.h=="ff":
            partitioned_cores=First_fit(cores,sys.sort(argv.s))
        elif argv.h=="nf":
            partitioned_cores=Next_fit(cores,sys.sort(argv.s))
        elif argv.h=="bf":
            partitioned_cores=Best_fit(cores,sys.sort(argv.s))
        elif argv.h=="wf":
            partitioned_cores=Worst_fit(cores,sys.sort(argv.s))

        
        for c in partitioned_cores:
            if c.utilisation>0 :
                print("************** p %s *****************"%(c.id))
                # data=Scheduling(tasks,l) , Plot(data,core_id,L)
                Plot(Scheduling(System(c.tasks),argv.l),c.id,argv.l)  
                print("*************************************")  

    else :
        print("System none schedulable")

if (__name__=="__main__"):
    p = get_parser(he=True)
    args = p.parse_args()
    main(args)