#!/usr/bin/env python3
# Created by: Lloyd Najac
# Created on: Oct 2022
# This program picks ask the user to enter an integer and
# display whether it is positive or negative.


def main():
    # ask user for an integer.
    integer = int(input("Enter integer:"))

    # display whether the number is positive or negative.
    if integer > 0:
        print("This number is positive!")
    if integer < 0:
        print("This number is negative!")
    if integer == 0:
        print("This number is zero!")


if __name__ == "__main__":
    main()
