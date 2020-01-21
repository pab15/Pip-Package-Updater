import os

file_name = "package-list.txt"

def writePackageList():
    print("Writing Outdated Package List...")
    command = "pip list --outdated > " + file_name
    os.system(command)

def reformatPackageList():
    print("Reformatting Outdated Package List...")
    with open(file_name) as file:
        unformatted_packages = [package.rstrip() for package in file]
    new_file = open(file_name, "w")
    for package in unformatted_packages:
        sep = r'('
        formatted_package = package.split(sep, 1)[0]
        new_file.write(formatted_package + "\n")
    new_file.close()
    file.close()

def updatePackages():
    file_count = 0
    print("Updating Outdated Packages...")
    with open(file_name) as file:
        package_list = [package.rstrip() for package in file]
    for package in package_list:
        command = "pip install --upgrade " + package
        os.system(command)
        file_count = file_count + 1
    file.close()
    os.remove(file_name)
    print("\n" + "Success! " + str(file_count) + " packages updated.")


writePackageList()
reformatPackageList()
updatePackages()
