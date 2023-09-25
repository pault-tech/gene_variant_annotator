import unittest

import variant_annotator
from unittest import mock

class TestVariantAnnotation(unittest.TestCase):

    def test_main(self):
        with mock.patch('argparse.ArgumentParser') as mock_parser:
            mock_parser.return_value.parse_args.return_value = mock.Mock(input_file='test_input.txt', output_file='test_output.txt', species='homo_sapiens', log='info')
            variant_annotator.main()

            # Check that the output file contains the expected annotations
            with open('test_output.txt') as f:
                output = f.read()
                expected_output = 'start\tend\tmost_severe_consequence\tgene_symbols\n123\t456\tmissense_variant\tGENE1\n'
                self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
