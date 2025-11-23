def basic_error_handling():
    try:
        x = 10 / 0
    except ZeroDivisionError as err:
        print(f'Can not divide by zero:: Exception Type: {type(err)}')

def multiple_exception_handling():
    try:
        value = int("abc")
    except (TypeError, ValueError) as verr:
        print(f'Value / Type Error:: type: {type(verr)}')

def catch_all_exception():
    try:
        value = int("abc")
    except Exception as err:
        print(f'Catch All Exception:: Exception Type: {type(err)}')

def try_catch_else():
    try:
        value = int("123")
    except ValueError as verr:
        print(f'Value / Type Error:: type: {type(verr)}')
    else:
        print(f'Converted. Else is executed only if the statements in the try block does nto raise an exception.')

def try_catch_finally():
    try:
        value = int("123g")
    except ValueError as verr:
        print(f'Value / Type Error:: type: {type(verr)}')
    else:
        print(f'Converted.')
    finally:
        print(f'In final block. Finally is executed regardless if the try block raised an exception. Now this also means if your '
              f'program exits on the exception, finally would still be executed (Dont assume any statements after the overall try-except would do the same as a finally).')

class ValueTooSmallError(Exception):
    pass

def custom_exception_handling():
    try:
        raise ValueTooSmallError("Value is too small for processing.")
    except ValueTooSmallError as vts:
        print(f'Custom Error: {str(vts)} :: Type: {type(vts)}')