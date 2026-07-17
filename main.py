import itertools
def dfs_n_queens(n):
    if n < 1 or n == 2 or n == 3:
        return []
    elif n == 1:
        return [[0]]
    result = []
    y = [x for x in range(n)]
    result = list(itertools.permutations(y))
    result = [list(result[x]) for x in range(len(result))]
    res = []
    for x in result:
        valid = True
        for y in range(len(x)):
            i1 = x.index(x[y])
            for j in range(y + 1, len(x)):
                i2 = x.index(x[j])
                if abs(i1 - i2) == abs(x[y] - x[j]) and j == len(x) - 1:
                    valid = False
                if abs(i1 - i2) == abs(x[y] - x[j]):
                    break
                
           
            if j != len(x) - 1:
                break
        
        if y == len(x) - 1 and abs(x[len(x)-1] - x[len(x)-2]) != 1 and valid:
            res.append(x)
    
    return res
    
print(len(dfs_n_queens(8)))
        
    
            
 


        