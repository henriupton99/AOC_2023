import re

with open("input.txt") as file:
    count_map = 0
    for line in file.readlines():
        if line.__contains__("seeds"):
            values = [int(e) for e in re.findall("[0-9]+",line)]
            starts = [val for i,val in enumerate(values) if i%2==0]
            ranges = [val for i,val in enumerate(values) if i%2!=0]
                    
        if line.__contains__("map"):
            if count_map == 0:
                mapping_dict = {}
                count_map +=1
            else:
                seeds = [mapping_dict[seed] 
                     if seed in mapping_dict.keys()
                     else seed for seed in seeds]
                mapping_dict = {}
                
        digits_matches = [int(e) for e in re.findall("[0-9]+",line)]
        if len(digits_matches)==3:
            dest,source = digits_matches[0],digits_matches[1]
            dict_range = digits_matches[2]
            for k in range(len(starts)):
                seeds_range = set(range(starts[k],starts[k]+ranges[k]))
                mapping_range = range(source,source+dict_range)
                print(seeds_range.intersection(mapping_range))
                ok
                

seeds = [mapping_dict[seed] 
        if seed in mapping_dict.keys()
        else seed for seed in seeds]

print(min(seeds))