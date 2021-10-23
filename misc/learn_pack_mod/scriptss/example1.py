print("Thanks for importing Example1 module.")

MY_EX1_STRING = 'Welcome to Example1 module!'


def yolo(x: int):
    print("You only LIve", x, "times.")


if __name__ == '__main__':  # This will only be True if this module is run directly
    yolo(10000)
