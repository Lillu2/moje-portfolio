import csv

class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon


    def __str__(self):
        """Vrací textovou reprezentaci pojištěného pro výpis na obrazovku."""
        return f"{self.jmeno} {self.prijmeni}, Věk: {self.vek}, Telefon: {self.telefon}"


class EvidencePojistenych:
    def __init__(self):
        self.pojisteni = []

    def pridej_pojisteneho(self, pojisteny):
        """Přidá nového pojištěného do evidence."""
        self.pojisteni.append(pojisteny)
        print(f"Pojištěný {pojisteny} byl úspěšně přidán.")

    def uloz_do_csv(self, soubor):
        """Uloží seznam pojištěných do CSV souboru."""
        with open(soubor, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Jméno', 'Příjmení', 'Věk', 'Telefon'])
            for pojisteny in self.pojisteni:
                writer.writerow([pojisteny.jmeno, pojisteny.prijmeni, pojisteny.vek, pojisteny.telefon])
        print(f"Data byla uložena do souboru {soubor}.")

    def nacti_z_csv(self, soubor):
        """Načte seznam pojištěných z CSV souboru."""
        self.pojisteni.clear()  #  Vymaže předchozí data, aby se nezdvojovala
        try:
            with open(soubor, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Přeskočí hlavičku
                for row in reader:
                    if len(row) == 4:  # Ověří, že řádek má správný počet sloupců
                        jmeno, prijmeni, vek, telefon = row
                        self.pojisteni.append(Pojisteny(jmeno, prijmeni, int(vek), telefon))
            print(f"Data byla načtena ze souboru {soubor}.")
        except FileNotFoundError:
            print(f"Soubor {soubor} nebyl nalezen.")
        except Exception as e:
            print(f"Nastala chyba při načítání dat: {e}")

    def vypis_vsechny_pojistene(self):
        if not self.pojisteni:
            print("Seznam pojištěných je prázdný.")
        else:
            for pojisteny in self.pojisteni:
                print(pojisteny)

    def najdi_pojisteneho(self, jmeno, prijmeni):
        """Najde pojištěného podle jména a příjmení."""
        for pojisteny in self.pojisteni:
            if pojisteny.jmeno.lower() == jmeno.lower() and pojisteny.prijmeni.lower() == prijmeni.lower():
                return pojisteny
        return None


class UzivatelskeRozhrani:
        def __init__(self):
            self.evidencePojistenych = EvidencePojistenych()

        def spustit(self):
            while True:
                print("\n1. Přidat pojištěného")
                print("2. Vypis všech pojištěných")
                print("3. Najít pojištěného")
                print("4. Konec")
                print("5. Uložit data do souboru")
                print("6. Načíst data ze souboru")

                volba = input("Zadejte číslo volby: ")

                if volba == "1":
                    self.pridej_pojisteneho()
                elif volba == "2":
                    self.evidencePojistenych.vypis_vsechny_pojistene()
                elif volba == "3":
                    self.najdi_pojisteneho()
                elif volba == "4":
                    print("Ukončuji program.")
                    break
                elif volba == "5":
                    soubor = input("Zadejte název souboru pro uložení (např. data.csv): ")
                    self.uloz_data(soubor)
                elif volba == "6":
                    soubor = input("Zadejte název souboru pro načtení (např. data.csv): ")
                    self.nacti_data(soubor)
                else:
                    print("Neplatná volba, zkuste to znovu.")

        def pridej_pojisteneho(self):
            """Získá údaje od uživatele a přidá nového pojištěného do evidence."""
            jmeno = input("Zadejte jméno pojištěného: ").strip()
            prijmeni = input("Zadejte příjmení pojištěného: ").strip()

            try:
                vek = int(input("Zadejte věk pojištěného: ").strip())
            except ValueError:
                print("Věk musí být celé číslo. Zkuste to znovu!")
                return
            telefon = input("Zadejte telefonní číslo pojištěného: ").strip()

            if not jmeno or not prijmeni:
                print("Jméno a příjmení nesmí být prázdné!")
                return

            novy_pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
            self.evidencePojistenych.pridej_pojisteneho(novy_pojisteny)

        def najdi_pojisteneho(self):
            """Získá jméno a příjmení a najde pojištěného."""
            jmeno = input("Zadejte jméno pojištěného: ").strip()
            prijmeni = input("Zadejte příjmení pojištěného: ").strip()

            if not jmeno or not prijmeni:
                print("Jméno a příjmení nesmí být prázdné!")
                return

            pojisteny = self.evidencePojistenych.najdi_pojisteneho(jmeno, prijmeni)
            if pojisteny:
                print(f"Nalezen pojištěný: {pojisteny}")
            else:
                print("Pojištěný nebyl nalezen.")

        def uloz_do_csv(self, soubor):
            """Uloží seznam pojištěných do CSV souboru."""
            self.evidencePojistenych.uloz_do_csv(soubor)

        def nacti_z_csv(self, soubor):
            """Načte seznam pojištěných z CSV souboru."""
            self.evidencePojistenych.nacti_z_csv(soubor)

        def uloz_data(self, soubor):
            """Uloží data do CSV souboru."""
            self.uloz_do_csv(soubor)

        def nacti_data(self, soubor):
            """Načte data z CSV souboru."""
            self.nacti_z_csv(soubor)


if __name__ == "__main__":
    rozhrani = UzivatelskeRozhrani()
    rozhrani.spustit()





