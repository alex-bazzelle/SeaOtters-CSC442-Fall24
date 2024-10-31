Commands and Options

Basic Syntax
python Steg.py -[s/r] -[b/B] -o <offset> [-i <interval>] -w <wrapper> [-hf <hidden file>]


- `-s` : Store mode – hides data in the wrapper file
- `-r` : Retrieve mode – extracts hidden data from the wrapper file
- `-b` : Bit method – stores data bit-by-bit in the least significant bits
- `-B` : Byte method – stores data by replacing entire bytes at intervals
- `-o` : Offset – starting point in the wrapper file for storage/retrieval
- `-i` : Interval (only for byte method) – spacing between bytes when storing
- `-w` : Wrapper file – file to store/retrieve data
- `-hf` : Hidden file – file containing data to hide (only required for `-s` mode)

Examples

1. Storing Data (Byte Method)
python Steg.py -s -B -o 1024 -i 8 -w image.bmp -hf hidden.txt > stegged_image.bmp

2. Storing Data (Bit Method)
python Steg.py -s -b -o 1024 -w image.bmp -hf hidden.txt > stegged_image.bmp

3. Retrieving Data (Byte Method)
python Steg.py -r -B -o 1024 -i 8 -w stegged_image.bmp > extracted_data.txt

4. Retrieving Data (Bit Method)
python Steg.py -r -b -o 1024 -w stegged_image.bmp > extracted_data.txt

Commands for the example bmp files
python Steg.py -r -b -o1024 -w stegged-bit.bmp > extracted_bit_message.txt

python Steg.py -r -B -o1024 -i8 -w stegged-byte.bmp > extracted_byte_message_1024_8.txt

python Steg.py -r -B -o1025 -i2 -w stegged-byte.bmp > extracted_byte_message_1025_2.txt