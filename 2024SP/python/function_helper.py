def line():
    print('***************') # 15 stars

def line_10():
    print('*' * 10)
    # print(line() * 10)

def line_n(num_of_stars):
    print('*' * num_of_stars)

# def multiple_lines():
#     line() * 10



def add_two_numbers(num_one, num_two):
    sum = int(num_one + num_two)
    return sum
    
def is_greater_than_10(num):
    # if 10 > 10:
    #     print('asldjfalsdkfj')
    if num > 10:
        return True
    elif num == 10:
        return "SAME"
    else:
        return False
    
# print(10 > 10)





















name = "Dave"

def change_name():
    name = "John"

def triangle():
    print('  *  ')
    print(' *** ')
    print('*****')

# print('HELPER FILE!!!!!')

def solid_rectangle():
    print('*****')
    print('*****')
    print('*****')

def hollow_rectangle():
    print('*****')
    print('*   *')
    print('*****')

def circle():
    print('  **  ')
    print(' *  * ')
    print(' *  * ')
    print('  ** ')