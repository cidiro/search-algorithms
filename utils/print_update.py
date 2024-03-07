import sys


def print_update(message):
    lines = message.splitlines()
    num_lines = len(lines)

    if hasattr(print_update, 'first_call'):
        if not print_update.first_call:
            sys.stdout.write(f"\033[{num_lines}A")
    else:
        print_update.first_call = True

    for line in lines:
        sys.stdout.write('\r\033[K' + line + '\n')

    sys.stdout.flush()
    print_update.first_call = False
