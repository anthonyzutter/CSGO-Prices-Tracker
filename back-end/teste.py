from classe import *
import os

if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    i1 = Item(nome = "AK-47 | Redline (Field-Tested)", preco = "R$ 82,62", 
    exterior = "Testada em Campo", quantidade = "1")

    i2 = Item(nome = "M4A4 | Desolate Space (Field-Tested)", preco = "R$ 65,75", 
    exterior = "Testada em Campo", quantidade = "2")

    i3 = Item(nome = "AWP | Atheris (Minimal Wear)", preco = "R$ 27,40", 
    exterior = "Pouco Usada", quantidade = "1")

    i4 = Item(nome = "Desert Eagle | Emerald Jörmungandr (Factory New)", preco = "R$ 430,53", 
    exterior = "Nova de Fábrica", quantidade = "1")

    db.session.add(i1)
    db.session.add(i2)
    db.session.add(i3)
    db.session.add(i4)
    db.session.commit()

    print(i1.json())
    print(i2.json())
    print(i3.json())
    print(i4.json())