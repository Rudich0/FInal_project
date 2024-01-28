import sys 


def data():
    try:
        with open(sys.argv[1], "rt") as file:
            exit_times_list=[]
            entry_times_list=[]
            owner=[]
            ours=0
            theirs=0
            for time in file:
                if time.strip() == "END":
                    break
                data=time.strip().split(",")
                exit_times_list.append(int(data[2]))
                entry_times_list.append(int(data[1]))
                owner.append(data[0])
                if data[0]=="OURS":
                    ours += 1
                if data[0]=="THEIRS":
                    theirs += 1
        return exit_times_list,entry_times_list, ours, theirs,owner
    except FileNotFoundError:
        print(f"The file was not found.")

    
def time_management(entry,exit,owner):
    time_diff=[]
    stay_time=0
    for i in range(len(exit)):
        time_diff.append(exit[i]-entry[i])
    for i in range(len(time_diff)):
        if owner[i]=="OURS":
            stay_time+=time_diff[i]
    hours = stay_time//60
    min = stay_time%60
    return time_diff,hours,min

def longest_shortest_average_time(time_diff,owner):  
    our_times = []
    
    for i in range(len(time_diff)):
        if owner[i] == "OURS":
            our_times.append(time_diff[i])

    if not our_times:
        return None, None, None

    shortest = min(our_times)
    longest = max(our_times)
    total_time = sum(our_times)
    count = len(our_times)

    average = total_time / count
    average = int(round(average, 0))

    return longest, shortest, average

def output(ours,theirs,hour,min,longest,shortest,average):
    print(f"Cat visits:{ours}")
    print(f"Other cats: {theirs}")
    print(f"Total Time in House: {hour} hours {min} minutes\n")
    print(f"Longest visit: {longest} minutes")
    print(f"Shortest visit: {shortest} minutes")
    print(f"Average visit: {average} minutes")


exit_list,entry_list,ours,theirs,ownership=data()
time_diff,hours,mins = time_management(entry_list,exit_list,ownership)
longest,shortest,average =longest_shortest_average_time(time_diff,ownership)
output(ours,theirs,hours,mins,longest,shortest,average)