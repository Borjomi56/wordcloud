# # 1. открытие файла
# f=open("r.txt", encoding="utf-8")
# print(f.read())

#  2.открытие файла с обработкой ошибки
# try:   
#     f=open("r.txt", encoding="utf-8")
#     print(f.read())
# except:
#     print( "файл не найден")

# 3.разделение текст на строки(линии)
f=open("r.txt", encoding="utf-8")
# print(f.read())

for line in f:
    # print(line)

    words=line.split()
    print(words)







































































