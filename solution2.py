import random

"""
Returns the number of mechanics needed to maintain the planes, considering
the possibility of unscheduled maintenance

Pre-conditions: 
- All times are between 0 and 24
- Start time is always before the end time

Parameters:
- a: an integer array representing planes and the their maintenance schedule

"""
def scheduling(a):
     
    if a is None or len(a) == 0:
        return 0   
    
    arr = [plane[:] for plane in a]
    arr.sort()
    end_times = []
    for airplane in arr:
        rand = int(random.gauss(0, 1)) # Account for unscheduled maintenance
        variable = max(-5, min(5, rand))
        if variable > 0:
            if variable + airplane[1] >= 24:
                airplane[1] = 24
            else:
                airplane[1] += variable

        for time in end_times:
            if time <= airplane[0]: # Check whether mechanic can fit plane in schedule
                end_times.remove(time)
                break
        end_times.append(airplane[1]) # Update/add new end time
    return len(end_times)

