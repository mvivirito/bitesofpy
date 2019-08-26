VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check: 
       - if 'quit' was entered for color, print 'bye' and break. 
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    while True:
        enterColor = input("Please enter a color or quit: ")
        enterColor = enterColor.lower()
        status = "Not a valid color"

        if enterColor == "quit":
            status = "bye"
            break
        else:
            for color in VALID_COLORS:
                if color == enterColor:
                    status = color 
                    print(status)    
    
    print(status)

print_colors()

