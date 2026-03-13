from src.main import numMembers, generateGroupName, welcomeMessage

def test_numMembers():
    test_list = ["Osoba1", "Osoba2"]
    assert numMembers(test_list) == 2
    print("NumMember method passed")

def test_generateGroupName():
    test_list = ["Osoba1", "Osoba2"]
    assert generateGroupName(test_list) == "Osoba1_Osoba2"
    print("generateGroupName method passed")

def test_welcomeMessage():
    test_list = ["Osoba1", "Osoba2"]
    assert welcomeMessage(generateGroupName(test_list)) == "=== Welcome to our Osoba1_Osoba2 group! ==="
    print("welcomeMessage method passed")

if __name__ == "__main__":
    test_numMembers()
    test_generateGroupName()
    test_welcomeMessage()