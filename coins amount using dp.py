#coins problem using dp
def can_make_amount(coins, amount):
    n = len(coins)
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for j in range(amount, coin - 1, -1):
            if dp[j - coin] == 1:
                dp[j] = 1
            elif dp[j - coin] == 0 and (j - coin) > amount:
                dp[j] = 1

    return dp[amount]
coins = list(map(int, input("Enter coins: ").split()))
amount = int(input("Enter amount: "))

if can_make_amount(coins, amount):
    print("yes")
else:
    print("No")

