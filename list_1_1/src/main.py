def numMembers(list):
    return len(list)

def welcomeMessage(groupName):
    return f"=== Welcome to our {groupName} group! ==="

def generateGroupName(names):
    return "_".join(names)

def formatInfo(surnames_list):

    groupName = generateGroupName(surnames_list)

    print(welcomeMessage(groupName))
    print(f"Group Name: {groupName}")
    
    print(f"Group List: {surnames_list}")
    print(f"Number of members: {numMembers(surnames_list)}")
    print("Program compiled without errors")
    print("=== End of program ===")

if __name__=="__main__":
    my_group = ["Majchrowski", "Kaminski"]
    formatInfo(my_group)
