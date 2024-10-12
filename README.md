# 🎮 Batalha de robôs 🤖

## 📋 Introdução
Este projeto é um jogo de combate entre robôs, onde 2 jogadores criam seus próprios robôs e os enviam para a batalha. O objetivo é destruir todas as partes do robô inimigo ou zerar sua energia.

## 🕹 Funcionalidades
1. ### Construção de Robôs:
    - Os jogadores constroem seus robôs, com nomes e cores de sua preferência.
    - O robô é composto por 6 partes diferentes: Cabeça, Arma, Braço Esquerdo, Braço Direito, Perna Esquerda e Perna Direita.
    - Cada parte tem seus próprios níveis de ataque, defesa e consumo de energia.
   <br><br>
   
    >           |0: {head_name}
    >           |Is available: {head_status}
    >           |Attack: {head_attack}
    >           |Defense: {head_defense}
    >           |Energy consumption: {head_energy_consume}
    >                   ^
    >                   |                  |1: {weapon_name}
    >                   |                  |Is available: {weapon_status}
    >          ____     |    ____          |Attack: {weapon_attack}
    >         |oooo|  ____  |oooo| ------> |Defense: {weapon_defense}
    >         |oooo| '    ' |oooo|         |Energy consumption: {weapon_energy_consume}
    >         |oooo|/\_||_/\|oooo| 
    >         `----' / __ \ `----'            |2: {left_arm_name}
    >        '/  |#|/\/__\/\|#|  \'           |Is available: {left_arm_status}
    >        /  \|#|| |/\| ||#|/  \           |Attack: {left_arm_attack}
    >       / \_/|_|| |/\| ||_|\_/ \          |Defense: {left_arm_defense}
    >      |_\/    O\=----=/O    \/_|         |Energy consumption: {left_arm_energy_consume}
    >      <_>      |=\__/=|      <_> ------> |
    >      <_>      |------|      <_>         |3: {right_arm_name}
    >      | |   ___|======|___   | |         |Is available: {right_arm_status}
    >     //\\  / |O|======|O| \  //\\        |Attack: {right_arm_attack}
    >     |  |  | |O+------+O| |  |  |        |Defense: {right_arm_defense}
    >     |\/|  \_+/        \+_/  |\/|        |Energy consumption: {right_arm_energy_consume}
    >     \__/  _|||        |||_  \__/
    >           | ||        || |          |4: {left_leg_name}
    >          [==|]        [|==]         |Is available: {left_leg_status}
    >          [===]        [===]         |Attack: {left_leg_attack}
    >           >_<          >_<          |Defense: {left_leg_defense}
    >          || ||        || ||         |Energy consumption: {left_leg_energy_consume}
    >          || ||        || || ------> |
    >          || ||        || ||         |5: {right_leg_name}
    >        __|\_/|__    __|\_/|__       |Is available: {right_leg_status}
    >       /___n_n___\  /___n_n___\      |Attack: {right_leg_attack}
    >                                     |Defense: {right_leg_defense}
    >                                     |Energy consumption: {right_leg_energy_consume}

2. ### Jogadas por Turnos:
    - Os jogadores alternam entre turnos para atacar.
    - Durante um turno, um jogador escolhe uma parte do seu robô para atacar e a parte do robô inimigo que deseja atingir.
    - O ataque diminui a defesa da parte atingida do robô inimigo e consome energia do robô atacante.

3. ### Vitória e Derrota:
    - O jogo termina quando um robô perde todas as partes ou fica sem energia.
    - O jogador cujo robô ainda tem partes ou energia restante é declarado vencedor.


<br><br>
> ## 💡 Como Jogar
>   1. #### Execute o código em um ambiente Python (IDE, terminal, etc.).
>   2. #### Siga as instruções para criar os robôs, com nomes e cores para eles.
>   3. #### Alternadamente, escolha as partes do seu robô para atacar e a parte do robô inimigo que deseja atingir.
>   4. #### Continue jogando até que um robô seja declarado vencedor ou até que você decida encerrar o jogo.
>   5. #### No final do jogo, você pode escolher jogar novamente ou encerrar o jogo


## 🛠️ Implementação
- **Linguagem de Programação:** Python
    - Versão: 3.10.12


## 🚀 Começando

### Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)


### Instalação
1. #### Clone o repositório:
    ```bash
     git clone https://github.com/vitoriabarbosa/robot_battle.git
    ```

2. #### Navegar até o Diretório do Projeto:
    ```bash
     cd robot_battle
    ```

3. #### Verificar a instalação do Python:
    - Verifique se você tem o Python instalado na sua maquina.
   ```bash
    python --version 
   ```

4. #### Executar a Aplicação:
    - No terminal, execute:
    ```bash
     python -m src.game
    ```


## 🤝 Colaboradores
- [Bruno Reis](#)
- [Maria Clara Pares](https://github.com/MariaPaes)
- [Vitória Barbosa](https://github.com/vitoriabarbosa)


## 📝 Licença
Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
