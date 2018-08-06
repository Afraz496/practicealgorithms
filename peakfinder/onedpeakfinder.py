#!usr/bin/env python
import numpy
import datetime

def find_peak_naive(Arr):
    i = 0
    peak_found = False
    while(not peak_found and i < len(Arr)):
        if Arr[i] <= Arr[i+1] and i is not len(Arr)-1:
            i += 1
        elif i == len(Arr)-1:
            break
        else:
            peak_found = True
    if peak_found:
        print("Found a Peak!")
    else:
        print("Didn't find a Peak!")

def find_peak_divide_and_conquer(Arr):
    i = len(Arr)/2
    peak_found = False
    while(not peak_found):
        if Arr[i] < Arr[i-1]: #Then go left
            i -= 1
        peak_found = True


def main():
    print("This program will solve the 1 dimensional peak finding problem and use timing features to gauge the time complexity of the 1 dimensional peak finding probelm")
    n = input("Please enter the size of your array: ")
    Arr = numpy.random.randint(n, size=n)

    start_time = datetime.datetime.now()
    find_peak_naive(Arr)
    end_time = datetime.datetime.now()
    naive_time = (end_time - start_time).total_seconds()

    start_time = datetime.datetime.now()
    find_peak_divide_and_conquer(Arr)
    end_time = datetime.datetime.now()
    divide_and_conquer_time = (end_time - start_time).total_seconds()

    print("Runtime Complexity Results")
    print("Naive: " + str(naive_time))
    print("Divide and Conquer: " + str(divide_and_conquer_time))

if __name__ == '__main__':
    main()
