if __name__ == '__main__':
    max_len = 100
    general_string = ""
    attempts = 1

    while len(general_string) <= max_len:
        # we need to collect data about the user.
        print('Print a random string containing 0 or 1:')
        # We will ask them to press 0's and 1's on the keyboard in an unpredictable order.
        usr_input = input()
        # All other characters should not be taken into account
        # (in case the user makes a mistake and presses "2" instead of "1", for example).
        tmp_filter_usr_input = ""
        for c in usr_input:
            if c in ['0', '1']:
                tmp_filter_usr_input += c

        usr_input = tmp_filter_usr_input

        general_string += usr_input
        print(f"Current data length is {len(general_string)}, {max_len - len(general_string)} symbols left")
        if len(general_string) >= max_len:
            print("Final data string:")
            print(general_string[0:100])

        attempts += 1


