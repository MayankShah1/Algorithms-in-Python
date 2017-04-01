def draw_line(tick_length, tick_label = ''):
    """Draw one line with given tick length(followed by optional label)"""
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    """Draw tick interval based upon a central tick length"""
    if center_length > 0:                   # Stop when length becomes 0
        draw_interval(center_length - 1)    # recursively draw top ticks
        draw_line(center_length)            # draw center tick
        draw_interval(center_length - 1)    # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches and major tick length"""
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)     # draw interior ticks for inch
        draw_line(major_length, str(j))

# Testing
draw_ruler(1, 4)
