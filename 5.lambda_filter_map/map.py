def double_number(numero):
    return numero*2

number_list = [2, 5, 10, 23, 50, 33]

double_number_list = map(double_number, number_list)

for number in double_number_list:
    print(number)