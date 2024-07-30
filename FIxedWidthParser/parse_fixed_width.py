import csv

def parse_fixed_width_file(spec_file, input_file, output_file):
    # Read the spec file to get the field lengths
    with open(spec_file, 'r') as spec:
        field_lengths = [int(length) for length in spec.read().strip().split()]

    # Read the input file and parse the lines based on the field lengths
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Create a CSV writer to write the output file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        for line in lines:
            start = 0
            parsed_line = []
            for length in field_lengths:
                parsed_line.append(line[start:start+length].strip())
                start += length
            writer.writerow(parsed_line)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python parse_fixed_width.py <spec_file> <input_file> <output_file>")
        sys.exit(1)
    
    spec_file = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    
    parse_fixed_width_file(spec_file, input_file, output_file)
