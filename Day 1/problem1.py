def unscramble_codes():
    scrambled_codes = read_codes()
    calibration_value = 0
    for code in scrambled_codes.splitlines():

        digits = [x for x in [*code] if x.isdigit()]
        calibration_value += int(digits[0] + digits[-1])

    return calibration_value


def read_codes():
    return open('scrambled_launch_codes.txt','r').read()


if __name__ == "__main__":
    print(unscramble_codes())
    print('Execution Complete')