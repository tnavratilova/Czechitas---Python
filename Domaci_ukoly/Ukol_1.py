from math import ceil

class Locality:
    def __init__(self, name, coefficient):
        self.name = name
        self.coefficient = coefficient

class Property:
    def __init__(self, locality):
        self.locality = locality

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
    
    def calculate_tax(self):
        tax = 0
        if self.estate_type == "land":
            tax = self.area * 0.85 * self.locality.coefficient
        if self.estate_type == "building site":
            tax = self.area * 9 * self.locality.coefficient
        if self.estate_type == "forrest":
            tax = self.area * 0.35 * self.locality.coefficient
        return ceil(tax)
    
    def __str__(self):
        oznaceni = {
            "land": "Zemědělský pozemek",
            "building site": "Stavební pozemek",
            "forrest": "Les"
        }
        return f"{oznaceni[self.estate_type]}, lokalita {self.locality.name} (koeficient {self.locality.coefficient}), {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."

lokalita_1 = Locality("Praha", 2)    
lesni_pozemek = Estate(lokalita_1, "forrest", 500)

print(lesni_pozemek.calculate_tax())
print(lesni_pozemek.__str__())
    
class Residence(Property):
    def __init__(self, locality, area, commercial=False):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        if self.commercial == True:
            tax = self.area * self.locality.coefficient * 15 * 2
        else:
            tax = self.area * self.locality.coefficient * 15
        return ceil(tax)
    
    def __str__(self):
        if self.commercial == True:
            typ_nemovitosti = "Komerční nemovitost"
        else:
            typ_nemovitosti = "Nemovitost"
        return f"{typ_nemovitosti} o ploše {self.area} metrů čtverečních v lokalitě {self.locality.name} s koeficientem {self.locality.coefficient}, má daň ve výši {self.calculate_tax()} Kč."



lokalita_2 = Locality("Manětín", 0.8)
lokalita_3 = Locality("Brno", 3)

zem_pozemek = Estate(lokalita_2, "land", 900)
dum = Residence(lokalita_2, 120)
kancelar = Residence(lokalita_3, 90, True)

print(zem_pozemek.calculate_tax())
print(dum.calculate_tax())
print(kancelar.calculate_tax())
print(dum.__str__())
print(kancelar.__str__())
