import random   
import time
import sys

def div_numbers(lst, num):
    return len(lst) // num

def rem_numbers(lst, num):
    return len(lst) % num

def num_ask(n):
    try:
       group_number = int(n)
       return group_number
    except ValueError:
        print("No es un numero")
        time.sleep(2.4)
        exit()

if __name__ == "__main__":