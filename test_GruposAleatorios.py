import pytest


#Prueba de Division
@pytest.mark.parametrize(
    "lst, div, except",
    [
        (["Lenore", "Candice", "Chanel", "Chet","Lorenzo"],5,1), 
        (["Lenore", "Candice", "Chanel", "Lorenzo"],4,2), 
        (["Lenore", "Candice", "Chanel", "Chet","Lorenzo","Juan","Maria","Jaime","Pedro","David","Jesus","Moises","Herodes"],6,2), 
        (["Lenore", "Candice", "Chanel", "Chet","Lorenzo","Juan","Maria","Jaime","Pedro","David","Jesus","Moises","Herodes"],5,2), 
    ]
)

#Prueba de Remanente
@pytest.mark.parametrize(
    "lst, rem, except",
    [
        (["Lenore", "Candice", "Chanel", "Chet","Lorenzo"],5,0), 
        (["Lenore", "Candice", "Chanel", "Lorenzo"],4,0), 
        (["Lenore", "Candice", "Chanel", "Chet","Lorenzo","Juan","Maria","Jaime","Pedro","David","Jesus","Moises","Herodes"],6,1), 
        (["Lenore", "Candice", "Chanel", "Chet","Lorenzo","Juan","Maria","Jaime","Pedro","David","Jesus","Moises","Herodes"],5,3), 
    ]
)

#Prueba de Remanente
@pytest.mark.parametrize(
    "lst, rem, except",
    [
        
    ]
)