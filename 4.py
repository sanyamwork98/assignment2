def print_rangoli(size):
    import string 
    alphabet = string.ascii_lowercase
    lines = []
    for i in range(size):
        left = alphabet[size-1:i:-1] 
        right = alphabet[i:size]      
        row = '-'.join(left + right)
        lines.append(row.center(4*size - 3, '-'))
        
    full_rangoli = lines[::-1][:-1] + lines
    print('\n'.join(full_rangoli))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
