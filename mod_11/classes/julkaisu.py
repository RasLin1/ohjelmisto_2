class Julkaisu():
    def  __init__(self, name):
        self.name = name

    def tulosta_tiedot(self):
        print("")
        print(f"{self.name}")

class Kirja(Julkaisu):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count
    
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.author} | Sivumäärä: {self.page_count}")

class Lehti(Julkaisu):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.chief_editor}")