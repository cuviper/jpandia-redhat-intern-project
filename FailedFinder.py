
from copr.v3 import config_from_file
import copr.v3
import sys
import os
import subprocess

hashmap = {}

def unzipFile():
    unzipCommand = "gzip -d " + str(file) + "/builder-live.log.gz"
    result = subprocess.run(unzipCommand, shell = True, capture_output = False, text = True)
    print(result.stdout)
        
def downloadBuild():

    username = sys.argv[1]
    projectName = sys.argv[2]
            
    config = config_from_file()
    package = copr.v3.proxies.package.PackageProxy(config)
    rj = package.get(username, projectName, "rust", False, True)
    buildID = rj["builds"]["latest_succeeded"]["id"]
    print("buildid: " + str(buildID))
    downloadCommand = "copr-cli download-build " + str(buildID)
    result = subprocess.run(downloadCommand, shell = True, capture_output = False, text = True)
    print(result.stdout)

downloadBuild()

#finds all test cases that passed and stores in a hashmap
files = os.listdir()
for file in files: 
    if "fedora" in file:
        unzipFile()
        filePath = str(file) + "/builder-live.log"
        with open(filePath, "r") as file:          
            for line in file:             
                if "test" in line and "..." in line and "ok" in line:   
                    hashmap[line[0:len(line) -7]] = 1

#finds all test cases that failed and cross references them with test cases that passed to determine abnormal failures 
# targetting architectures
for file in files:
     filename = file
     filePath = str(file) + "/builder-live.log"
     
     if "fedora" in file:
          with open(filePath, "r") as file:
                for line in file:
                    if "test" in line and "..." in line and "FAILED" in line:
                        if hashmap.get(line[0:len(line) -11]) is not None:
                            print(line + filename + "\n")
                        
                            




