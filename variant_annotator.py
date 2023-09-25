import argparse
import requests
import json
import logging

def main():
    parser = argparse.ArgumentParser(description='Variant annotation command line utility')
    parser.add_argument('-input_file', type=str, help='Input file containing list of dbSNP RSIDs')
    parser.add_argument('-output_file', type=str, help='Output file containing annotations')
    parser.add_argument('--species', type=str, help='Optional species name/alias, default=human', required=False, default='human')
    parser.add_argument("--log", help="Optional logging level. Example --log debug, default=warning", default='warning')

    args = parser.parse_args()

    logging.basicConfig(level=args.log.upper())

    with open(args.input_file) as f:
        rsids = f.readlines()
    rsids = [x.strip() for x in rsids]

    # Annotate the variants using the Ensembl API
    annotations = variant_tools.annotate(rsids)

    with open(args.output_file, 'w') as f:
        f.write('start\tend\tmost_severe_consequence\tgene_symbols\n')
        for annotation in annotations:
            if annotation is not None:
                start = annotation['start']
                end = annotation['end']
                most_severe_consequence = annotation['most_severe_consequence']
                gene_symbols = list(set([x['gene_symbol'] for x in annotation['transcript_consequences'] if 'gene_symbol' in x]))
                gene_symbols_str = ','.join(gene_symbols)
                f.write(f'{start}\t{end}\t{most_severe_consequence}\t{gene_symbols_str}\n')
            else:
                f.write(f'\n') #blank line for missing data/404

        f.close()

if __name__ == '__main__':
    main()
