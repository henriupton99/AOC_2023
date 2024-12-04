import itertools

with open("input.txt") as file:
    ans = 0
    for line in file.readlines():
        seq, nums = line.split()
        seq = list(seq.replace(" ",""))
        nums = [int(n) for n in nums.split(",")]
        
        num_hashtags = len([e for e in seq if e=="#"])
        empty_indexes = [i for i,e in enumerate(seq) if e=="?"]
        num_hashtags_to_fill = sum(nums) - num_hashtags
        
        for indexes in itertools.combinations(empty_indexes,num_hashtags_to_fill):
            temp = seq.copy()
            for i in indexes:
                temp[i] = "#"
            temp = [e if e!="?" else "." for e in temp]

            seq_hashtags = []
            count = 0
            actual_seq = []
            for e in temp:
                if e == "#":
                    actual_seq.append("#")
                elif actual_seq:
                    seq_hashtags.append(actual_seq)
                    actual_seq = []
            if actual_seq:
                seq_hashtags.append(actual_seq)
            len_seq_hashtags = [len(seq) for seq in seq_hashtags]
            
            if len_seq_hashtags == nums:
                ans += 1

print(ans)