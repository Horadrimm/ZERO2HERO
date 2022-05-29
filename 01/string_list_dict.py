numbers = "One,Two,Three,Four,Three"

numbers_list = numbers.split(",")

like_number = ("Four", "Three")

number_dict = {
    "One" : 1,
    "Two" : 2, 
    "Three" : {
        "Four" : 5,
        "Six" : 6,
    },
}
print(number_dict.get("aslkjdlkasj") )

# number_dict["asdas"] = 10
# print(number_dict)
# print(numer_dict["Three"])


# for k in number_dict["Three"]:
#     print(number_dict["Three"][k])


# print(numbers_list[2])

count_nums = {}
for x in numbers_list:
    
    if x in like_number:
        if (count_nums.get(x) != None):
            count_nums[x] = count_nums[x] + 1
        else:
            count_nums[x] = 1


print(count_nums)
# print("Любимых чисел", count)


# Домашнее задание 
# Заккомитить и запушить текущие изменения
# Есть ссылка https://api.coindesk.com/v1/bpi/currentprice.json
# Необходимо по ней получить данные
# Из этих данных сформировать существующие в pyhton структуру данных ( словари, списки етц )

# Создать программу, которая будет выводить стоимость битка в выбранных валютах с помощью поля "rate"
# Мы должны выводить стоимость в валютах USD, EUR
# Предполагается, что кол-во валют бесконечное.

# Ключевые  библиотеки: json, requests
# Кроме них ничего не используем 

# Находим индусов на ютубе, смотрим про 
#     Словари (dict)
#     Списки (list)
#     Строки (str)










# print (numbers)

# print(type(numbers))
# print(dir(numbers))
# print(numbers.upper())

# print(numbers_list)

# 123 тысячи 123 и 34 сотых
# fucking_number = "123,123.34"
# normal_nunber = fucking_number.replace(",","")

# int_number  = 44 
# float_numer = 44.213232
# print(type(float_numer))

# print ( type( 34 * float("15.6") ) )

# print( 10 * float(normal_nunber))



