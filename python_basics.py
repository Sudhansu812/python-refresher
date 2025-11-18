def basic_operations():
    # Printing
    print('Hello World')

    # Variables & data types
    x: int = 10  # int
    y: float = 20.3  # float

    # Complex Numbers
    comp: complex = 4 + 5j

    # Boolean
    flag: bool = False

    # None Type
    nothing: None = None

    # Type Casting
    str_to_int: int = int("124")
    str_to_float: float = float("124.12")
    int_to_str: str = str(1252)

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

    # Case Conversions
    upper_name = name.upper()
    lower_name = name.lower()
    title_name = name.title()
    capital_name = name.capitalize()  # First letter capital
    swapped_case_name = title_name.swapcase()

    # Trimming
    strip_name = name.strip()  # Remove leading/trailing spaces
    left_strip_name = name.lstrip()
    right_strip_name = name.rstrip()

    # Searching
    find_doe = name.find('Doe')  # Find index
    right_find_doe = name.rfind('Doe')  # Find index from the right
    find_strict_doe = name.index('Doe')  # Error if not found
    count_o = name.count('o')  # Count occurrences

    # Replacing
    replaced_name = name.replace("John", "Jane")

    # Checking
    name_starts_with_j: bool = name.startswith('J')  # bool
    name_ends_with_e = name.endswith('e')
    is_name_alphabetic_name = name.isalpha()
    is_name_digit = name.isdigit()
    is_name_alphanumeric = name.isalnum()
    is_name_space = name.isspace()  # Is it whitespace only
    is_name_title_cased = name.istitle()

    # Splitting
    split_name_space: list[str] = name.split()
    custom_split_name = name.split('o')
    split_right_name = name.rsplit('o', 1)

    # Joining
    names: list[str] = ["John", "Doe"]
    joined_name: str = " ".join(names)  # Join into string

    # Formatting
    formatted_line = "{} {}".format(name[1], name[0])
    named_formatted_line = "First Name: {fname}, Last Name: {lname}".format(fname="John", lname="Doe")
    f_string_line = f"Full Name: {formatted_line}"

    # Slicing
    slice_start_to_index = upper_name[:3]
    slice_end_to_index = upper_name[3:]
    slice_reverse = upper_name[::-1]
    slice_stepping = upper_name[::2]

    # Encode & Decode
    encoded_name = name.encode()
    decoded_name = encoded_name.decode()

    # Partition
    partition_name = name.partition("Doe")  # Split into 3 parts using the separator
    right_partition_name = name.rpartition("o")
    print(partition_name)
    print(right_partition_name)

    # Padding
    padded_numeric_string = "23".zfill(5)
    print(padded_numeric_string)