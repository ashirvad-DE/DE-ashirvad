# Fixed Width Parser

This project contains a script to parse fixed-width files and generate delimited files (CSV).

## Usage

To run the script, you need to provide three arguments: the spec file, the input file, and the output file.

```bash
python parse_fixed_width.py spec.txt input.txt output.csv

docker build -t fixed-width-parser .

docker run --rm -v $(pwd):/app fixed-width-parser
