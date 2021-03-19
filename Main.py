#!/usr/bin/env python


def main():
    print("Hello world!")
    function1()
    function2()


def function1():
    print("function1 call succeeded")
    return


def removeDupe(inputList):
    inputList = list(set(inputList))
    return inputList


def function2():
    print("function2 call suceeded")
    return


def sortedEvens(inputList):
    return sorted([x for x in inputList if (x % 2) == 0])


def isLeapYear(year):
    return (year % 4 == 0) and ((year % 400 == 0) or (year % 100 > 0))


if __name__ == "__main__":
    main()
