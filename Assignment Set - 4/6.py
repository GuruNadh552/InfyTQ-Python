

def check_string(string):
    if(len(string)==1):
        return string
    s = ''
    li = 'aeiouAEIOU'
    for i in string:
        if i not in li:
            s+= i
    return s

def sms_encoding(data):
    #start writing your code here
    a = data.split()
    sent = []
    for i in a:
        sent.append(check_string(i))
    return ' '.join(sent)

data="I love Python"
print(sms_encoding(data))