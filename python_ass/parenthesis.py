#this is the program for parenthesis 
#here open bracket should be greater than 
class Main:
    def para(self,n:int):
        list=[]
        res =[]

        def func(bopen,bclose):
            if bopen == bclose == n:
                res.append(''.join(list))
                return

            if bopen < n:
                list.append("(")
                func(bopen+1,bclose)
                list.pop() #this stack is a global variable so everytime we are done with function we are poppping the character that we just added to stack 

            if bclose < bopen:
                list.append(")")
                func(bopen,bclose+1)
                list.pop()

        func(0,0)
        return res


n = int(input("Enter number of parentheses you want: "))
sol = Main()
print(sol.para(n))