# variant_annotator.py

### Description:

This script accepts a file with a list of dbSNP RSIDs and outputs a TSV file with annotations. Using the [variant-tools](https://vatlab.github.io/vat-docs/) package it queries the Ensembl API using this endpoint https://rest.ensembl.org/documentation/info/vep_id_get and returns the following fields: start, end, most_severe_consequence and a unique list of genes (pulled from the gene_symbol value in the list of transcript_consequences). If multiple variants are returned, it uses the first one. If a RSID is not found in Ensembl it returns a blank line.

### Requirements:
python version 3.10

`variant-tools` package: an integrated annotation and analysis package for next-generation sequencing data. You can install it using pip with the following command:

```
pip install variant-tools
```

see [https://pypi.org/project/variant-tools/](https://pypi.org/project/variant-tools/)

Alternatively, if you are using a conda environment, you can install variant-tools with the following command:

```
conda install variant_tools -c bioconda -c conda-forge
```


### Usage:
```bash

variant_annotator.py [-h] [-input_file INPUT_FILE] [-output_file OUTPUT_FILE]
                             [--species SPECIES] [--log LOG]

Variant annotation command line utility

options:
  -h, --help            show this help message and exit
  -input_file INPUT_FILE
                        Input file containing list of dbSNP RSIDs
  -output_file OUTPUT_FILE
                        Output file containing annotations
  --species SPECIES     Optional species name/alias, default=human
  --log LOG             Optional provide logging level. Example --log debug, default=warning

```

### Eaxmple usage:
```bash

python variant_annotator.py -input_file=input_bto.txt -output_file=output_bto.txt

```

### Unit tests for the main functionality
```bash

python -m unittest  variant_annotator_test.TestVariantAnnotation

```

### Running in a github codespace:
Open [pault-tech/bto_variant_annotator](https://github.com/pault-tech/bto_variant_annotator), then click the `Code` button, under `Codespaces` click, `Create codespace on main` to launch a new codespace instance.

