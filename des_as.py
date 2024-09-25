input_bits = [
    1, 0, 1, 1, 0, 0, 1, 1,
    0, 0, 0, 0, 1, 1, 1, 1,
    1, 1, 0, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 0, 1, 1, 0,
    1, 1, 1, 1, 0, 1, 0, 0,
    0, 0, 1, 1, 0, 0, 0, 1,
    0, 1, 0, 1, 1, 1, 1, 1,
    1, 0, 0, 1, 0, 1, 1, 0
]

des_key = [
    0, 0, 1, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 1, 1, 0,
    1, 0, 1, 1, 1, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0,
    1, 1, 1, 1, 1, 1, 0, 0,
    1, 0, 1, 1, 0, 1, 1, 0,
    1, 1, 1, 1, 1, 0, 1, 0,
    1, 1, 1, 1, 1, 1, 1, 0
]

ip_array = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

inverse_permutation = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

expansion_table = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

s1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

s2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]

s3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
]

s4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
]

s5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
]

s6 = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
]

s7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
]

s8 = [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
]

permutation_table = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

pc1_array = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

pc2_array = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

circle_shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def prettyfiArr(arr, col):
  for i in range(0, len(arr), col):
    print(arr[i:i+col])
  print()

def split_array(arr, n):
  ni = n//2
  lpt = arr[:ni]
  rpt = arr[ni:]
  return lpt, rpt

def expand_rpt(rpt):
  expanded_rpt = []
  for i in range(len(expansion_table)):
    expanded_rpt.append(rpt[expansion_table[i] - 1])
  return expanded_rpt

def xor(a, b):
  result = []
  for i in range(len(a)):
    result.append(a[i] ^ b[i])
  return result

def binary_to_deciaml(binary):
  decimal = 0
  for i in range(len(binary)):
    decimal += binary[i] * (2 ** (len(binary) - i - 1))
  return decimal

def s_box(s_input):
  s_box_output = []
  s_box_output2 = []

  s1_input = s_input[:6]
  s2_input = s_input[6:12]
  s3_input = s_input[12:18]
  s4_input = s_input[18:24]
  s5_input = s_input[24:30]
  s6_input = s_input[30:36]
  s7_input = s_input[36:42]
  s8_input = s_input[42:]

  s_box_set = [s1_input, s2_input, s3_input, s4_input, s5_input, s6_input, s7_input, s8_input]
  s_boxes = [s1, s2, s3, s4, s5, s6, s7, s8]

  for i in range(len(s_box_set)):
    row = binary_to_deciaml([s_box_set[i][0], s_box_set[i][5]])
    col = binary_to_deciaml(s_box_set[i][1:5])
    print(f"row : {row} , col: {col}")
    s_box_output.append(s_boxes[i][row][col])

  return s_box_output

def decimal_to_4_bit_binary(decimal):
  binary = bin(decimal)[2:].zfill(4)
  return[int(bit) for bit in binary]

def stitch_s_box_op(s_output):
  out = []
  for i in range(len(s_output)):
    out += decimal_to_4_bit_binary(s_output[i])
  return out

def permutation(s_box_output):
  permutation_output = []
  for i in range(len(permutation_table)):
    permutation_output.append(s_box_output[permutation_table[i] - 1])
  return permutation_output

def pc1(des_key):
  pc1_output = []
  for i in range(len(pc1_array)):
    pc1_output.append(des_key[pc1_array[i] - 1])
  return pc1_output

def left_shift(c, d, round_number):
  shift = circle_shift[round_number]
  c = c[shift:] + c[:shift]
  d = d[shift:] + d[:shift]
  return c, d

def pc2(key):
  pc2_output = []
  for i in range(len(pc2_array)):
    pc2_output.append(key[pc2_array[i] - 1])
  return pc2_output

def lpt_rpt_swap(lpt, rpt):
  return rpt, xor(rpt, lpt)

def swap32(lpt, rpt):
  return rpt + lpt

def inverse_permutation_function(rpt):
  inverse_permutation_output = []
  for i in range(len(inverse_permutation)):
    inverse_permutation_output.append(rpt[inverse_permutation[i] - 1])
  return inverse_permutation_output

initial_permuted_input = []
for i in range(len(ip_array)):
  initial_permuted_input.append(input_bits[ip_array[i] - 1])
len(initial_permuted_input)

prettyfiArr(initial_permuted_input, 8)
print()
print("input")
prettyfiArr(input_bits, 8)

lpt,rpt = split_array(initial_permuted_input, 64)

print("lpt")
prettyfiArr(lpt, 8)
print()
print("rpt")
prettyfiArr(rpt, 8)

# PC1 applied to DES_key 64 bit --> 56 bit key
pc1_key = pc1(des_key)
print("pc1_key")
prettyfiArr(pc1_key, 8)

# 56 bit DES_key split into c, d
c, d =split_array(pc1_key, 56)
print("c")
prettyfiArr(c, 8)
print()
print("d")
prettyfiArr(d, 8)

def DES_round(lpt, rpt, c, d, round):
  expanded_rpt = expand_rpt(rpt)
  print("expanded_rpt")
  prettyfiArr(expanded_rpt, 8)

  shifted_c, shifted_d = left_shift(c, d, round)
  print("shifted_c")
  prettyfiArr(shifted_c, 8)
  print()
  print("shifted_d")
  prettyfiArr(shifted_d, 8)

  PC2_input = shifted_c + shifted_d
  print("PC2_input")
  prettyfiArr(PC2_input, 8)
  print()

  pc2_output = pc2(PC2_input)
  print("pc2_output")
  prettyfiArr(pc2_output, 8)
  print()

  xor_output = xor(expanded_rpt, pc2_output)
  print("xor_output")
  prettyfiArr(xor_output, 8)

  s_box_output = s_box(xor_output)
  print("s_box_output")
  prettyfiArr(s_box_output, 8)

  s_box_output = stitch_s_box_op(s_box_output)
  print("s_box_output")
  prettyfiArr(s_box_output, 8)

  permutation_output = permutation(s_box_output)
  print("permutation_output")
  prettyfiArr(permutation_output, 8)

  new_right = xor(lpt, permutation_output)
  print("new_right")
  prettyfiArr(new_right, 8)

  new_left = rpt
  print("new_left")
  prettyfiArr(new_left, 8)

  return new_left, new_right, shifted_c, shifted_d

for i in range(len(circle_shift)):
  lpt, rpt, c, d = DES_round(lpt, rpt, c, d, i)

swap32_output = swap32(lpt, rpt)
print("swap32_output")
prettyfiArr(swap32_output, 8)

final_output = inverse_permutation_function(swap32_output)
print("cypher_text")
prettyfiArr(final_output, 8)

# Custom number of rounds
for i in range(2):
  lpt, rpt, c, d = DES_round(lpt, rpt, c, d, i)

swap32_output = swap32(lpt, rpt)
print("swap32_output")
prettyfiArr(swap32_output, 8)

final_output = inverse_permutation_function(swap32_output)
print("cypher_text")
prettyfiArr(final_output, 8)