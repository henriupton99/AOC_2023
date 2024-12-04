import re

with open("input.txt") as file:
    count_map = 0
    for line in file.readlines():
        if line.__contains__("seeds"):
            seeds = [int(e) for e in re.findall("[0-9]+",line)]
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
            for seed in seeds:
                if seed>=source and seed<=source+dict_range and seed not in mapping_dict.keys():
                    mapping_dict[seed] = dest + (seed-source)

seeds = [mapping_dict[seed] 
        if seed in mapping_dict.keys()
        else seed for seed in seeds]

print(seeds)
print(min(seeds))