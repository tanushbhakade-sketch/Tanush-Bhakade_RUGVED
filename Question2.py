def sort_and_count_characters(s):
 
    s = s.replace(" ", "")
    
 
    sorted_str = ''.join(sorted(s))
    
  
    print("Sorted string:", sorted_str)
    
  
    print("Character counts:")
    for char in sorted(set(sorted_str)):
        count = sorted_str.count(char)
        print(f"{char}: {count}")


