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
    lines = []
    try:
        with open(path, "r") as f:
            l = f.readlines()
            for line in l: 
                lines.append(line.rstrip("\n"))
            f.close()
            return lines
    except IOError:
        print("Archivo no encontrado")
        time.sleep(2.4)
        exit()

def req(gnum,std,temas):
    if(gnum <= len(temas) and len(std) >= gnum):
        return True
    else:
        print("Parametro no valido")
        time.sleep(2.4)
        exit()

def distribucion(std, theme, n):
    
    std_div = div_numbers(std, n)
    std_rem = rem_numbers(std, n)
    theme_div = div_numbers(theme, n)
    theme_rem = rem_numbers(theme, n)

    cont = []
    #dividir temas 
    for i in range(n):
        temp = []
        for j in range(theme_div):
            choice = random.choice(theme)
            theme.remove(choice)
            temp.append(choice)
        cont.append([temp])
    
    #remanente temas 
    if theme_rem != 0:
        l = list(range(0, n))
        random.shuffle(l)
        for i in range(theme_rem):
            choice = random.choice(theme)
            theme.remove(choice)
            num = l.pop()
            cont[num][0].append(choice)
    
    #dividir std 
    for i in range(n):
        temp = []
        for j in range(std_div):
            choice = random.choice(std)
            std.remove(choice)
            temp.append(choice)
        cont[i].append(temp)
    
    #remanente temas 
    if std_rem != 0:
        l = list(range(0, n))
        random.shuffle(l)
        for i in range(std_rem):
            choice = random.choice(std)
            std.remove(choice)
            num = l.pop()
            cont[num][1].append(choice)
    
    return cont
    

if __name__ == '__main__':
    group_number = num_ask(sys.argv[1])
    std_path = sys.argv[2]
    themes_path = sys.argv[3]
    std_lits = read_file(std_path)
    themes_lits = read_file(std_path)

    if req(group_number, std_lits, themes_lits):
        grupos = distribucion(std_lits, themes_lits, group_number)
        for i in grupos:
            print("temas: " + ','.join(i[0]) + "---> estudiantes: " + ','.join(i[1]))