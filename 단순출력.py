def clap_game(count):
    for num in range(1, count + 1):
        if '3' in str(num) or '6' in str(num) or '9' in str(num):
            clap_count = str(num).count('3') + str(num).count('6') + str(num).count('9')
            print('짝!' * clap_count)
        else:
            print(num)


def play_game():
    # 게임 횟수 입력
    total_count = int(input("게임 횟수를 입력하세요: "))

    # 게임 시작
    clap_game(total_count)


# 게임 시작
play_game()
