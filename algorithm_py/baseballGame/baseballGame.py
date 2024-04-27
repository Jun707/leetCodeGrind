#Initial Approach
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        nums=[]
        flag = True
        add = 0
        add1 = 0
        add2=0
        temp=0
        for i in range(len(operations)):
            try:
                int(operations[i])
            except ValueError:
                flag = False
            if flag:
                nums.append(int(operations[i]))
            else:
                flag=True
                if operations[i]=="C":
                    nums.pop()
                elif operations[i]=="D":
                    temp=nums.pop()
                    nums.append(temp)
                    nums.append(temp*2)
                elif operations[i]=="+":
                    add1= nums.pop()
                    add2=nums.pop()
                    add = add1+add2
                    nums.append(add2)
                    nums.append(add1)
                    nums.append(add)
        return sum(nums)