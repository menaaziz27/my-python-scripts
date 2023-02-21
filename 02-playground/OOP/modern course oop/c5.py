# class Variables second case (Validation)

class Pet:
    Allowed = ['cat' , 'dog', 'fish', 'rat']
    def __init__(self, name, species):
        if species not in Pet.Allowed:
            raise ValueError (f"You can't have a {species} pet!")
        self.name = name
        self.species = species
    def set_species(self,specie):
        if specie not in Pet.Allowed:
            raise ValueError(f"You can't have a {specie} pet!")
        self.species = specie

cat = Pet("Fluffy" , "cat")
dog = Pet("wyatt" , "dog")
''' Pet("Dragon" ,"Dinasour") FIXME XXX TODO'''
# not_allowed = Pet("Dragon" , "Dinasour")
# dog.species = 'tiger'   #FIXME
# print(dog.species)      
# dog.set_species("Tiger") #Works now 

Pet.Allowed.append("Pig")

cat.species = 'Pig'
# print(cat.__dict__)
# cat.Allowed = ['hamster' , 'rabbits'] #creating a new instance attribute for cat instance only
# print(id(cat.Allowed))
# print(cat.__dict__)
# print(dog.__dict__)

# print(Pet.Allowed)