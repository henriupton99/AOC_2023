strings = open("input.txt").read().replace("\n","").split(",")
ans = 0
scores = []
for s in strings:
    # compute score of sequence (seq)
    score = 0
    for l in s:
        score += ord(l)
        score *= 17
        score = score % 256
    ans += score

print(ans)
        