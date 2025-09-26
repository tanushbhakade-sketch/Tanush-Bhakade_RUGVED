def is_hill_number(n):
    digits = list(map(int, str(n)))
    
    if len(digits) < 3:
        return False 

    i = 1

    while i < len(digits) and digits[i] >= digits[i - 1]:
        i += 1

    if i == 1 or i == len(digits):  
        return False

    while i < len(digits) and digits[i] <= digits[i - 1]:
        i += 1

    return i == len(digits)


