def climb_random(n):
    import random
    x = 1
    result = [x]
    while True:
        if result[-1] == n:
            return result
        if result[-1] > n:
            x = 1
            result = [x]
        x = eval(random.choice([f"2*{x}", f"2*{x}+1"]))
        result.append(x)

#print(climb(100000))

def climb(n):
    x = n
    result = [n]
    while result[-1] != 1:
        if x % 2:
            x = (x - 1) // 2
        else:
            x = x // 2
        result.append(int(x))
    return result[::-1]
    
print(climb(588583886501776960809973918513))
