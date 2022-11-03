class Solution:
    def intToRoman(self, num: int) -> str:
        notations=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        pos=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman=""
        for no,p in zip(notations,pos):
            if num>=p:
                roman+=no*(num//p)
                num=num%p
        return roman
      
'''
notations=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
pos=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
n=int(input())
roman=""
for no,p in zip(notations,pos):
    if n>=p:
        roman+=no*(n//p)
        n=n%p
print(roman)
'''
        
        
