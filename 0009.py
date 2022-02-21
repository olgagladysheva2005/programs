n = int(input())
chisla1 = input().split()
chisla = chisla1[:n]
chisla = [int(i) for i in chisla]
summ = [i for i in chisla if i > 0]
mx = str(max(chisla))
mn = str(min(chisla))
c = ''.join(chisla1)
a = c.find(mx)
b = c.find(mn)

print(sum(summ), )