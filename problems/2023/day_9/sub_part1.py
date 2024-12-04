with open("input.txt") as file:
    extrapolation_values = []
    for history in file.readlines():
        history = [int(x) for x in history.split()]
        # bottleneck part :
        bottleneck = [history]
        while not all(x==0 for x in bottleneck[-1]):
            bottleneck.append([bottleneck[-1][k+1]-bottleneck[-1][k] for k in range(len(bottleneck[-1])-1)])
        
        # extrapolation part :
        bottleneck[-1].append(0)
        for l in range(1,len(bottleneck)):
            bottleneck[-(l+1)].append(bottleneck[-l][-1]+bottleneck[-(l+1)][-1]) 
        
        extrapolation_values.append(bottleneck[0][-1])
    
print(sum(extrapolation_values))        