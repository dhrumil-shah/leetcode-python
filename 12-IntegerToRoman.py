class Solution:       
    def intToRoman(self, num: int) -> str:
        r = num
        ret = []
        if 1000 <= num <= 3999:
            p = 3
        if 100 <= num <= 999:
            p = 2
        if 10<=num <=99:
            p = 1
        if 1 <=num <= 9 :
            p = 0
        while r !=0:
            q,r = divmod(r, 10**p)
            if (p ==3):
                ret.append('M'* q)
            elif (p ==2):
                if (q==4):
                    ret.append('CD')
                elif(q==5):
                    ret.append('D')
                elif(q==6):
                    ret.append('DC')
                elif(q==7):
                    ret.append('DCC')
                elif(q==8):
                    ret.append('DCCC')
                elif(q==9):
                    ret.append('CM')                
                else:
                    ret.append('C'*q)
            elif (p==1):
                if (q==4):
                    ret.append('XL')
                elif(q==5):
                    ret.append('L')
                elif(q==6):
                    ret.append('LX')
                elif(q==7):
                    ret.append('LXX')
                elif(q==8):
                    ret.append('LXXX')
                elif(q==9):
                    ret.append('XC')                
                else:
                    ret.append('X'*q)
            elif (p ==0):
                if (q==4):
                    ret.append('IV')
                elif(q==5):
                    ret.append('V')
                elif(q==6):
                    ret.append('VI')
                elif(q==7):
                    ret.append('VII')
                elif(q==8):
                    ret.append('VIII')
                elif(q==9):
                    ret.append('IX')
                else:
                    ret.append('I'*q)
            p -=1
        return "".join(ret)
