import unittest

import variant_annotator
from unittest import mock

class TestVariantAnnotation(unittest.TestCase):

    def test_get_variant_annotation(self):
        self.assertEqual(variant_annotator.get_variant_annotation('homo_sapiens', 'rs699'), (230710048, 230710048, 'missense_variant', ['AGT']))
        self.assertIsNone(variant_annotator.get_variant_annotation('homo_sapiens', 'rsid_missing'))

    def test_main(self):
        with mock.patch('argparse.ArgumentParser') as mock_parser, \
            mock.patch('requests.get') as mock_get:
            mock_parser.return_value.parse_args.return_value = mock.Mock(input_file='test_input.txt', output_file='test_output.txt', species='homo_sapiens')
            mock_get.return_value.ok = True
            mock_get.return_value.content = b'[{"start": 123, "end": 456, "most_severe_consequence": "missense_variant", "transcript_consequences": [{"gene_symbol": "GENE1"}]}]'
            variant_annotator.main()

            # Check that the output file contains the expected annotations
            with open('test_output.txt') as f:
                output = f.read()
                expected_output = 'start\tend\tmost_severe_consequence\tgene_symbols\n123\t456\tmissense_variant\tGENE1\n'
                self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
