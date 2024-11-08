#!/usr/bin/env python3
# Author ID: avirk18

def read_file_string(file_name):
    f = open(file_name, 'r')
    read_data = f.read()
    return read_data

def read_file_list(file_name):
    f = open(file_name, 'r')
    list_data = list(f)
    read_list = [line.strip() for line in list_data]
    return read_list


def append_file_string(file_name, string_of_lines):
    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()
    return
    # Takes two strings, appends the string to the end of the file

def write_file_list(file_name, list_of_lines):
    f = open(file_name, 'w')
    for item in list_of_lines:
        f.write(item + '\n')
    f.close()
    return
    # Takes a string and list, writes all items from list to file where each item is one line

def copy_file_add_line_numbers(file_name_read, file_name_write):
    f = open(file_name_read, 'r')
    read_file = f.readlines()
    f.close()

    f = open(file_name_write, 'w')
    line_number = 1
    for line in read_file:
        f.write(f"{line_number}:{line}")
        line_number = line_number + 1
    f.close()
    return
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))   
