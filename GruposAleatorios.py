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

def read_file(path): 
    line = []
    try:
        with open(path, "r") as f:
            l = f.readline()
            for lines in l: 
                line.append(lines.rstrip("\n"))
        f.close()
        return line
    except IOError:
        print("Archivo no encontrado")
        time.sleep(2.4)
        exit()

        
        

if __name__ == "__main__":