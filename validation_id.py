import re

def is_even(index):
    return index % 2 == 0

def sum_not_even(temp_digits):
    temp_digits = int(temp_digits)*2
    sum_digits =0
    if temp_digits > 9:
        digit = temp_digits % 10
        sum_digits += digit + int(temp_digits/10)
        return sum_digits
    else:
        return temp_digits

def lohan_algorytm(id):
    index_id= 0
    sum_digits= 0
    for digit in id:
        if is_even(index_id):
            sum_digits += int(digit)
        else:
            sum_digits += sum_not_even(digit)
        index_id += 1
    # CODREVIEW: change to range loop
    # for index_id in range(len(id)):
    #     digit = int(id[index_id])
    #
    #
    unity_digit = sum_digits % 10
    if unity_digit == 0:
        lohan_safe_digit=0
    else: lohan_safe_digit = 10 - unity_digit
    return lohan_safe_digit

def validation(id_number):
    pattern = '^[0-9]{9}$'
    id_result = re.match(pattern, id_number)
    if not id_result:
        return "pattern ID doesn't exsits"
    last_index = len(id_number)-1
    last_digit = id_number[last_index]
    id_without_last_digit = id_number[:last_index]
    safe_digit = lohan_algorytm(id_without_last_digit)
    return safe_digit == int(last_digit)
