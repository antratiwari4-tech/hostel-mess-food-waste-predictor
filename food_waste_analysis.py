
import pandas as pd
import matplotlib.pyplot as plt

# Example data only — not real hostel records
data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"],
    "Meal": ["Lunch", "Lunch", "Lunch", "Lunch",
             "Lunch", "Lunch", "Lunch"],
    "Students_Expected": [180, 170, 190, 175, 200, 130, 110],
    "Meals_Prepared": [200, 190, 210, 195, 220, 160, 140],
    "Meals_Consumed": [175, 165, 185, 170, 195, 125, 105]
}

df = pd.DataFrame(data)

# Calculate leftover meals
df["Leftover_Meals"] = (
    df["Meals_Prepared"] - df["Meals_Consumed"]
)

print("HOSTEL MESS FOOD WASTE ANALYSIS")
print("-" * 35)
print(df.to_string(index=False))

print("\nTotal meals prepared:", df["Meals_Prepared"].sum())
print("Total meals consumed:", df["Meals_Consumed"].sum())
print("Total leftover meals:", df["Leftover_Meals"].sum())

waste_percentage = (
    df["Leftover_Meals"].sum()
    / df["Meals_Prepared"].sum()
) * 100

print(f"Leftover meal percentage: {waste_percentage:.2f}%")

# Plot daily leftovers
plt.figure(figsize=(9, 5))
plt.bar(df["Day"], df["Leftover_Meals"])
plt.title("Daily Leftover Meals")
plt.xlabel("Day")
plt.ylabel("Number of leftover meals")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("daily_leftover_meals.png")
plt.show()
