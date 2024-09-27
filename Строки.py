print("Повторяет слово N раз\n    Напишите любое слово")
w = input()
print("Сколько раз его повторить?")
n = int(input())
print ("В строчку: ")
for i in range(0, n):
    print(w, end=" ")
print("\n")
print ("В столбик: ")
for i in range(0, n):
    print(w)
print("\n")
print("Без пробелов: ", w*n)
