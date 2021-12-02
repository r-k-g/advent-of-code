def tribonacci(n):
    """get tribonacci number at point n>2"""
    dp = [0] * n
    dp[2] = 1
    
    for i in range(3, n):
        dp[i] = sum(dp[i-3:i])
    
    return dp

def manual_input():
    inp_l = []
    while True:
        i = input()
        if i.lower() == "!q":
            break
        inp_l.append(i)
    return "\n".join(inp_l)