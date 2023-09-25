import argparse
import requests
import json
import logging

def get_variant_annotation(species, variant_id):
    #Uses the vep (variant effect predictor) endpoint
    url = f"https://rest.ensembl.org/vep/{species}/id/{variant_id}?content-type=application/json"
    response = requests.get(url)
    if response.ok:
        data = json.loads(response.content)
        logging.debug(data)
        # To keep it simple, if multiple variants are returned just use the first one.
        start = data[0]['start']
        end = data[0]['end']
        most_severe_consequence = data[0]['most_severe_consequence']
        # a unique list of genes (pull from the `gene_symbol` value in the list of `transcript_consequences`)
        logging.debug(data[0]['transcript_consequences'])
        gene_symbols = list(set([x['gene_symbol'] for x in data[0]['transcript_consequences'] if 'gene_symbol' in x]))
        return start, end, most_severe_consequence, gene_symbols
    else:
        return None

def main():
    parser = argparse.ArgumentParser(description='Variant annotation command line utility')
    parser.add_argument('--input_file', type=str, help='Input file containing list of dbSNP RSIDs', required=True)
    parser.add_argument('--output_file', type=str, help='Output file containing annotations', required=True)
    parser.add_argument('--species', type=str, help='Optional species name/alias, default=human', required=False, default='human')
    parser.add_argument("--log", help="Optional logging level. Example --log debug, default=warning", default='warning')

    args = parser.parse_args()

    logging.basicConfig(level=args.log.upper())

    with open(args.input_file) as f:
        rsids = f.readlines()
    rsids = [x.strip() for x in rsids]


    with open(args.output_file, 'w') as f:
        f.write('start\tend\tmost_severe_consequence\tgene_symbols\n')
        for rsid in rsids:
            annotation = get_variant_annotation(args.species, rsid)
            if annotation is not None:
                start, end, most_severe_consequence, gene_symbols = annotation
                gene_symbols_str = ','.join(gene_symbols)
                f.write(f'{start}\t{end}\t{most_severe_consequence}\t{gene_symbols_str}\n')
            else:
                f.write(f'\n') #blank line for missing data/404

        f.close()

if __name__ == '__main__':
    main()
