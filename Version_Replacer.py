import os
import sys
import subprocess

projectName = sys.argv[1]

#remove older files and download updated ones
if (os.path.exists("rustc-nightly-src.tar.xz")):
    os.remove("rustc-nightly-src.tar.xz")
specCommand = "spectool -g rust.spec"
result = subprocess.run(specCommand, shell = True, capture_output = True, text = True)
print(result.stdout)

#extract file from version folder
extractCommand = "tar xf rustc-nightly-src.tar.xz rustc-nightly-src/version"
result = subprocess.run(extractCommand, shell = True, capture_output = True, text = True)


#read file
with open("rustc-nightly-src/version", 'r') as file:
    version = file.read()

#parse "version" retrieved from file to suit rpm syntax
array = version.split()
substring = array[0]
substring2 = array[2][:-1]
version = substring + "~" + substring2
version = version.replace("-", "~")



#replace version from spec file with correct version
with open("rust.spec", "r") as file:
    specFile = file.readlines()
length = len(specFile)
i = 0
for line in specFile:
    if "Version: " in line:
        lineNum = i
        break
    i = i + 1

lineModified = "Version:        " + version + "\n"
specFile[lineNum] = lineModified
new_rust_spec_file = "".join(specFile)
with open("rust.spec", "w") as file:
    file.write(new_rust_spec_file)


#package specfile into srpm file
packagingCommand = "fedpkg srpm"
result = subprocess.run(packagingCommand, shell = True, capture_output = True, text = True)
array = result.stdout.split("/")

# #create project
# createCommand = "copr-cli create " + projectName + " --chroot fedora-38-i386 --chroot fedora-38-x86_64 --chroot fedora-38-aarch64 --chroot fedora-38-ppc64le --chroot fedora-38-s390x" 
# result = subprocess.run(createCommand, shell = True, capture_output = False, text = True)
# print(result.stdout)

#build project
srpmfile = array[-1]
buildCommand = "copr-cli build " + str(projectName) + " " + str(srpmfile)
result = subprocess.run(buildCommand, shell = True, capture_output = False, text = True)
print(result.stdout)


    
