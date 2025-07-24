def sort_colors():
    color_sequence = input("Enter hyphen-separated colors: ")  # e.g., green-red-yellow-black-white
    colors = color_sequence.split('-')
    colors.sort()
    sorted_sequence = '-'.join(colors)
    print("Sorted colors:", sorted_sequence)


# Call the function
sort_colors()
