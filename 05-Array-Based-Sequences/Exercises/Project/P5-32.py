def add_threed(dataset1, dataset2):
    """Add two three dimensional datasets componentwise"""
    if len(dataset1) != len(dataset2):
        raise ValueError('Dimensions must agree')
    resultant = []
    for i in range(len(dataset1)):
        if len(dataset1[i]) != len(dataset2[i]):
            raise ValueError('Dimensions must agree')
        outer = []
        for j in range(len(dataset1[i])):
            if len(dataset1[i][j]) != len(dataset2[i][j]):
                raise ValueError('Dimensions must agree')
            inner = []
            for k in range(len(dataset1[i][j])):
                inner.append(dataset1[i][j][k] + dataset2[i][j][k])
            outer.append(inner)
        resultant.append(outer)
    return resultant



# Testing
if __name__ == "__main__":
    print(add_threed([[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]],[[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]]))