digit_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def unscramble_codes():
    scrambled_codes = read_codes()
    calibration_value = 0
    for code in scrambled_codes.splitlines():

        if len(code) < 3:
            calibration_value += only_digit_code(code)

        else:
            calibration_value += string_and_digit_code(code)

    return calibration_value


def string_and_digit_code(code):
    digits = []
    temp_str = ""
    for x in code:
        if x.isdigit():
            digits.append(x)
            temp_str = ""
        else:
            temp_str = temp_str + x
            for number in digit_strings:
                if number in temp_str:
                    digits.append(str(digit_strings.index(number) + 1))
                    temp_str = "" + temp_str[-1]

    return int(digits[0] + digits[-1])


def only_digit_code(code):
    digits = [x for x in [*code] if x.isdigit()]
    return int(digits[0] + digits[-1])


def read_codes():
    return open("scrambled_launch_codes.txt",'r').read()


if __name__ == "__main__":
    print(unscramble_codes(test_input))
    print('Execution Complete')
