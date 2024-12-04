import collections
strings = open("input.txt").read().replace("\n","").split(",")
boxes = collections.defaultdict(dict[list])
for s in strings:
    if len(s.split("="))==2:
        seq, lens = s.split("=")[0], s.split("=")[1]
        dash = False
    else:
        seq = s.replace("-","")
        dash = True
    
    # first step : compute score of sequence (seq)
    score = 0
    for l in seq:
        score += ord(l)
        score *= 17
        score = score % 256
    
    # second step : add or remove from box = score
    
    # if dash is present in the string, add lens in the box
    if not dash:
        boxes[score][seq] = lens
    
    # else, try to remove the lens if sequence is in the box
    # otherwise just pass
    else:
        try:
            del boxes[score][seq]
        except:
            pass
    
ans = 0
for box, content in boxes.items():
    if content:
        for i, (string,lens) in enumerate(content.items()):
            ans += (box+1)*(i+1)*int(lens)

print(ans)
        