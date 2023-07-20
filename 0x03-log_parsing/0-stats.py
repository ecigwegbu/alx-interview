#!/usr/bin/python3
"""
0. Log Parsing: Write a script that reads stdin line by line and
computes metrics
"""
from datetime import datetime
import shlex
from time import sleep


def process_output(total_size, status_codes, result):
    """Prints an output header and the result document"""
    print("File size: {}".format(total_size), flush=True)
    for code in status_codes:
        if result[code]:
            print("{}: {}".format(code, result[code]), flush=True)


def process_line(line, total_size, status_codes, result):
    """Check if line is valid; if it is parse and populate result document"""
    # global total_size
    # print("processing line...")
    # print_line_tokens(line)
    if not line:
        return
    tokens = shlex.split(line)
    try:
        code = tokens[-2]
        file_size = tokens[-1]
        assert code in status_codes
        file_size = int(file_size)
    except Exception:
        print("minor exception $$$$$$$$$$$$$$")
        return
    result[code] += 1
    total_size += file_size
    # print("Code: ", code, "\tfile_size: ", file_size, "\ttotal size:",
    # total_size)


def print_line_tokens(line):
    """Print the tokens entered in a line"""
    print("Printing line tokens...")
    tokens = shlex.split(line)
    if tokens:
        print("Tokens:")
        for i in range(len(tokens)):
            print(i, tokens[i])


def main():
    """Entry point for program"""
    # initialise variables:
    total_size = 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    result = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
              "405": 0, "500": 0}

    while True:
        lines = 0
        try:
            while lines < 10:
                line = input()
                process_line(line, total_size, status_codes, result)
                lines += 1
        except KeyboardInterrupt:
            process_output(total_size, status_codes, result)
            print(flush=True)
            exit(0)
        except EOFError:
            continue
        process_output(total_size, status_codes, result)


if __name__ == "__main__":
    main()
