input_lines = []
while True:
    try:
        line = input()
        input_lines.append(line)
    except EOFError:
        input_lines.reverse()
        for line in input_lines:
            print(line)
        break