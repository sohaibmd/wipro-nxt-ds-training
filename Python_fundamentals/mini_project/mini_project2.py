# MINI PROJECT 2: Cloud Hosting Cost Estimator

hourly_rate = 0.51


daily_cost = hourly_rate * 24
weekly_cost = daily_cost * 7
monthly_cost = daily_cost * 30

print(f"Cost to operate one server per day: ${daily_cost:.2f}")
print(f"Cost to operate one server per week: ${weekly_cost:.2f}")
print(f"Cost to operate one server per month: ${monthly_cost:.2f}")


budget = float(input("Enter your budget in dollars: $"))

days_possible = budget / daily_cost
print(f"You can operate one server for approximately {days_possible:.2f} days with ${budget:.2f}")
