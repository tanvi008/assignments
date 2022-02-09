class Solution:
    def check( strs):
        res ={} #empty dict that holds anagram subsets
        for i in strs:
            a = sorted(list(i))
            b = ''.join(a)

            if b in res:
                res[b].append(i)
            else:
                res[b] = [i] 

        return(list(res.values()))
           


           
lst =[]
n = int(input("Enter number of elements you want to enter in string: "))
for i in range(0,n):
    ele = input()
    lst.append(ele)

print("Input",lst)
print("Output: ",Solution.check(lst))