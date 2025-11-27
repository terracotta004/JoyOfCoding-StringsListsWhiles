# stringslistswhiles.py
# Ben Underwood

# A collection of functions that demonstrate the use of strings, lists, and while loops in Python.

def average_neg_evens(numbers):
    """
    Calculate the average of negative even numbers in a list.
    
    Parameters:
    numbers (list): A list of integers.
    
    Returns:
    float: The average of negative even numbers, or 0 if there are none.
    """
    total = 0
    count = 0
    index = 0
    
    while index < len(numbers):
        if numbers[index] < 0 and numbers[index] % 2 == 0:
            total += numbers[index]
            count += 1
        index += 1
    
    if count == 0:
        return 0
    else:
        return total / count
    
def count_letter(string_list, letter):
    """
    Count the occurrences of a specific letter in a list of strings.
    
    Parameters:
    string_list (list): A list of strings.
    letter (str): The letter to count.
    
    Returns:
    int: The total count of the specified letter in all strings.
    """
    total_count = 0
    index = 0
    
    while index < len(string_list):
        total_count += string_list[index].lower().count(letter)
        index += 1
    
    return total_count

def main():
    # Test the average_neg_evens function
    test_list = [0, 1, 2, -2, -3, -4, 3, 4]
    result = average_neg_evens(test_list)
    print(f"The average of negative even numbers in {test_list} is: {result}")

    # Test the count_letter function
    string_list = ["HELLO", "goodbye", "1234 Oooh!"]
    letter = 'o'
    count = count_letter(string_list, letter)
    print(f"The letter '{letter}' appears {count} times in the list {string_list}.")


if __name__ == "__main__":
    main()