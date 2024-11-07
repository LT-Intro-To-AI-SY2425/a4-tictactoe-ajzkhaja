# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    species = "canis familiaris"

    def __init__(self, n, a):
        self.name = n
        self.age = a
        self.fetch_count = 0 
    def __str__(self):
        s = f"{self.name} is {self.age} years old"
        return s 
    # Dunder methods are methods that the program automatically creates 

    def play_fetch(self, num_fetch):
        self.fetch_count += num_fetch
    
    def fetch_reset(self):
        self.fetch_count = 0


logan = Dog("logan", 8)
becker = Dog("becker", 4)
kepa = Dog("kepa", 4)

print(logan.fetch_count)
logan.play_fetch(5)
print(logan.fetch_count)
logan.play_fetch(3)
print(logan.fetch_count)
logan.fetch_reset()
print(logan.fetch_count)

print(becker)
print(kepa)





