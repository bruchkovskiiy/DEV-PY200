if __name__ == "__main__":


    class Animal:
        def __init__(self, species, age, health):
            self.species = species
            self.age = age
            self.health = health
            self.alive = True

        def age_up(self):
            # Старение животного. Возраст растет, здоровье немного падает
            if self.alive:
                self.age += 1
                self.health -= 5
                self.check_alive()

        def eat(self, amount):
            # Питание восстанавливает здоровье
            if self.alive:
                self.health += amount
                if self.health > 100:
                    self.health = 100

        def check_alive(self):
            # Проверка, живо ли животное
            if self.health <= 0:
                self.alive = False
            return self.alive


    class Herbivore(Animal):
        def eat_plant(self):
            print(f"{self.species} ест траву")
            self.eat(10)


    class Carnivore(Animal):
        def hunt(self, prey):
            if self.alive and prey.alive:
                print(f"{self.species} охотится на {prey.species}!")
                prey.health = 0
                prey.check_alive()
                self.eat(20)


    class Omnivore(Animal):
        def eat_anything(self, food_type):
            print(f"{self.species} ест {food_type}.")
            self.eat(15)


    class World:
        def __init__(self):
            self.animals = []

        def add_animal(self, animal):
            self.animals.append(animal)

        def life_cycle(self):
            # Проведение цикла жизни для всех обитателей
            print("\n--- Новый цикл жизни ---")
            for animal in self.animals:
                if animal.alive:
                    animal.age_up()
                    # Простая логика автоматического питания в цикле
                    animal.eat(5)

        def check_world_status(self):
            # Проверка состояния всех животных
            print("Статус мира:")
            for animal in self.animals:
                status = "Жив" if animal.alive else "Мертв"
                print(f"{animal.species} | Возраст: {animal.age} | Здоровье: {animal.health} | Статус: {status}")


my_world = World()

zebra = Herbivore(species="Зебра", age=2, health=80)
lion = Carnivore(species="Лев", age=5, health=90)

my_world.add_animal(zebra)
my_world.add_animal(lion)

print("Начальное состояние:")
my_world.check_world_status()

lion.hunt(zebra)

my_world.life_cycle()
my_world.life_cycle()

print("\nФинальное состояние:")
my_world.check_world_status()