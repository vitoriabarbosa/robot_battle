from src.assets.art import robot_art, colors
from src.robot.parts import Part

class Robot:
    def __init__(self, name, color_code):
        self.name = name
        self.color_code = color_code
        self.energy = 100
        self.parts = [
            Part("Head", attack_level=5, defense_level=10, energy_consummation=5),
            Part("Weapon", attack_level=15, defense_level=0, energy_consummation=10),
            Part("Left Arm", attack_level=3, defense_level=20, energy_consummation=10),
            Part("Right Arm", attack_level=6, defense_level=20, energy_consummation=10),
            Part("Left Leg", attack_level=4, defense_level=20, energy_consummation=15),
            Part("Right Leg", attack_level=8, defense_level=20, energy_consummation=15),
        ]


    def print_status(self):
        print(self.color_code)

        #   formatando para string o robot_art, (**) desempacota o return "part_status" e pega as chaves e
        #   valores do "get_part_status" e preenche nas partes reservadas do "robot_art {}"
        str_robot = robot_art.format(**self.get_part_status())

        self.greet()
        self.print_energy()
        print(str_robot)
        print(colors["White"])  # cor default


    def greet(self):    # saudação
        print("Hello, my name is", self.name)

    def print_energy(self): # energia
        print("We have", self.energy, " percent energy left")


    def get_part_status(self):
        part_status = {}
        for part in self.parts:
            #   obtendo o status de cada parte do robo no status_dict e adicionando no part_status
            status_dict = part.get_status_dict()
            part_status.update(status_dict)
        return part_status

    # retorna se o status da parte do robô está "True" ou "False"
    def is_there_available_part(self):
        for part in self.parts:
            if part.is_available():
                return True
        return False

    # ADICIONADO para retornar somente as partes disponíveis do robô para atacar
    def is_available_part(self, part_index):
        return self.parts[part_index].is_available()

    # MODIFICADO para retornar somente energia > 0 (robô está ligado!)
    def is_on(self):
        return self.energy > 0


    def attack(self, enemy_robot, part_to_use, part_to_attack):

        # ADICIONADO para verificar quando o usuário realizar um ataque com energia insuficiente
        if self.energy < self.parts[part_to_use].energy_consummation:
            print(f"\n\033[91m{self.name.capitalize()}, you don't have energy enough to attack.\n\033[0m")

        # seleciona a parte que sera atacada do robo inimigo no dict parts, em seguida, chama o
        # metodo "reduce_and_defense" (da parte selecionada do robo), passando como atributo o nivel
        # de ataque do robo que está atacando
        enemy_robot.parts[part_to_attack].reduce_and_defense(self.parts[part_to_use].attack_level)
        self.energy -= self.parts[part_to_use].energy_consummation

        # ADICIONADO para impedir energia negativa
        if self.energy <= 0:
            self.energy = 0
