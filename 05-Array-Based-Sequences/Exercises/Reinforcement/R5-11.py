def sum_elements(dataset):
    """Return the sum of all elements in the dataset(list of list)"""
    sum = 0
    for i in range(len(dataset)):
        for j in range(len(dataset[i])):
            sum += dataset[i][j]

    return sum

# Testing
if __name__ == "__main__":
    print(sum_elements([[1,2,3],[4,5,6],[7,8,9]]))