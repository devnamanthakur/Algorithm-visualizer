def knapsack(weights, values, capacity, visualize_step=None):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],  # not taking this item
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]  # taking this item
                )
            else:
                dp[i][w] = dp[i - 1][w]
            
            if visualize_step:
                # Pass a deep copy for visualization to reflect changes
                from copy import deepcopy
                visualize_step(deepcopy(dp), i, w)
    
    return dp[n][capacity]