def merge_lists(list_1, list_2):
    # Create a new list that is the two lists joined together
    merged_list = list_1 + list_2
    return merged_list


# Main function
def main():
    list1 = []
    list2 = []
    # Get the first list from the user
    list1_str = input("Enter the first list of elements: ")

    # Split the input string on commas
    list1 = list1_str.split(" ")

    # Get the second list from the user
    list2_str = input("Enter the second list of elements: ")

    # Split the input string on commas
    list2 = list2_str.split(" ")

    # Call the merge_lists function and store the result
    merged_list = merge_lists(list1, list2)

    # Print the merged list
    print("The two lists joined together are:", merged_list)


if __name__ == "__main__":
    main()
