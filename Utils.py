#tasks class
class Task:
    def __init__(self,id,offset,WCET,deadline,period):
        self.id=id
        self.offset=int(offset)
        self.WCET=int(WCET)
        self.deadline=int(deadline)
        self.period=int(period)
        self.utilisation=self.WCET/self.period
    #print a task
    def show(self):
        print("%s %s %s %s" %(self.offset,self.WCET,self.deadline,self.period))

#jobs

class Job:
    def __init__(self,id,key,task_id,release,wcet,deadline):
        self.id=id
        self.key="T%sJ%s"%(task_id,id)
        self.task_id=task_id
        self.release=release
        self.wcet=wcet
        self.deadline=deadline
        self.start=release
        self.end=deadline
        self.active=False #job is active when it did miss the deadline and remaine >0
        self.pre=False
        self.remaine=wcet
#tasks system
class System:
    def __init__(self,tasks):
        self.tasks=tasks

    def get_task_by_id(self,id):
        for task in self.tasks:
            if task.id==id:
                return task
            else:
                pass
    #get the max utilisation of a task in this system
    def get_Umax(self):
        max_util_task=max(self.tasks, key=lambda Task:Task.utilisation) 
        return max_util_task.utilisation
    
    #get the total utilisation of those tasks
    def get_utilisation(self):
        utilisation=0
        for task in self.tasks:
            utilisation+=task.utilisation
        return utilisation
    
    #sort tasks by utilisation
    def sort(self,mode):
        if mode=="du":
            return sorted(self.tasks, key=lambda Task:Task.utilisation,reverse=True) 
        else:
             return sorted(self.tasks, key=lambda Task:Task.utilisation)

#cores class
class Core:
    def __init__(self,id):
        self.id=id
        self.tasks= []
        self.utilisation=0
    #add task to a core
    def add_task(self,task):
        self.tasks.append(task)
        self.utilisation+=task.utilisation