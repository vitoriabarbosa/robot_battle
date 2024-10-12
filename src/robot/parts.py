class Part:

    # ADICIONADO o atributo "part_status" para retornar de início todas as partes "True"
    def __init__(self, name: str, attack_level=0, defense_level=0, energy_consummation=0, part_status = True):
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consummation = energy_consummation
        self.part_status = part_status

    # retorna um dicionário preenchendo as informações das partes do robô
    def get_status_dict(self):
        formatted_name = self.name.replace(" ", "_").lower()
        return {
            "{}_name".format(formatted_name): self.name.upper(),
            "{}_status".format(formatted_name): self.is_available(),
            "{}_attack".format(formatted_name): self.attack_level,
            "{}_defense".format(formatted_name): self.defense_level,
            "{}_energy_consume".format(formatted_name): self.energy_consummation,
        }

    # MODIFICADO para quando o novel de defesa chegar a zero, o status da parte ficar "False"
    def reduce_and_defense(self, attack_level):
        self.defense_level -= attack_level
        if self.defense_level <= 0:
            self.defense_level = 0
            self.part_status = False

    # MODIFICADO para retornar o status das partes do robô
    def is_available(self):
        return self.part_status
        # return self.defense_level >= 0        # deixar partes disponíveis "True"