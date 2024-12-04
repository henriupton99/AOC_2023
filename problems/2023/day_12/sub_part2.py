from collections import defaultdict

def get_arangement_count(seq, nums):
    nums_count = len(nums)
    arangements = dict()
    arangements[0, 0] = 1

    def is_valid(group_index, current_group_size, strict):
        try:
            if strict:
                return current_group_size == nums[group_index]
            else:
                return current_group_size <= nums[group_index]
        except:
            return False

    for c in seq:
        new_arangements = defaultdict(int)
        for (group_index, current_group_size), count in arangements.items():
            valid = True
            if c == '#':
                current_group_size += 1
                valid = is_valid(group_index, current_group_size, False)
            elif c == '?':
                if current_group_size > 0:
                    if is_valid(group_index, current_group_size):
                        new_arangements[group_index + 1, 0] += count
                else:
                    new_arangements[group_index, current_group_size] += count
                new_arangements[group_index, current_group_size + 1] += count
                continue
            else:
                if current_group_size > 0:
                    valid = is_valid(group_index, current_group_size)
                    current_group_size = 0
                    group_index += 1
            if valid:
                new_arangements[group_index, current_group_size] += count
        arangements = new_arangements
    c = 0
    for (group_index, current_group_size), count in arangements.items():
        if current_group_size > 0:
            try:
                if current_group_size != nums[group_index]:
                    continue
            except:
                continue
            group_index += 1
        if group_index == nums_count:
            c += count
    return c


with open("input.txt") as file:
    ans = 0
    for line in file.readlines():
        seq, nums = line.split()
        seq = "?".join(5 * [seq])
        nums = [int(n) for n in nums.split(",")]*5
        ans += get_arangement_count(seq,nums)

print(ans)