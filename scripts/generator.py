#
# make a folder of a set of strings
#
# run the command (./build_champsim.sh bimodal no no no no <> 1)
# replace <> with element from a set of strings 
# now run the command (./run_champsim.sh bimodal-no-no-no-<>-1core 30 30 <>)
# replace <> with the same set of strings
# replace other <> from another set of strings.
# save the results generated in results_30M and copy them in the folder with name from the first set of strings
# copy the cache file from a folder and replace with the existing cache file
#  
#

import os

folders = ["non_inc", "exec_modified", "exec_pure", "inc"]
files = ["cache.cc", "modifexc.cc", "exc.cc", "inc.cc"]

cache_policies = ["rl"]
traces = ["bc", "bfs", "pr", "sssp"]

for i in range(4):
    os.system("mkdir ../../" + folders[i])
    os.system("cp ../../{} ./src/cache.cc".format(files[i]))

    for cache_policy in cache_policies:
        os.system("./build_champsim.sh bimodal no no no no {} 1".format(cache_policy))
        print("Running for cache policy: {}".format(cache_policy))
        for trace in traces:
            print("Running for trace: {}".format(trace))
            os.system("./run_champsim.sh bimodal-no-no-no-no-{}-1core 30 30 {}-3.trace.gz".format(cache_policy, trace))
            os.system("cp ./results_30M/* ../../{}".format(folders[i]))
    
    os.system("rm -rf ./results_30M")



