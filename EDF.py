from Utils import Job
#get the Earliest deadline job
def Earliest_deadline(jobs):
    active_jobs=[]
    for job in jobs:
        if job.active==True:
            active_jobs.append(job)
    if active_jobs:
        return min(active_jobs, key=lambda Job:Job.deadline) 
    else:
        pass

#EDF Scheduling
def Scheduling(sys,l):
    #list of jobs
    lstJobs=[]
    #final result that can we use to plot results
    data={}
    #initialise first job of every task
    for task in sys.tasks:
        data.setdefault(task.id, [])
        lstJobs.append(Job(1,"T%sJ%s"%(task.id,1),task.id,task.offset+(0)*task.period,task.WCET,task.offset+(0)*task.period+task.deadline))
   
    t=0
    while t<l:     
        for job in lstJobs:
            current_task=sys.get_task_by_id(job.task_id)
            #job release
            if t==job.release:
                print("%s %s Released  (deadline %s)" %(t,job.key,job.deadline))
                job.active=True
            #create new job
            if t==current_task.offset+(job.id-1)*current_task.period:
                lstJobs.append(Job(job.id+1,"T%sJ%s"%(job.task_id,job.id+1),current_task.id,current_task.offset+(job.id)*current_task.period,current_task.WCET,current_task.offset+(job.id)*current_task.period+current_task.deadline))
            #job deadline
            if t==(job.id-1)*current_task.period+current_task.offset + current_task.deadline :
                print("%s Deadline of T%sJ%s " %(t,job.task_id,job.id))
                job.active=False   
        #get earliest deadline job    
        earl_job=Earliest_deadline(lstJobs)
        if earl_job:
            #data to return for ploting
            data[earl_job.task_id].append(t)
            #time execution ramaine
            earl_job.remaine-=1
            #if earl_job.pre==True means that this job hase the preoprety in the last time
            if earl_job.pre:
                if earl_job.remaine==0:     
                    earl_job.end=t
                    print("%s %s %s"%(earl_job.start,earl_job.end,earl_job.key))
                    earl_job.active=False
                    earl_job.pre=False
            #give this job the preorety
            else:
                earl_job.pre=True
                earl_job.start=t
        t+=1
    return data