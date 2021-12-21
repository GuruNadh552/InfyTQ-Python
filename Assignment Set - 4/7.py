
    
def max_frequency_word_counter(data):
    word=""
    frequency=0
    data = data.lower()
    data = data.replace(',','')
    sent = data.split()
    for i in sent:
        if(sent.count(i)>frequency):
            frequency = sent.count(i)
            word = i
    if(frequency==1):
        c = ''
        for j in sent:
            if(len(j)>len(c)):
                c = j
        print(c,1)
    else:
        print(word,frequency)

#Provide different values for data and test your program.
data="Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)