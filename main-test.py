# Import the Add function, and assert if it works correctly.
from main import Add

def TestAdd():
        assert Add(5,4) == 9
        print("Add Function works correctly")

if __name__ == '__main__':
        TestAdd()