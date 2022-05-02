from hstest.stage_test import *
from hstest.test_case import TestCase

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)

COMBO_LENGTH = 3
MIN_DATA_STR_LEN = 100
INSTRUCTION = 'Print a random string containing 0 or 1'

correct_output = ["000:2,6", "001:13,1", "010:13,22", "011:2,2", "100:6,8", "101:22,3", "110:1,3", "111:2,0"]


class GenRandTest(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase(stdin=["1010101101010",
                                "1010100111001010010101001010100001010001",
                                '01010000100101011010001001000101011101000101010010100101'],
                         attach=[109, correct_output]),
                TestCase(stdin=["1010101101010_some_wrong_symbols",
                                "1010100111001010010101001010100001010001_some_more_wrong_symbols",
                                '01010000100101011010001001000101011101000101010010100101'],
                         attach=[109, correct_output])
                ]

    def check(self, output: str, attach) -> CheckResult:
        correct_len, correct_output = attach
        strings = [s for s in output.split('\n') if s != '']

        if not strings:
            return CheckResult.wrong("The output seems to be empty.")

        instructions = strings[0]

        final_string_index = -(2**COMBO_LENGTH + 1)
        if len(strings) < abs(final_string_index):
            return CheckResult.wrong("Your program is supposed to output at least 9 lines.\n"
                                     "However, there are less than 9 lines.")

        data_string = strings[final_string_index]

        if INSTRUCTION.lower() not in instructions.lower():
            return CheckResult.wrong('Please give instructions to user in the form "{}"'.format(INSTRUCTION))

        if len(data_string) < MIN_DATA_STR_LEN:
            return CheckResult.wrong('Data string \"{}\" is too short, it should have length >={}'.format(data_string,
                                                                                                          MIN_DATA_STR_LEN))
        if len(data_string) != correct_len:
            return CheckResult.wrong(
                "The string \"{}\" of your output is supposed to contain the final data string. \n"
                "However, it contains wrong number of symbols".format(data_string)
            )

        for i in range(2**COMBO_LENGTH):
            tested_string = strings[-i-1].replace(' ', '')
            if tested_string[:3] != correct_output[-i-1][:3]:
                return CheckResult.wrong(
                    "The string \"{}\" of your output is supposed to contain the data for the triad {}".format(
                        strings[-i-1],
                        correct_output[-i-1][:3])
                )
            elif tested_string != correct_output[-i-1]:
                return CheckResult.wrong(
                    "The result \"{}\" does not match with the expected result for triad {}".format(
                        strings[-i - 1][4:],
                        correct_output[-i - 1][:3])
                )

        return CheckResult.correct()


if __name__ == '__main__':
    GenRandTest('predictor.predictor').run_tests()
