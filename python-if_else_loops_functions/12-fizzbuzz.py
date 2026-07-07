#!/usr/bin/env python3
"""FizzBuzz function - prints numbers 1-100 with Fizz/Buzz/FizzBuzz"""


def fizzbuzz():
    """Prints numbers from 1 to 100 with Fizz, Buzz, and FizzBuzz"""
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
