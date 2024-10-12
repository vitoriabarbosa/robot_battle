from src.assets.art import colors
from src.robot.robot import Robot


# PARTE 5
# construindo o robô

def build_robot():
    robot_name = input("Robot name: ")
    color_code = choose_color()
    robot = Robot(robot_name, color_code)
    robot.print_status()
    return robot

# escolhendo a cor do robô
def choose_color():
    available_colors = colors
    print("\nAvailable colors:")
    for key, value in available_colors.items():
        print(value, key)
    print(colors["White"])  # cor default
    # ADICIONADO para validação do inputs
    while True:
        chosen_color = input("Choose a color: ").capitalize()
        if chosen_color not in available_colors:
            print("\033[91mInvalid color. Please choose a valid color.\033[0m\n")
        else:
            break
    color_code = available_colors[chosen_color]
    return color_code