result = [[] for _ in range(2)]

try:
    with open("numbers.txt", "r") as file:
        lineNum = 0
        while True:
            try:
                line = file.readline().split()
                lineNum += 1
                if line == []:
                    break
                line[0], line[2] = map(float, (line[0], line[2]))
                if line[1] == '+':
                    result[0].append("{} + {} = {:.1f}".format(line[0], line[2], line[0] + line[2]))
                elif line[1] == '-':
                    result[0].append("{} - {} = {:.1f}".format(line[0], line[2], line[0] - line[2]))
                elif line[1] == '*':
                    result[0].append("{} * {} = {:.1f}".format(line[0], line[2], line[0] * line[2]))
                elif line[1] == '/':
                    result[0].append("{} / {} = {:.1f}".format(line[0], line[2], line[0] / line[2]))
                else:
                    raise ArithmeticError
            except ValueError as e:
                result[1].append(f"Line {lineNum}: 숫자 포맷 오류가 발생했습니다.")
            except ZeroDivisionError as e:
                result[1].append(f"Line {lineNum}: 0으로 나눌 수 없습니다.")
            except ArithmeticError as e:
                result[1].append(f"Line {lineNum}: 지원하지 않는 연산자를 사용했습니다.")
            except Exception as e:
                result[1].append(f"Line {lineNum}: 알 수 없는 오류입니다.")

    print("계산결과:")
    print(*result[0], sep='\n')
    print()
    print("오류가 발생한 줄:")
    print(*result[1], sep='\n')
except FileNotFoundError as e:
    print("파일이 존재하지 않습니다.")
except Exception as e:
    print("알 수 없는 오류입니다.")
