import re , json
from consts import valid_msg_dict , valid_status_dict

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
    sum_digits= 0
    for index_id, digit in enumerate(id):
        if index_id %2 ==0:
            sum_digits += int(digit)
        else:
            sum_digits += sum_not_even(digit)

    unity_digit = sum_digits % 10
    if unity_digit == 0:
        return 0
    return 10 - unity_digit

def json_msg_response(res_status,res_msg):
    return json.dumps({'status': valid_status_dict[res_status], 'valid_msg': valid_msg_dict[res_msg]})

def validation(id_number):
    pattern = '^[0-9]{9}$'
    id_result = re.match(pattern, id_number)

    if not id_result:
        return json_msg_response('False', 'not_exist')

    last_digit = id_number[-1]
    id_without_last_digit = id_number[:-1]
    safe_digit = lohan_algorytm(id_without_last_digit)

    if safe_digit == int(last_digit):
        return json_msg_response('True', 'valid')
    else:
        return json_msg_response('False', 'not_valid')