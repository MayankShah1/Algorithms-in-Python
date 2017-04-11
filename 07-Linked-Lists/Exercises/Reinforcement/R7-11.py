import positional_list as PL

def max(positional_list):
    """Return the maximum"""
    max = positional_list.first().element()
    for item in positional_list:
        if item > max:
            max = item
    return max

# Testing
if __name__ == "__main__":
    pos_list = PL.PositionalList()
    pos_list.add_first(20)
    pos_list.add_first(30)
    pos_list.add_first(50)
    pos_list.add_first(40)
    pos_list.add_first(10)
    print(max(pos_list))