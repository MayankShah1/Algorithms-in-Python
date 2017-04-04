import stackarray as Stack

def is_matched_html(raw):
    """Return True if all HTML tags are properly matched;False otherwise"""

    S = Stack.ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:                     # invalid tag
            return False
        tag = raw[j+1 : k]              # strip away the tag
        space = tag.find(' ')
        if space != -1:
            tag = tag[0: space]
        if not tag.startswith('/'):     # opening tag
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()

# Testing
if __name__ == "__main__":
    raw_html = open('/home/mayank/Desktop/Algorithms-in-Python/06-Stacks-Queues-Deques/Exercises/Creativity/sample.html')
    html_list = []
    for line in raw_html:
        html_list.append(line)
    html_str = ''.join(html_list)
    print(html_str)
    print(is_matched_html(html_str))