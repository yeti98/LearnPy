
class Animals:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
    def info(self):
        print(self.name," ", self.legs);


    # override __hash__ vs __eq__ is very important
    def __hash__(self) -> int:
        return hash(self.name)+hash(self.legs)

    def __eq__(self, o: object) -> bool:
        return (self.__class__==o.__class__ and self.name==o.name and self.legs==o.legs)

