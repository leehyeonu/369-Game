def 게임시작():
    숫자 = 1
    플레이어차례 = False

    while True:
        if 플레이어차례:
            사용자입력 = input()
            if (사용자입력.isdigit() and int(사용자입력) == 숫자 and
                    str(숫자).count('3') + str(숫자).count('6') + str(숫자).count('9') == 0):
                숫자 += 1
                플레이어차례 = False
            elif 사용자입력 in ["짝", "짝짝", "짝짝짝"]:
                카운트 = str(숫자).count('3') + str(숫자).count('6') + str(숫자).count('9')
                if 카운트 > 0 and 카운트 == len(사용자입력):
                    숫자 += 1
                    플레이어차례 = False
            else:
                print("틀렸습니다. 다시 시도하세요.")
        else:
            컴퓨터입력 = str(숫자) if str(숫자).count('3') + str(숫자).count('6') + str(숫자).count('9') == 0 else "짝" * (str(숫자).count('3') + str(숫자).count('6') + str(숫자).count('9'))
            숫자 += 1
            print(컴퓨터입력)
            플레이어차례 = True

게임시작()
