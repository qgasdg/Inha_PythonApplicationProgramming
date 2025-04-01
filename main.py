import search_utils as su

arr = [2, 4, 6, 8, 10, 12]
print(f"미리 정의된 리스트: {arr}")
num = int(input("찾을 숫자를 입력하세요: "))
tmp = su.binary_search(arr, num, 0, len(arr) - 1)
if tmp == -1:
    print(f"숫자 {num}은(는) 리스트에 존재하지 않습니다.")
else:
    print(f"숫자 {num}은(는) 인덱스 {tmp}에 있습니다.")
