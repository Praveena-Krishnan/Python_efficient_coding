def remove_matching_letters(name1, name2):
    # Convert names into lists of characters
    name1_list = list(name1)
    name2_list = list(name2)

    # Find common letters in both names
    common_letters = set(name1).intersection(set(name2))

    # Remove common letters from both names
    result_name1 = [char for char in name1_list if char not in common_letters]
    result_name2 = [char for char in name2_list if char not in common_letters]

    # Join the results together
    result = ''.join(result_name1 + result_name2)
    return result

# Example usage
name1 = "ARUN"
name2 = "SANA"
result = remove_matching_letters(name1, name2)
print(result)  # Output: "RUSA"