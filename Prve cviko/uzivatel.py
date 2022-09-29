from xml.etree.ElementInclude import DEFAULT_MAX_INCLUSION_DEPTH


class Uzivatel:
    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        pass

    def print_info(self) -> str:
        return print(f"Meno: {self.first_name} Priezvisko: { self.last_name} Vek: {self.age}")

        
        