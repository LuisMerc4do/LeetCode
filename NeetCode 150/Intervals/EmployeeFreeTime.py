def employeeFreeTime(schedule):
    flattened = [i for employee in schedule for i in employee]
    intervals = sorted(flattened, key=lambda x: x[0])
    
    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(interval[1], merged[-1][1])
            
    free_times = []
    for i in range(1, len(merged)):
        start = merged[i-1][1]
        end = merged[i][0]
        free_times.append([start,end])
    
    return free_times