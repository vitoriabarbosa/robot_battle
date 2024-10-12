# criando uma string multilinhas

robot_art = r"""

          |0: {head_name}
          |Is available: {head_status}
          |Attack: {head_attack}
          |Defense: {head_defense}
          |Energy consume: {head_energy_consume}
                  ^
                  |                  |1: {weapon_name}
                  |                  |Is available: {weapon_status}
         ____     |    ____          |Attack: {weapon_attack}
        |oooo|  ____  |oooo| ------> |Defense: {weapon_defense}
        |oooo| '    ' |oooo|         |Energy consume: {weapon_energy_consume}
        |oooo|/\_||_/\|oooo|
        `----' / __ \ `----'            |2: {left_arm_name}
       '/  |#|/\/__\/\|#|  \'           |Is available: {left_arm_status}
       /  \|#|| |/\| ||#|/  \           |Attack: {left_arm_attack}
      / \_/|_|| |/\| ||_|\_/ \          |Defense: {left_arm_defense}
     |_\/    O\=----=/O    \/_|         |Energy consume: {left_arm_energy_consume}
     <_>      |=\__/=|      <_> ------> |
     <_>      |------|      <_>         |3: {right_arm_name}
     | |   ___|======|___   | |         |Is available: {right_arm_status}
    //\\  / |O|======|O| \  //\\        |Attack: {right_arm_attack}
    |  |  | |O+------+O| |  |  |        |Defense: {right_arm_defense}
    |\/|  \_+/        \+_/  |\/|        |Energy consume: {right_arm_energy_consume}
    \__/  _|||        |||_  \__/
          | ||        || |          |4: {left_leg_name}
         [==|]        [|==]         |Is available: {left_leg_status}
         [===]        [===]         |Attack: {left_leg_attack}
          >_<          >_<          |Defense: {left_leg_defense}
         || ||        || ||         |Energy consume: {left_leg_energy_consume}
         || ||        || || ------> |
         || ||        || ||         |5: {right_leg_name}
       __|\_/|__    __|\_/|__       |Is available: {right_leg_status}
      /___n_n___\  /___n_n___\      |Attack: {right_leg_attack}
                                    |Defense: {right_leg_defense}
                                    |Energy consume: {right_leg_energy_consume}

"""


# dicionário de cores

colors = {
    "Black":   '\033[90m',
    "Blue":   '\033[94m',
    "Cyan":   '\033[96m',
    "Green":   '\033[92m',
    "Magenta":  '\033[95m',
    "Red":    '\033[91m',
    "White":   '\033[97m',
    "Yellow":   '\033[93m',
}
