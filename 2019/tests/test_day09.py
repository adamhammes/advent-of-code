import unittest

from lib import Tape


def run_tape(_in):
    tape = Tape(_in)
    tape.run()
    return tape.output


class TestDay09(unittest.TestCase):
    def test_simple(self):
        _in = [1, 1, 1, 0, 4, 0, 99]
        self.assertEqual([2], run_tape(_in))

    def test_simple_immediate(self):
        _in = [1101, 20, 22, 0, 4, 0, 99]
        self.assertEqual([42], run_tape(_in))

    def test_day_5_examples(self):
        _in = [1002, 4, 3, 4, 33]
        tape = Tape(_in)
        tape.run()
        self.assertEqual(99, tape._read(4))

    def test_example_1(self):
        _in = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]

        tape = Tape(_in)
        tape.run()

        self.assertEqual(_in, run_tape(_in))

    def test_example_2(self):
        _in = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]

        output = run_tape(_in)
        self.assertTrue(len(str(output[-1])) == 16)

    def test_example_3(self):
        _in = [104, 1125899906842624, 99]

        self.assertEqual(1125899906842624, run_tape(_in)[-1])
