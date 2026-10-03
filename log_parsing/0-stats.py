#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics.
"""

import re
import sys


def print_stats(total_size, status_codes):
    """
    Prints accumulated statistics.

    Args:
        total_size (int): Total sum of file sizes.
        status_codes (dict): Status codes and their respective counts.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


if __name__ == "__main__":
    log_regex = re.compile(
        r'^\S+\s*-\s*\[.*?\]\s*"GET /projects/260 HTTP/1\.1"\s*(\S+)\s+(\S+)$'
    )
    total_size = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            line = line.strip()
            match = log_regex.match(line)
            if match:
                code, size = match.group(1), match.group(2)
                try:
                    total_size += int(size)
                except ValueError:
                    pass
                if code in status_codes:
                    status_codes[code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
