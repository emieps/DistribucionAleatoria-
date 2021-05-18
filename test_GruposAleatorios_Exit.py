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

#Pruba de Lectura
@pytest.mark.parametrize(
    "path",
    [
        (r"C:\Users\Emily\Desktop\1.Tendencias\Prueba\std_1"),
        (r"C:\Users\Emily\Desktop\1.Tendencias\Prueba\std900291.txt"),
 
    ]
)

#Probar requerimientos 
@pytest.mark.parametrize(
    "num, std_list, themes_list",
    [
        (5, ["Lenore", "Candice", "Chanel", "Chet"], ["Sociales", "Naturales", "Matematicas", "Lengua Española", "Religion"]), 
        (13, ["Lenore", "Candice", "Chanel", "Chet","Lorenzo","Juan","Maria","Jaime","Pedro","David","Jesus","Moises","Herodes"], 
          ["Sociales", "Naturales", "Matematicas", "Ingles", "Recreo", "Quimica", "Fisica", "Edu. Fisica"]),
    ]
)