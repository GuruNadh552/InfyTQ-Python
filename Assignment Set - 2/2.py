#lex_auth_012693802383794176153

def form_triangle(num1,num2,num3):
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    if(num1<num2+num3 and num2<num1+num3 and num3<num1+num2):
        return success
    return failure

#Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
num3=5
print(form_triangle(num1, num2, num3))