# This file searches text documents for a certain IPC line and returns the IPC
# All these file contain a line like this:
# "CPU 0 cumulative IPC: 0.294297 instructions: 30000001 cycles: 101937895"
# We want to get the IPC value from this line

import csv

# The below are 4 folders each of which contain 20 tracefiles containing the above line
folders = ["exec_modified0", "exec_pure0", "inc0", "non_inc0"]

# Each folder contains the following 20 files and we want to get the IPC from each of these files 
# ├── bc-3.trace.gz-bimodal-no-no-no-no-hawkeye-1core.txt
# ├── bc-3.trace.gz-bimodal-no-no-no-no-lru-1core.txt
# ├── bc-3.trace.gz-bimodal-no-no-no-no-random-1core.txt
# ├── bc-3.trace.gz-bimodal-no-no-no-no-rl-1core.txt
# ├── bc-3.trace.gz-bimodal-no-no-no-no-ship-1core.txt
# ├── bfs-3.trace.gz-bimodal-no-no-no-no-hawkeye-1core.txt
# ├── bfs-3.trace.gz-bimodal-no-no-no-no-lru-1core.txt
# ├── bfs-3.trace.gz-bimodal-no-no-no-no-random-1core.txt
# ├── bfs-3.trace.gz-bimodal-no-no-no-no-rl-1core.txt
# ├── bfs-3.trace.gz-bimodal-no-no-no-no-ship-1core.txt
# ├── pr-3.trace.gz-bimodal-no-no-no-no-hawkeye-1core.txt
# ├── pr-3.trace.gz-bimodal-no-no-no-no-lru-1core.txt
# ├── pr-3.trace.gz-bimodal-no-no-no-no-random-1core.txt
# ├── pr-3.trace.gz-bimodal-no-no-no-no-rl-1core.txt
# ├── pr-3.trace.gz-bimodal-no-no-no-no-ship-1core.txt
# ├── sssp-3.trace.gz-bimodal-no-no-no-no-hawkeye-1core.txt
# ├── sssp-3.trace.gz-bimodal-no-no-no-no-lru-1core.txt
# ├── sssp-3.trace.gz-bimodal-no-no-no-no-random-1core.txt
# ├── sssp-3.trace.gz-bimodal-no-no-no-no-rl-1core.txt
# └── sssp-3.trace.gz-bimodal-no-no-no-no-ship-1core.txt

traceTypes = ["bc", "bfs", "pr", "sssp"]
cacheTypes = ["hawkeye", "lru", "random", "rl", "ship"]

# This function takes in a file and returns the IPC value from the file
def getIPC(file):
    f = open(file, "r")
    for line in f:
        if "CPU 0 cumulative IPC:" in line:
            #print(line)
            return float(line.split(" ")[4])
        
if __name__ == "__main__":

    # A is a 3D array that stores the IPC values
    A = [[[0 for i in range(5)] for j in range(4)] for k in range(4)]

    i = 0
    # For each folder
    for folder in folders:
        
        j = 0
        # For each trace type
        for traceType in traceTypes:

            k = 0
            # For each cache type
            for cacheType in cacheTypes:
                # Get the IPC value from the file and print it
                A[i][j][k] = getIPC(folder + "/" + traceType + "-3.trace.gz-bimodal-no-no-no-no-" + cacheType + "-1core.txt")
                k+=1
            j+=1
        i+=1

    print("LL")
    # Store the IPC values in a csv file
    with open('IPC.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["exec_modified", "exec_pure", "inc", "non_inc"])
        for i in range(4):
            writer.writerow([traceTypes[i], A[0][i][0], A[1][i][0], A[2][i][0], A[3][i][0]])
            writer.writerow([traceTypes[i], A[0][i][1], A[1][i][1], A[2][i][1], A[3][i][1]])
            writer.writerow([traceTypes[i], A[0][i][2], A[1][i][2], A[2][i][2], A[3][i][2]])
            writer.writerow([traceTypes[i], A[0][i][3], A[1][i][3], A[2][i][3], A[3][i][3]])
            writer.writerow([traceTypes[i], A[0][i][4], A[1][i][4], A[2][i][4], A[3][i][4]])

            

    # Plot a joint bar graph of the IPC values
    # For each trace we show a cluster of 5 bars, each bar representing a cache type and 4 such clusters for each folder
    import matplotlib.pyplot as plt
    import numpy as np

    # For a given A[i] we create one plot
    # For a given A[i][~][k] we create one cluster of 4 bars; vary j within each i,k
    # The j's form the cluster of different cache hierarchies

    # We create a single plot with 5 clusters of 4 bars each
    fig, ax = plt.subplots()
    index = np.arange(4)
    bar_width = 0.15
    

    # We create 5 clusters of 4 bars each
    # Each cluster represents a cache 



    
        

    

        


