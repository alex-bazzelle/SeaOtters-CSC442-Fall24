"""=== Imports ==="""
import sys  # System-specific parameters and functions
import argparse  # Parser for command-line options, arguments and sub-commands
import os  # Miscellaneous operating system interfaces
import math

"""=== Constants ==="""
SENTINEL = bytearray([0x00, 0xff, 0x00, 0x00, 0xff, 0x00])  # Sentinel value

"""=== Methods ==="""


def calculate_optimal_interval(wrapper_size, hidden_size, offset, sentinel_size=6):
    return math.floor(wrapper_size - offset) // (hidden_size + sentinel_size)  # Calculate optimal interval


def store_byte_method(wrapper, hidden, offset, interval):  # Store data using byte method
    i = 0  # Initialize index for hidden data
    while i < len(hidden):  # Loop through hidden data
        wrapper[offset] = hidden[i]  # Store byte from hidden data
        offset += interval  # Move to next offset
        i += 1  # Move to next byte
    for byte in SENTINEL:  # Loop through sentinel
        wrapper[offset] = byte  # Store byte from sentinel
        offset += interval  # Move to next offset
    return wrapper  # Return wrapper with hidden data


def retrieve_byte_method(wrapper, offset, interval):  # Retrieve data using byte method
    hidden = bytearray()  # Initialize hidden data
    i = 0  # Initialize index for sentinel
    while offset < len(wrapper):  # Loop through wrapper
        byte = wrapper[offset]  # Get byte from wrapper

        # Debug: Print bytes being read (remove in production)
        # print(f"Reading byte at offset {offset}: {byte:02x}")
        # Debug: Sentinal bytes (remove in production)
        # print(f"Sentinel bytes: {SENTINEL}")

        # Check for sentinel match
        if byte == SENTINEL[i]:  # Check if byte matches sentinel
            i += 1  # Move to next byte in sentinel
            if i == len(SENTINEL):  # Check if sentinel fully matched
                # print("Sentinel detected. Ending retrieval.")  # Print message
                return hidden  # Sentinel fully matched, return data
        else:  # Byte does not match sentinel
            if i > 0:  # Check if partial match
                hidden.extend(SENTINEL[:i])  # Add partial match to hidden data
                i = 0  # Reset sentinel index
            hidden.append(byte)  # Add byte to hidden data
        offset += interval  # Move to next offset
    print("No sentinel found. Reached end of file.")  # Print message
    return hidden  # Return hidden data


def store_bit_method(wrapper, hidden, offset):  # Store data using bit method
    for byte in hidden:  # Loop through hidden data
        for i in range(8):  # Loop through bits in byte
            wrapper[offset] &= 0b11111110  # Clear LSB (Least Significant Bit)
            wrapper[offset] |= (byte & 0b10000000) >> 7  # Set LSB
            byte = (byte << 1) & 0xFF  # Shift byte left, restrict to 8 bits
            offset += 1  # Move to next offset
    for byte in SENTINEL:  # Loop through sentinel
        for i in range(8):  # Loop through bits in byte
            wrapper[offset] &= 0b11111110  # Clear LSB
            wrapper[offset] |= (byte & 0b10000000) >> 7  # Set LSB
            byte = (byte << 1) & 0xFF  # Shift byte left, restrict to 8 bits
            offset += 1  # Move to next offset
    return wrapper  # Return wrapper with hidden data


