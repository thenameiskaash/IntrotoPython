x = 0
while(x < 5):
    print(f"x is not 5 yet.  It is {x}")
    x += 1

print(f"It looped {x} times")

n = 0
for left in range(7):
    for right in range(7):
        print(f"[ left : {str(left)} | right : {str(right)} ]", end=" ")
        n += 1
    print()
print(n)

teams = ['Wolves', 'Dragon', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(f"{home_team} vs {away_team}")

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

print(f"{factorial(3)}")

