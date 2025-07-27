people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

# Display the original list
print("Original List:")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")

print("\n--- Updating Facts ---\n")

# Update Jeff's fact
people_facts["Jeff"] = "Is afraid of heights."

# Add a new person and fact
people_facts["Jill"] = "Can hula dance."

# Display the updated list
print("Updated List:")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")