def retrieve_bit_method(wrapper, offset, interval):  # Retrieve data using bit method
    hidden = bytearray()  # Initialize hidden data
    sentinel_index = 0  # Initialize sentinel index
    while offset < len(wrapper):  # Loop through wrapper
        byte = 0  # Initialize byte

        # Debug: Print bytes being read (remove in production)
        # print(f"Reading byte at offset {offset}: {byte:02x}")
        # Debug: Sentinal bytes (remove in production)
        # print(f"Sentinel bytes: {SENTINEL}")

        for i in range(8):  # Loop through bits in byte
            byte |= (wrapper[offset] & 0b00000001)  # Get LSB
            if i < 7:  # Check if not final bit  
                byte <<= 1  # Shift left
                offset += interval  # Move to next bit
        
        offset += interval  # Move to next byte
        hidden.append(byte)  # Add byte to hidden data

        if hidden[-len(SENTINEL):] == SENTINEL:  # Check if sentinel detected
            return hidden[:-len(SENTINEL)]  # Return without sentinel
       


    return hidden  # Can never run as without hitting sentinal it would break entirely


def main():  # Main method
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Steganography Program - Hide and Retrieve Data")  # Create parser
    parser.add_argument('-s', action='store_true', help="Store data")  # Store mode
    parser.add_argument('-r', action='store_true', help="Retrieve data")  # Retrieve mode
    parser.add_argument('-b', action='store_true', help="Bit method")  # Bit method
    parser.add_argument('-B', action='store_true', help="Byte method")  # Byte method
    parser.add_argument('-o', type=int, default=0, help="Offset value")  # Offset value
    parser.add_argument('-i', type=int, default=1, help="Interval value")  # Interval value
    parser.add_argument('-w', required=True, help="Wrapper file")  # Wrapper file
    parser.add_argument('-hf', help="Hidden file (for storing)")  # Changed from -h to -hf

    args = parser.parse_args()  # Parse arguments

    try:  # Read wrapper file
        with open(args.w, 'rb') as f:  # Open wrapper file in binary mode
            wrapper = bytearray(f.read())  # Read wrapper file
    except FileNotFoundError:  # Handle file not found error
        print("Error: Wrapper file not found.")  # Print error message
        sys.exit(1)  # Exit program

    if args.s and args.B and args.i is None:
        # If interval is not provided, calculate it
        wrapper_size = os.path.getsize(args.w)  # Get size of wrapper file
        hidden_size = os.path.getsize(args.hf)  # Get size of hidden file
        args.i = calculate_optimal_interval(wrapper_size, hidden_size, args.o)  # Calculate optimal interval

    if args.s:  # Store mode
        if args.hf is None:  # Check if hidden file provided
            print("Error: Hidden file must be provided in store mode.")  # Print error message
            sys.exit(1)  # Exit program
        try:  # Read hidden file
            with open(args.hf, 'rb') as f:  # Changed from args.h to args.hf
                hidden = bytearray(f.read())  # Read hidden file
        except FileNotFoundError:  # Handle file not found error
            print("Error: Hidden file not found.")  # Print error message
            sys.exit(1)  # Exit program

        if args.B:  # Byte method
            wrapper = store_byte_method(wrapper, hidden, args.o, args.i)  # Store data using byte method
        elif args.b:  # Bit method
            wrapper = store_bit_method(wrapper, hidden, args.o)  # Store data using bit method
        else:
            print("Error: Specify either -b (bit) or -B (byte) mode.")  # Print error message
            sys.exit(1)  # Exit program

        sys.stdout.buffer.write(wrapper)  # Write wrapper to standard output

    elif args.r:  # Retrieve mode
        if args.B:  # Byte method
            hidden = retrieve_byte_method(wrapper, args.o, args.i)  # Retrieve data using byte method
        elif args.b:  # Bit method
            hidden = retrieve_bit_method(wrapper, args.o, args.i)  # Retrieve data using bit method
        else:  # No method specified
            print("Error: Specify either -b (bit) or -B (byte) mode.")  # Print error message
            sys.exit(1)  # Exit program

        sys.stdout.buffer.write(hidden)  # Write hidden data to standard output
        sys.stdout.flush() 
    else:  # No mode specified
        print("Error: Specify either -s (store) or -r (retrieve) mode.")  # Print error message
        sys.exit(1)  # Exit program


"""=== Execution ==="""
if __name__ == "__main__":
    main()  # Run the program
