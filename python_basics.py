def basic_operations():
    # Printing
    print('Hello World')

    # Variables & data types
    x: int = 10  # int
    y: float = 20.3  # float

    # Complex Numbers
    comp: complex = 4 + 5j
    print(f'Complex number: {comp}')

    # Boolean
    flag: bool = False
    boolean_expression: bool = (5 > 3) and (2 < 4) and not flag
    print(f"Boolean Expression ((5 > 3) and (2 < 4) and not flag): {boolean_expression}.")

    # None Type
    nothing: None = None
    print(nothing)

    # Type Casting
    str_to_int: int = int("124")
    print(f'String to int: {str_to_int}, typeof: {type(str_to_int)}')
    str_to_float: float = float("124.12")
    print(f'String to float: {str_to_float}, typeof: {type(str_to_float)}')
    int_to_str: str = str(1252)
    print(f'String to str: {int_to_str}, typeof: {type(int_to_str)}')

    # Adding f in front of the quotes allows string interpolation
    print(f'Sum: {x + y}')
    print(f'Subtraction: {x - y}')
    print(f'Multiplication: {x * y}')
    print(f'Division: {x / y}')
    print(f'Floor Division: {x // y}')
    print(f'Exponent: {x ** y}')
    print(f'Modulus: {x % y}')


def string_operations():
    name = "John Doe"  # string
    print(f'name: {name}')

    # Case Conversions
    upper_name = name.upper()
    print(f'Upper name: {upper_name}')
    lower_name = name.lower()
    print(f'Lower name: {lower_name}')
    title_name = name.title()
    print(f'Title name: {title_name}')
    capital_name = name.capitalize()  # First letter capital
    print(f'Capital name: {capital_name}')
    swapped_case_name = title_name.swapcase()
    print(f'Swapped case name: {swapped_case_name}')

    # Trimming
    strip_name = name.strip()  # Remove leading/trailing spaces
    print(f'Strip name: {strip_name}')
    left_strip_name = name.lstrip()
    print(f'Left strip name: {left_strip_name}')
    right_strip_name = name.rstrip()
    print(f'Right strip name: {right_strip_name}')

    # Searching
    find_doe = name.find('Doe')  # Find index
    print(f'Find doe: {find_doe}')
    right_find_doe = name.rfind('Doe')  # Find index from the right
    print(f'Right find doe: {right_find_doe}')
    find_strict_doe = name.index('Doe')  # Error if not found
    print(f'Find strict doe: {find_strict_doe}')
    count_o = name.count('o')  # Count occurrences
    print(f'Count o: {count_o}')

    # Replacing
    replaced_name = name.replace("John", "Jane")
    print(f'Replaced name: {replaced_name}')

    # Checking
    name_starts_with_j: bool = name.startswith('J')  # bool
    print(f'Name starts with J: {name_starts_with_j}')
    name_ends_with_e = name.endswith('e')
    print(f'Name ends with E: {name_ends_with_e}')
    is_name_alphabetic_name = name.isalpha()
    print(f'Name alphabetic name: {is_name_alphabetic_name}')
    is_name_digit = name.isdigit()
    print(f'Name digit: {is_name_digit}')
    is_name_alphanumeric = name.isalnum()
    print(f'Name alphanumeric: {is_name_alphanumeric}')
    is_name_space = name.isspace()  # Is it whitespace only
    print(f'Name space: {is_name_space}')
    is_name_title_cased = name.istitle()
    print(f'Name title cased: {is_name_title_cased}')

    # Splitting
    split_name_space: list[str] = name.split()
    print(f'Split name space: {split_name_space}')
    custom_split_name = name.split('o')
    print(f'Custom split name: {custom_split_name}')
    split_right_name = name.rsplit('o', 1)
    print(f'Split right name: {split_right_name}')

    # Joining
    names: list[str] = ["John", "Doe"]
    print(f'Names: {names}')
    joined_name: str = " ".join(names)  # Join into string
    print(f'Joined name: {joined_name}')

    # Formatting
    formatted_line = "{} {}".format(name[1], name[0])
    print(f'Formatted line: {formatted_line}')
    named_formatted_line = "First Name: {fname}, Last Name: {lname}".format(fname="John", lname="Doe")
    print(f'Named formatted line: {named_formatted_line}')
    f_string_line = f"Full Name: {formatted_line}"
    print(f'Full Name: {f_string_line}')

    # Slicing
    slice_start_to_index = upper_name[:3]
    print(f'Slicing start to_index: {slice_start_to_index}')
    slice_end_to_index = upper_name[3:]
    print(f'Slicing end to_index: {slice_end_to_index}')
    slice_reverse = upper_name[::-1]
    print(f'Slicing reverse: {slice_reverse}')
    slice_stepping = upper_name[::2]
    print(f'Sliced stepping every 2 chars: {slice_stepping}')

    # Encode & Decode
    encoded_name = name.encode()
    print(f'Encoded name: {encoded_name}')
    decoded_name = encoded_name.decode()
    print(f'Decoded name: {decoded_name}')

    # Partition
    partition_name = name.partition("Doe")  # Split into 3 parts using the separator
    right_partition_name = name.rpartition("o")
    print(partition_name)
    print(right_partition_name)

    # Padding
    padded_numeric_string = "23".zfill(5)
    print(padded_numeric_string)

