# 方法 d：用遞迴+查表+陣列 with Claude3.5
def power2n_d(n):
    # Initialize the memoization array with -1
    memo = [-1] * (n + 1)
    
    # Base case: 2^0 = 1
    memo[0] = 1
    
    def power2n_helper(n):
        # If we've already calculated this value, return it
        if memo[n] != -1:
            return memo[n]
        
        # If n is even, calculate 2^n as (2^(n/2))^2
        if n % 2 == 0:
            half = power2n_helper(n // 2)
            result = half * half
        # If n is odd, calculate 2^n as 2 * 2^(n-1)
        else:
            result = 2 * power2n_helper(n - 1)
        
        # Store the result in our memoization array
        memo[n] = result
        return result
    
    return power2n_helper(n)
print('power2n(10) =', power2n_d(10))
print('power2n(40) =', power2n_d(40))
