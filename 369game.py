'''
게임 설명 
1. 게임 도중 "다시시작" 또는 "restart" 치면 게임 다시시작

2. 1부터 숫자를 하나씩 대면서, 3, 6, 9가 들어가는 숫자는 숫자를 치는 대신 짝을 입력 
2-1. 3/6/9가 두번 들어가는 숫자(예: 33, 36, 39)에서는 박수를 두번 쳐야 하며, 
2-2. 3/6/9가 세번 들어가는 숫자(예: 333, 336, 339, 363)에서는 박수를 세번 쳐야 한다.
'''

import time

# 게임 플레이 함수
def play_game():
    current_number = 1  # 현재 숫자 초기화
    player_turn = False  # 플레이어 차례 여부 초기화
    records = []  # 기록을 저장하는 리스트 초기화

    while True:
        if player_turn:
            # 플레이어 차례
            user_input = input("당신의 차례입니다. 숫자 또는 '짝'을 입력하세요: ")
            if user_input.lower() == "다시시작":
                # 게임 다시 시작
                current_number = 1
                player_turn = False
                records = []
                print("게임을 다시 시작합니다.")
                time.sleep(1)  # 1초 대기
                continue
            if user_input.isdigit():
                if int(user_input) == current_number and count_369(current_number) == 0:
                    # 입력이 숫자이고, 현재 숫자와 같으며, 3, 6, 9가 포함되지 않은 경우
                    records.append(user_input)  # 기록에 숫자 추가
                    current_number += 1  # 다음 숫자로 이동
                    player_turn = False  # 컴퓨터 차례로 변경
                else:
                    # 입력이 잘못된 경우
                    print("틀렸습니다. 다시 시도하세요.")
                    time.sleep(1)  # 1초 대기
            elif user_input in ["짝", "짝짝", "짝짝짝"]:
                count = count_369(current_number)
                if count > 0 and count == len(user_input):
                    # 입력이 '짝', '짝짝', '짝짝짝' 중 하나이고, 현재 숫자에 포함된 3, 6, 9의 개수와 일치하는 경우
                    records.append(user_input)  # 기록에 짝 추가
                    current_number += 1  # 다음 숫자로 이동
                    player_turn = False  # 컴퓨터 차례로 변경
                else:
                    # 입력이 잘못된 경우
                    print("틀렸습니다. 다시 시도하세요.")
                    time.sleep(1)  # 1초 대기
            else:
                # 입력이 잘못된 경우
                print("틀렸습니다. 다시 시도하세요.")
                time.sleep(1)  # 1초 대기
        else:
            # 컴퓨터 차례
            computer_input = generate_computer_input(current_number)  # 컴퓨터 입력 생성
            records.append(computer_input)  # 기록에 컴퓨터 입력 추가
            current_number += 1  # 다음 숫자로 이동
            player_turn = True  # 플레이어 차례로 변경

# 컴퓨터 입력 생성 함수
def generate_computer_input(number):
    count = count_369(number)  # 현재 숫자에 포함된 3, 6, 9의 개수
    if count > 0:
        # 현재 숫자에 포함된 3, 6, 9의 개수에 따라 '짝'을 반복해서 반환
        return "짝" * count
    else:
        # 3, 6, 9가 없는 경우 현재 숫자를 문자열로 반환
        return str(number)

# 3, 6, 9 개수 세는 함수
def count_369(number):
    return str(number).count('3') + str(number).count('6') + str(number).count('9')

# 콘솔 지우기 함수
def clear_console():
    # 콘솔 화면을 지우기 위해 특수 문자열 출력
    print("\033c", end="")

# UI 출력 함수
def print_ui(current_number, player_turn, records):
    clear_console()
    print("===============================================================")
    print(""" 
   ____     ___    ___          ___     __     _  _    ____ 
  ( __ \   / __)  / _ \        / __)   / _\   ( \/ )  (  __)
  (__ (   (  _ \  \__  )      ( (_ \  /    \  / \/ \   ) _) 
  (____/   \___/  (___/        \___/  \_/\_/  \_)(_/  (____)
""")
    print("===============================================================")
    print("     현재 숫자:", current_number)
    print("     차례:", "당신" if player_turn else "컴퓨터")
    print("---------------------------------------------------------------")
    print("기록:")
    for record in records:
        # 기록을 한 줄씩 출력
        print(record)

# UI로 게임 플레이 함수
def play_game_with_ui():
    current_number = 1
    player_turn = False
    records = []

    while True:
        print_ui(current_number, player_turn, records)
        if player_turn:
            # 플레이어 차례
            user_input = input("당신의 차례입니다. 숫자 또는 '짝'을 입력하세요: ")
            if user_input.lower() == "다시시작":
                # 게임 다시 시작
                current_number = 1
                player_turn = False
                records = []
                print("게임을 다시 시작합니다.")
                time.sleep(1)  # 1초 대기
                continue
            if user_input.isdigit():
                if int(user_input) == current_number and count_369(current_number) == 0:
                    # 입력이 숫자이고, 현재 숫자와 같으며, 3, 6, 9가 포함되지 않은 경우
                    records.append(user_input)  # 기록에 플레이어 입력 추가
                    current_number += 1  # 다음 숫자로 이동
                    player_turn = False  # 컴퓨터 차례로 변경
                else:
                    # 입력이 잘못된 경우
                    print("틀렸습니다. 다시 시도하세요.")
                    time.sleep(1)  # 1초 대기
            elif user_input in ["짝", "짝짝", "짝짝짝"]:
                count = count_369(current_number)  # 현재 숫자에 포함된 3, 6, 9의 개수
                if count > 0 and count == len(user_input):
                    # 입력이 '짝', '짝짝', '짝짝짝' 중 하나이고, 현재 숫자에 포함된 3, 6, 9의 개수와 일치하는 경우
                    records.append(user_input)  # 기록에 플레이어 입력 추가
                    current_number += 1  # 다음 숫자로 이동
                    player_turn = False  # 컴퓨터 차례로 변경
                else:
                    # 입력이 잘못된 경우
                    print("틀렸습니다. 다시 시도하세요.")
                    time.sleep(1)  # 1초 대기
            else:
                # 입력이 잘못된 경우
                print("틀렸습니다. 다시 시도하세요.")
                time.sleep(1)  # 1초 대기
        else:
            # 컴퓨터 차례
            computer_input = generate_computer_input(current_number)  # 컴퓨터 입력 생성
            records.append(computer_input)  # 기록에 컴퓨터 입력 추가
            current_number += 1  # 다음 숫자로 이동
            player_turn = True  # 플레이어 차례로 변경

# UI로 게임 플레이 시작
play_game_with_ui()
