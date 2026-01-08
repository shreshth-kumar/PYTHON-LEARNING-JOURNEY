import numpy as np

#step 1 : ask user for number of rolls
n = int(input("How many times do you want ot roll the dice? "))

#Step 2 : Simulate the rools using NumPy
# one array for each die

die1 = np.random.randint(1, 7, size=n)
die2 = np.random.randint(1, 7, size=n)

#step 3 : add the results
totals = die1 + die2

#step 4 : show the first few results
print("first 10 rolls (sum of dice) :", totals[:10])

# using bincount to count occurrences
freq = np.bincount(totals)

# only pront results for valid dice totals (2 to 12)
for total in range (2, 13):
    print(f"total {total}: {freq[total]} times")

for total in range (2, 13):
    percentage = (freq[total] / len(totals)) * 100
    print(f"total {total}: {freq[total]} times ({percentage: .2f}%)")