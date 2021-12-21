

def find_common_characters(msg1,msg2):
    msg1 = msg1.replace(" ","")
    msg2 = msg2.replace(" ","")
    common = ''
    for i in msg1:
        if i in msg2:
            if i not in common:
                common += i
    if len(common)>0:
        return common
    else:
        return -1

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)