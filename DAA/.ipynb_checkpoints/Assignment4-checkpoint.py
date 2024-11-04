# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    dp = [0 for i in range(W+1)]  # Creating the dp array
    
    # Iterating over each item
    for i in range(1, n+1):
        # Iterating through all capacities starting from the maximum
        for w in range(W, 0, -1):
            # If the current item's weight is less than or equal to the current capacity
            if wt[i-1] <= w:
                # Update dp[w] to the maximum of either taking the current item or not
                dp[w] = max(dp[w], dp[w - wt[i-1]] + val[i-1])
    
    return dp[W]  # Returning the maximum value for the full knapsack capacity

# Driver code
val = [60, 100, 120]  # Values of items
wt = [10, 20, 30]     # Weights of items
W = 50                # Capacity of knapsack
n = len(val)          # Number of items

# Function call to find the maximum value that can be carried
print(knapSack(W, wt, val, n))
