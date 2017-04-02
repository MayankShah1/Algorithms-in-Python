import stackarray as Stack

def reverse_file(filename):
    """Overwrite a a given file with its contents line-by-line reversed."""
    S = Stack.ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    # Now we overwrite the file
    output = open(filename,'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()


# Testing
if __name__ == "__main__":
    reverse_file('/home/mayank/Desktop/Algorithms-in-Python/06-Stacks-Queues-Deques/Stacks/sample.txt')