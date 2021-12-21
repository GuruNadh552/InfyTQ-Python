
def create_largest_number(number_list):
    number_list.sort()
    number_list = number_list[::-1]
    s = ''
    for i in number_list:
        s+=str(i)
    return int(s)

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)