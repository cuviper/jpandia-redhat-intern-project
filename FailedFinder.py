
from copr.v3 import config_from_file
import copr.v3
import sys
import os
import subprocess

hashmap = {}

def unzipFile():

    print(file)
    filepath = cd + "/" + file
    print(filepath)
    os.chdir(filepath)
    unzipCommand = "gzip -d builder-live.log.gz"
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



#downloadBuild()

print("ayooo wtf")

files = os.listdir()
cd = os.getcwd()

weirdFailures = {}

for file in files:
    
    if "fedora" in file:
        unzipFile()
       
        
        
        with open("builder-live.log", "r") as file:

            
            for line in file:

                if "test" in line and "..." in line and "ok" in line:   
                    # print(line)
                    # print(line[0:len(line) -7])

                    hashmap[line[0:len(line) -7]] = 1
                    #print(line)
                    #print(line)




for file in files:
     print(file)
     if "fedora" in file:
          with open("builder-live.log", "r") as file:
                for line in file:
                    if "test" in line and "..." in line and "FAILED" in line:
                        # print(line)
                        # print(line[0:len(line) -11])
                        if hashmap.get(line[0:len(line) -11]) is None:
                            weirdFailures[line] = 1

                        # print(line) 


for key in weirdFailures.keys():
    print(key)            


