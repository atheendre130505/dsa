
def lengthOfLastWord(s):
        length=0
        x=s.split()
        y=x[-1]
        return len(y)

s="Hello World"
            

len = lengthOfLastWord(s)
print(len)  # Output: 5 