def data_structures():
    print("List:")

    int_list: list[int] = [1, 2, 3, 4]
    print(f"Init list: {int_list}")
    print(f"List Count: {len(int_list)}")
    sliced_list = int_list[0:2]
    print(f"Sliced List: {sliced_list}")
    int_list.append(5)
    print(f"Appended: {int_list}")
    int_list.extend([6 ,7])
    print(f"Extended: {int_list}")
    int_list.insert(1, 10)
    print(f"Inserted: {int_list}")
    popped_element = int_list.pop()
    print(f"Popped element: {popped_element}")
    print(f"List after pop: {int_list}")
    popped_element_index = int_list.index(2)
    print(f"Popped element index: {popped_element_index}")
    print(f"List after index pop: {int_list}")
    int_list.remove(10)
    print(f"Removed 10: {int_list}")
    copy_int_list = int_list.copy()
    print(f"Copied list: {copy_int_list}")
    int_list.reverse()
    print(f"Reversed list: {int_list}")
    int_list.sort()
    print(f"Sorted list: {int_list}")
    sorted_int_list = sorted(copy_int_list)
    print(f"Sorted list: {sorted_int_list}")

    # List Comprehension (Square Braces)
    int_sq_list = [x*x for x in range(5)]
    print(f'Square list: {int_sq_list}')
    int_evens_list = [x for x in range(10) if x%2 == 0]
    print(f'Even list: {int_evens_list}')

    # Tuples (Round Braces)
    tuple_int = (1, 2, 3)
    print(f'Tuple init: {tuple_int}')
    tuple_element = tuple_int[0]
    print(f'Tuple element: {tuple_element}')
    print(f'Tuple element count: {tuple_int.count(2)}')
    print(f'Tuple element index: {tuple_int.index(3)}')
    t1, t2, t3 = tuple_int
    print(f'Tuple Unpacked: t1: {t1}, t2: {t2}, t3: {t3}')

    # Sets (Curley Braces)
    set_int = {1, 2, 3}
    print(f'Set: {set_int}')
    set_int.add(4)
    print(f'Set after .add(4): {set_int}')
    set_int.update([5, 6])
    print(f'Set after .update([5, 6]): {set_int}')
    set_int.remove(2)
    print(f'Set after .remove(2): {set_int}')
    set_int.discard(10) # Safe Remove
    print(f'Set after .discard(10): {set_int}')
    union_set_int: set[int] = set_int.union({2, 7})
    print(f'New set after .union({{2, 7}}): {union_set_int}')
    intersection_set_int = set_int.intersection({1, 2, 4, 9})
    print(f'Intersection set after .intersection({{1, 2, 4, 9}}): {intersection_set_int}')
    difference_set_int = set_int.difference({2, 4})
    print(f'Difference set after .difference({{2, 4}}): {difference_set_int}')
    symmetric_diff_set_int = set_int.symmetric_difference({2, 3})
    print(f'Symmetric Difference set after .symmetric_difference({{2, 3}}): {symmetric_diff_set_int}')

    # Set Comprehension
    square_sets: set[int] = {x*x for x in range(5)}
    print(f'Square sets: {square_sets}')

    # Dictionaries
    dict_john: dict[str, str | int] = { "name": "John", "age": 30 }
    name_from_dict = dict_john["name"]
    print(f'Name from dict using dict_john["name"]: {name_from_dict}')
    age_from_dict = dict_john.get("age")
    print(f'Age from dict_john.get("age"): {age_from_dict}')
    dict_john["city"] = "Oklahoma" # Add key
    print(f'Add key using dict_john["city"]: {dict_john["city"]}')
    dict_john.update({ "age": 26 })
    print(f'Update key using dict_john.update({{ "age": 26 }}): {dict_john["age"]}')
    dict_keys = dict_john.keys()
    print(f'Dict keys using .keys(): {dict_keys}, type(dict_keys): {type(dict_keys)}')
    dict_values = dict_john.values()
    print(f'Dict values using .values(): {dict_values}, type(dict_values): {type(dict_values)}')
    dict_items = dict_john.items()
    print(f'Dict values using .items(): {dict_items}, type(dict_items): {type(dict_items)}')
    popped_dict_item = dict_john.pop("city")
    print(f'Popped dict item using .pop("city"): {popped_dict_item}')
    popped_last_item = dict_john.popitem()
    print(f'Popped last dict item using .popitem(): {popped_last_item}')
    copy_dict = dict_john.copy()
    print(f'Copied dict item using .copy(): {copy_dict}')

    # Dictionary Comprehension
    squares_dict = { x: x*x for x in range(5) }
    print(f'Squares dict: {squares_dict}')

def control_flow():
    # Conditionals
    x = 10
    msg: str
    if x > 5:
        msg = "Greater than 5"
    elif x == 5:
        msg = "Equals to 5"
    else:
        msg = "Smaller than 5"

    status = "adult" if x >= 18 else "juvenile"

    # Loops
    for i in range(5):
        print(f"for {i}")

    for item in ["a", "b", "c"]:
        print(f'List iteration: {item}')

    count = 0
    while count < 3:
        print(f'While: {count}')
        count += 1

    for i in range(10):
        if i == 2:
            print('continue')
            continue
        if i == 5:
            print('break')
            break
        print(f'Pass: {i}')
        pass # It functions as a placeholder where a statement is syntactically required but no action is intended or defined yet.

    for i in range(5):
        print(f'Loop-else: {i}')
    else:
        print('Loop-else Complete')











