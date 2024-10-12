from time import sleep

from src.robot.build import build_robot
from src.robot.utils import welcome, lets_play, clear_screen


# inicializando o jogo
def play():
    playing = True

    welcome()
    sleep(5)
    print(f'\n\n\033[91m{"-"*40}\n|{"Datas for player 1:".center(38," ")}|\n{"-"*40}\n\033[0m')
    robot_one = build_robot()       # construção do robô 1
    sleep(5)
    clear_screen()
    # clear_output()    # em ambientes Jupyter Notebook tire o comentário desta linha e substitua pela linha acima
    welcome()
    sleep(5)
    print(f'\n\n\033[91m{"-"*40}\n|{"Datas for player 2:".center(38," ")}|\n{"-"*40}\n\033[0m')
    robot_two = build_robot()       # construção do robô 2
    sleep(5)

    current_robot = robot_one
    enemy_robot = robot_two
    round = 0

    while playing:
        # verifica de quem é a vez de jogar cada partida
        if round % 2 == 0:
            current_robot = robot_one
            enemy_robot = robot_two
        else:
            current_robot = robot_two
            enemy_robot = robot_one


        clear_screen()
        # clear_output()    # em ambientes Jupyter Notebook tire o comentário desta linha e substitua pela linha acima
        lets_play()
        sleep(2)
        # ADICIONADO para mostra o nome do robô que joga a partida
        turn = current_robot.name + "'s turn"
        print(f'\n\033[3;97;40m{turn.upper().center(100, " ")}\033[0m\n\n')

        current_robot.print_status()

        # MODIFICADO para verificar se a escolha de ataque do usuário é uma parte disponível do seu robô
        while True:
            print("What part should I use to attack?:")
            part_to_use = int(input("Choose a number part: "))

            # ADICIONADO para validação dos inputs
            if part_to_use < 0 or part_to_use > 5:
                print("\033[91mInvalid input. Please choose a number between 0 and 5.\n\033[0m")
            elif not current_robot.is_available_part(part_to_use):
                print("\033[91mOps... This part is not available. Choose another part!\n\033[0m")
            else:
                break

        print(f'\n\n{"=+"*40}\n\n')  # apenas uma separação visual dos robôs
        enemy_robot.print_status()

        # MODIFICADO para verificar se a escolha do usuário é uma parte disponível do robô inimigo
        while True:
            print("Which part of the enemy should we attack?")
            part_to_attack = int(input("Choose an enemy number part to attack: "))

            # ADICIONADO para validação do inputs
            if part_to_attack < 0 or part_to_attack > 5:
                print("\033[91mInvalid input. Please choose a number between 0 and 5.\n\033[0m")
            elif not enemy_robot.is_available_part(part_to_attack):
                print("\033[91mThis enemy part has been destroyed. Choose another part!\n\033[0m")
            else:
                break


        # o robô atual vai atacar o robo inimigo no "par_to_attack" com a "part_to_use"
        current_robot.attack(enemy_robot, part_to_use, part_to_attack)
        round += 1
        sleep(5)

        # ADICIONADO variáveis para um "print()" mais "limpo" no código
        f_title =f'\n\n{"H"*100}\n\n'
        game_over = f'{f_title}|{"Game Over !  {} won !".format(enemy_robot.name).center(98, " ")}|{f_title}'
        congrats = f'{f_title}|{"Congratulations {} !  You won !".format(current_robot.name).center(98, " ")}|{f_title}'

        # ADICIONADO para verifica se o robô tem energia suficiente para atacar
        if not current_robot.is_on():
            print('\033[1;91m', game_over.upper(),"\033[0m")
            playing = False

        # encerra o jogo quando todas as partes do robô inimigo são destruídas
        if not enemy_robot.is_on() or enemy_robot.is_there_available_part() == False:
            print('\033[1;92m', congrats.upper(), "\033[0m")
            playing = False

    # ADICIONADO um loop caso o jogador queira jogar novamente
    play_again = input("\n\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes" or play_again == "y":
        clear_screen()
        # clear_output()    # em ambientes Jupyter Notebook tire o comentário desta linha e substitua pela linha acima
        play()
    elif play_again == "no" or play_again == "n":
        print("\nOk. Until later!")
    else:
        print("\nSorry... Invalid Input. Until later!")


play()