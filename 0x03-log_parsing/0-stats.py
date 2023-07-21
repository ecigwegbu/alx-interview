#!/usr/bin/python3
"""
0. Log Parsing: Write a script that reads stdin line by line and
computes metrics
"""
from datetime import datetime
import shlex
import sys
total_size = 0


def process_output(status_codes, result):
    """Prints an output header and the result document"""
    global total_size
    sys.stdout.write("File size: {}\n".format(total_size))
    for code in status_codes:
        if result[code]:
            sys.stdout.write("{}: {}\n".format(code, result[code]))
    sys.stdout.flush()


def process_line(line, status_codes, result):
    """Check if line is valid; if it is parse and populate result document"""
    global total_size
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
    global total_size
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    result = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
              "405": 0, "500": 0}
    lines = 1

    try:
        while True:
            for line in sys.stdin:
                # sys.stdout.write("Line {}: {}".format(lines, line))
                process_line(line, status_codes, result)
                if lines % 10 == 0:
                    # sys.stdout.write("Num of lines: {}\n".format(lines))
                    process_output(status_codes, result)
                lines += 1
    except KeyboardInterrupt:
        sys.stdout.flush()
        process_output(status_codes, result)
        sys.stdout.flush()
    except EOFError:
        pass


if __name__ == "__main__":
    main()
