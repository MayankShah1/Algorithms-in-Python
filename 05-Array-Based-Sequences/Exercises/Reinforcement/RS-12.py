def sum_elements(dataset):
    """Return the sum of all elements in the dataset(list of list)"""
    return sum([sum(i) for i in dataset])

# Testing
if __name__ == "__main__":
    print(sum_elements([[1,2,3],[4,5,6],[7,8,9]]))