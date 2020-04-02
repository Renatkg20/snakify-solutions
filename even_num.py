user_input_numbers = input('Please input numbers ').split(' ')
list_ = []
for _ in user_input_numbers:
    list_.append(_)
for index in range(0, len(list_)+1, 2):
    print(list_[index], end = ' ')
# b = float(input())