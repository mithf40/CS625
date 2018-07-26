# Reading the qr code directly
hex_raw = """
01011011000100110
0110001101100111011
011010011010000101110
01100001001100000011001
1011001010011011101100011
011000110110011001101101011
00100001101100011010000110100
0011011101101101001100000110010
0011000010110011100110110011001
10001100110011011100110100011
000010110011101100100001101
0001100100011001010011001
10110000000101000010101
010101010101010101010
1010101010101010101
01010101010000000
""".replace('\n','')

# convert the hex_code to a binary value
hex_raw_value = int(hex_raw,2)

# create a string of the same length to xor with
xor_value = int(('10'*(len(hex_raw)/2))[0:len(hex_raw)],2)

# perform XOR and convert back to binary string
hex_code = str(bin(hex_raw_value ^ xor_value))[2:]

out_string = ""
i = 2 # skip the 2 bit header

# add the first character (guessing that bit 6 is set)
bit6IsSet = True
out_string = out_string + chr(int(hex_code[i:i + (7 if bit6IsSet else 6)], 2))
i = i + (7 if bit6IsSet else 6)

# the rest of the characters are 8 bit
while i < len(hex_code)-8:
    out_string = out_string + chr(int(hex_code[i:i+8], 2))
    i = i + 8

print(out_string)
