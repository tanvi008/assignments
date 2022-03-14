#if you want to type two numbers then put space in between 
#for word to number
num1 = input("Enter number1: ")
num2 = input("Enter number2: ")
class W2n:
    def convertw(self,word):
        arr= {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            'zero' : '0'
        }
        res = ''.join(arr[ele] for ele in word.split())
        
        return res


def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)



#code for number to word
def get_word_value(n):
    x ={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    return x.get(n)
def convert_num_to_words(n):
    s = ""
    for i in range(len(num)):
        s = s + get_word_value(int(num[i]))
    return s



#for word to number
temp = W2n()
a =int(temp.convertw(num1))
b =int(temp.convertw(num2))
print(a,b)

numm= gcd(a,b)
print("Result of gcd is: ",numm)



# here I have to give number as a input then only it will convert that number to string 


# for number to word
num = input("Enter numnum ")
print(convert_num_to_words(num))