n = int(input())
for i in range(n):
    l = input()
    count = 0
    score = 0
    for j in range(len(l)):
        if(l[j]=='O'):
            count+=1
            score+=count
        else: count = 0
    print(score)