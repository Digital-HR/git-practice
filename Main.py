#!/usr/bin/env python


def main():
    print("Hello world!")
    function1()
    function2()


def function1():
    print("function1 call succeeded")
    return


def function2():
    print("function2 call suceeded")
    return


def isLeapYear(year):
    return year % 4 == 0


if __name__ == "__main__":
    main()
