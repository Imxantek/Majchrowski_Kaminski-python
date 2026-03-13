def numMembers(list):
    return len(list)
def welcomeMessage():
    print("=== Welcome to our project group! ===")
def formatInfo():
    welcomeMessage()
    groupName = "Majchrowski_Kaminski"
    print(f"Group Name: {groupName}")
    groupList = {"Majchrowski", "Kaminski"}
    print(f"Group List: {groupList}")
    print(f"Number of members: {numMembers(groupList)}")
    print("Program compiled without errors")
    print("=== End of program ===")
if __name__=="__main__":
    formatInfo()
