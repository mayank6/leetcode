class Solution:
    def judgeCircle(self, moves):
        v,h=0,0
        for i in moves:
            if (i=="U"):
                v+=1
            elif(i=="D"):
                v-=1
            elif(i=="R"):
                h+=1
            else:
                h-=1
        return h==v==0
