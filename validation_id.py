import re
def is_even(index):
    if index % 2 == 0 or index == 0:
        is_even=True
    else:
        is_even = False
    return is_even

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

    unity_digit = sum_digits % 10
    if unity_digit == 0:
        lohan_safe_digit=0
    else: lohan_safe_digit = 10 - unity_digit
    return lohan_safe_digit

def validation(id_number):
    pattern = '^[0-9]{9}$'
    id_result= re.match(pattern, id_number)
    if id_result:
        last_index = len(id_number)-1
        last_digit = id_number[last_index]
        id_without_last_digit = id_number[0:last_index]
        safe_digit = lohan_algorytm(id_without_last_digit)

        if safe_digit == int(last_digit):
            validation_status = True
            print(f'validation: {validation_status}')
            return validation_status
        else:
            validation_status = False
            print(f'validation: {validation_status}')
            return validation_status
    else: return "pattern ID doesn't exsits"