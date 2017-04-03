import stackarray as Stack

def reverse_list(data):
    """Reverse the elements of list using stack"""

    S = Stack.ArrayStack()
    for i in range(len(data)):
        S.push(data[i])
    for i in range(len(data)):
        data[i] = S.pop()

# Testing
if __name__ == "__main__":
    data_set = [1,2,3,4,5,6,7]
    print(data_set)
    reverse_list(data_set)
    print(data_set)