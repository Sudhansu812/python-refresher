import python_basics as pb
import modules_and_packages as mp
import fileio as fio

class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_msg(msg: str):
    print(f'{BColors.HEADER}{msg}{BColors.ENDC}')

if __name__ == '__main__':
    print_msg('------Basic Operations------')
    pb.basic_operations()

    print_msg('\n------String Operations------')
    pb.string_operations()

    print_msg('\n------Data Structures------')
    pb.data_structures()

    print_msg('\n------Control Flow------')
    pb.control_flow()

    print_msg('\n------Functions------')
    pb.functions()

    print_msg('\n------Built-in Functions------')
    pb.built_in_functions()

    print_msg('\n------Math Library Usages------')
    mp.math_usages()

    print_msg('\n------Random Library Usages------')
    mp.random_usages()

    print_msg('\n------Specific Library Import Usages------')
    mp.specific_import_usages()

    print_msg('\n------JSON Library Usages------')
    mp.json_usages()

    print_msg('\n------OS Library Usages------')
    mp.os_usages()

    print_msg('\n------sys Library Usages------')
    mp.sys_usages()

    print_msg('\n-------File IO------')
    fio.show_all_file_modes()
    fio.write_to_file()
    fio.read_entire_file()
    fio.read_per_line()
    fio.append_to_file()
    fio.write_binary_file()
    fio.read_binary_file()