import pytest
import GruposAleatorios as gp

#Pruba de numero
@pytest.mark.parametrize(
    "num",
    [
        ("hola"),
        ("nkjrdhnkjfcnekj6"),
        ("30dft")
    ]
)

def test_num_ask_exit(num):
    with pytest.raises(SystemExit) as e:
        gp.num_ask(num)
    assert e.type == SystemExit


#Pruba de Lectura
@pytest.mark.parametrize(
    "path",
    [
        (r"C:\Users\Emily\Desktop\1.Tendencias\Prueba\std_1"),
        (r"C:\Users\Emily\Desktop\1.Tendencias\Prueba\std900291.txt")
 
    ]
)

def test_read_file_exit(path):
    with pytest.raises(SystemExit) as e:
        gp.read_file(path)
    assert e.type == SystemExit

#Probar requerimientos 
@pytest.mark.parametrize(
    "num, std_list, themes_list",
    [
        (5, ["Lenore", "Candice", "Chanel", "Chet"], ["Sociales", "Naturales", "Matematicas", "Lengua Española", "Religion"]), 
        (13, ["Lenore", "Candice", "Chanel", "Chet","Lorenzo","Juan","Maria","Jaime","Pedro","David","Jesus","Moises","Herodes"], 
          ["Sociales", "Naturales", "Matematicas", "Ingles", "Recreo", "Quimica", "Fisica", "Edu. Fisica"])
    ]
)
def test_req_exit(num, std_list, themes_list):
    with pytest.raises(SystemExit) as e:
        gp.req(num, std_list, themes_list)
    assert e.type == SystemExit
