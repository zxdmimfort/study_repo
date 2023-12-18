from collections import Counter


words = [Counter(input()) for _ in range(int(input()))]
correct = Counter("TINKOFF")
for word in words:
    
    print("Yes" if correct == word else "No")
