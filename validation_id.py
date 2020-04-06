import re , json

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


def json_msg_response(status,msg):
    return json.dumps({'status': status, 'msg': msg})


def validation(id_number):
    pattern = '^[0-9]{9}$'
    id_result= re.match(pattern, id_number)
    valid_msg = {
        'not_exsit': 'Pattern ID doesn\'t exsit',
        'valid': 'Your ID is valid',
        'not_valid': 'Your ID is NOT valid'
    }
    status={
        'False': False,
        'True': True
    }

    if not id_result:
        return json.dumps({'status': status['False'],'msg': valid_msg['not_exsit']})

    last_digit = id_number[-1]
    id_without_last_digit = id_number[:-1]
    safe_digit = lohan_algorytm(id_without_last_digit)

    if safe_digit == int(last_digit):
        return json.dumps( {'status': status['True'],'msg': valid_msg['valid']})
    else:
        return json.dumps({'status':status['False'], 'msg':valid_msg['not_valid']})