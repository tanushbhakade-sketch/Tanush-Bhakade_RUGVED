def divide_string(s, n):
    
    if len(s) % n != 0:
        print("Error: String length is not divisible by given part size.")
        return


    parts = len(s) // n

   
    first_part = s[:n]

    
    for i in range(1, parts):
        if s[i*n:(i+1)*n] != first_part:
            print("Error: The string cannot be divided into equal repeating sequences.")
