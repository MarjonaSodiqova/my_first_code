def invest(a, r, y):
    for y in range(1, y + 1):
        a += a * r
        print(f"year {y}: ${a:.2f}")

initial_amount = float(input("Enter the initial amount in $: "))
annual_rate = float(input("Enter the annual rate of return in decemal: "))
num_years = int(input("Enter the number of years: "))

invest(initial_amount, annual_rate, num_years)
