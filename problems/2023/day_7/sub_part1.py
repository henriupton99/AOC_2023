from collections import Counter
import pandas as pd
with open("input.txt") as file:
    hands = []
    bids = []
    for line in file.readlines():
        content = line.split(" ")
        hands.append([figure for figure in content[0]])
        bids.append(int(content[1]))

df = pd.DataFrame({"hand":hands, "bid":bids})

def first_sort(hand):
    hand_count = Counter(hand).values()
    # five of a kind :
    if 5 in hand_count:
        return 1
    # four of a kind
    elif 4 in hand_count:
        return 2
    # full house :
    elif 3 in hand_count and 2 in hand_count:
        return 3
    # three of a kind :
    elif 3 in hand_count:
        return 4
    # two pair :
    elif 2 in hand_count \
        and Counter(hand_count)[2]==2:
        return 5
    # one pair :
    elif 2 in hand_count :
        return 6
    else:
        return 7

df["first_rank"] = df["hand"].apply(first_sort)

# figures ranks :
figures_ranks = {'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9':8,\
    '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}

def second_sort(hand):
    return [figures_ranks[figure] for figure in hand]

df["second_rank"] = df["hand"].apply(second_sort)
res = pd.DataFrame()
for first_rank, group in df.groupby("first_rank"):
    res = pd.concat([res,group.sort_values(by="second_rank",ascending=False)])

res = res.reset_index().drop(["index"],axis=1)
res["rank"] = len(res)
res["rank"] -= res.index

print(sum(res["bid"]*res["rank"]))