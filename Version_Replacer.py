import os
import subprocess

#extract file from version folder
extractCommand = "tar xf rustc-nightly-src.tar.xz rustc-nightly-src/version"
result = subprocess.run(extractCommand, shell = True, capture_output = True, text = True)


#retreive file from folder
cd = os.getcwd()
file_path = cd + "/rustc-nightly-src/version"
with open(file_path, 'r') as file:
    version = file.read()

#parse "version" retrieved from file to suit rpm syntax
substring = version[0:14]
substring2 = version[26:-1]
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
with open("rust_spec_tester.txt", "w") as file:
    file.write(new_rust_spec_file)

#get rust sources
specCommand = "spectool -g rust.spec"
result = subprocess.run(specCommand, shell = True, capture_output = True, text = True)
print(result.stdout)

# # #create project
# createCommand = "copr-cli create --chroot fedora-38-i386 --chroot fedora-38-x86_64 test-project4"
# result = subprocess.run(createCommand, shell = True, capture_output = True, text = True)
# print(result.stdout)

#build project

print("Hellloo")
#buildCommand = "ls"
buildCommand = "copr-cli build test-project4 ./rust-1.70.0-1.fc39.src.rpm"
result = subprocess.run(buildCommand, shell = True, capture_output = False, text = True)
print(result.stdout)



