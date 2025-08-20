class Solution(object):
    def plusOne(self, digits):
        s=""
        for i in digits:
            s+=str(i)
        total=int(s)
        total+=1
        total=str(total)
        lst=[]
        for i in total:
            lst.append(int(i))

        return lst

        