def is_valid_credit_card(card_number):
    
    card_number = card_number.replace(" ", "").replace("-", "")
    
    if not card_number.isdigit():
        return False

    total = 0
    reverse_digits = card_number[::-1]

    for i, digit in enumerate(reverse_digits):
        n = int(digit)
      
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n

  
    return total % 10 == 0


