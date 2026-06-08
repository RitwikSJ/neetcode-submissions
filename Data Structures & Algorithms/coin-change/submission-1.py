class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = dict()
        dp[0] = 0

        for i in coins:
            dp[i] = 1
        
        min_coin = min(coins)
        
        for target in range(min_coin + 1, amount + 1):
            choices = []

            if target not in dp:
                for coin in coins:
                    if target - coin < min_coin:
                        dp[target - coin] = -1
                    if target - coin >= 0 and dp[target - coin] != -1:
                        choices.append(dp[target - coin])
                dp[target] = 1 + min(choices) if choices else -1
        
        return dp[amount] if amount in dp else -1