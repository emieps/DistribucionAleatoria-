import pytest
import GruposAleatorios as gp


#Prueba de Division
@pytest.mark.parametrize(
    "lst, div, ex",
    [
        (["Lenore", "Candice", "Chanel", "Chet","Lorenzo"], 5, 1), 
        (["Lenore", "Candice", "Chanel", "Lorenzo"], 4, 1), 
        (["Lenore", "Candice", "Chanel", "Chet","Lorenzo","Juan","Maria","Jaime","Pedro","David","Jesus","Moises","Herodes"], 6, 2), 
        (["Lenore", "Candice", "Chanel", "Chet","Lorenzo","Juan","Maria","Jaime","Pedro","David","Jesus","Moises","Herodes"], 5, 2)
    ]
)
def test_div_numbers(lst, div, ex):
    assert gp.div_numbers(lst, div) == ex

#Prueba de Remanente
@pytest.mark.parametrize(
    "lst, rem, ex",
    [
        (["Lenore", "Candice", "Chanel", "Chet","Lorenzo"], 5, 0), 
        (["Lenore", "Candice", "Chanel", "Lorenzo"], 4, 0), 
        (["Lenore", "Candice", "Chanel", "Chet","Lorenzo","Juan","Maria","Jaime","Pedro","David","Jesus","Moises","Herodes"], 6,1), 
        (["Lenore", "Candice", "Chanel", "Chet","Lorenzo","Juan","Maria","Jaime","Pedro","David","Jesus","Moises","Herodes"], 5,3)
    ]
)
def test_rem_numbers(lst, rem, ex):
    assert gp.rem_numbers(lst, rem) == ex 

#Probar String
@pytest.mark.parametrize(
    "num, expect",
    [
        ("5", 5),
        ("6", 6),
        ("3000", 3000)
    ]
)

def test_num_ask(num, expect):
    assert gp.num_ask(num) == expect

#Probar requerimientos 
@pytest.mark.parametrize(
    "num, std_list, themes_list",
    [
        (5, ["Lenore", "Candice", "Chanel", "Chet","Lorenzo"], ["Sociales", "Naturales", "Matematicas", "Lengua Española", "Religion"]), 
         (13, ["Lenore", "Candice", "Chanel", "Chet","Lorenzo","Juan","Maria","Jaime","Pedro","David","Jesus","Moises","Herodes"], 
          ["Sociales", "Naturales", "Matematicas", "Lengua Española", "Religion", "Artes", "Informatica", "Civica", "Ingles", "Recreo", "Quimica", "Fisica", "Edu. Fisica"])
    ]
)
def test_req(num, std_list, themes_list):
    assert gp.req(num, std_list,themes_list) == True


#Probar lectura 
@pytest.mark.parametrize(
    "path, expect",
    [
        (r"C:\Users\Emily\Desktop\1.Tendencias\Prueba\std_1.txt", ["Lenore", "Candice", "Chanel", "Chet","Leroi"]), 
        (r"C:\Users\Emily\Desktop\1.Tendencias\Prueba\std_2.txt", ["Lenore", "Candice", "Chanel", "Chet", "Leroi", "Robbie", "Annalise", "Ashleigh", "Jaxx"])
    ]
)

def test_req(path, expect):
    assert gp.read_file(path)== expect