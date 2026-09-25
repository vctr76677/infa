n = int(input())
sum = sum(map(int, input().split()))
total=n*(n+1)//2
card = total-sum

print(card)