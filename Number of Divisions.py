def divisions(n, divisor):
    result = 0
    while n not in [0,1]:
        n //= divisor
        if n != 0:
            result += 1
    return result


#print(divisions(100, 2))

print(divisions(19782614033167944833, 5))