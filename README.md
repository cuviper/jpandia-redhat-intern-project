Copr Builder And Automater

These scripts allow users to automatically create copr builds and search previous builds for abnormal test failures. Abnormal test 
failures are tests that failed on some architectures (processecers like s390x, aarch64 etc.) but passed on others.

In order to connect to the copr API, you must the API token in the ~/.config/copr directory. For clear instructions: https://copr.fedorainfracloud.org/api/

Version_Replacer.py requires the name that that the user wants to call the project. It automatically installs the latest nightly build of rust, corrects the rust version number, and creates a new build with the given chroots "fedora-38-i386, "fedora-38-x86_64". To input the project name, do so in the following format: "Version_Replacer.py <project_name>"

FailedFinder.py requires the username of the copr account and the project name of the build that the user wishes to analyze. The program automatically retrieves the build id of the latest successful build, downloads the logs, and searches for abnormal failures. To input username and project name, do so in the following format: "FailedFinder.py <username> <project_name>" on the command line"


Jai Pandia (2023)

This project is licensed under the MIT License - see the LICENSE.md file for details

Thanks to the Platform Tools team at Red Hat.



