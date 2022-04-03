def to_hex(n):
    hex = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    output = []
    if n < 0 or n > 255:
        return "Invalid"
    elif n ==0:
        return "0x0"
    div_n = n // 16
    rem_n = n % 16
    output.append(rem_n)
    while(rem_n != 0):
        rem_n = div_n % 16
        output.append(rem_n)
        div_n = div_n // 16
    output = output[::-1]
    output = output[1:]
    str = "0x"
    for i in output:
        str += hex[i]
    return str        

print(to_hex(175))
