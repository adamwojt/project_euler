def count_digits(num):
    """sum digits in number"""
    stringy = str(num)
    sum_dig = 0
    for dig in stringy:
        sum_dig += int(dig)
    return sum_dig

def generate_num(a, b):
    """generate power"""
    return a**b

def main():
    """main function"""
    list_powers = [generate_num(a, b) for a in range(1, 100) for b in range(1, 100)]
    list_sums = [count_digits(num) for num in list_powers]
    print(max(list_sums))

if __name__ == '__main__':
    main()
