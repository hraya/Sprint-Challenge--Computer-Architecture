# Code to test the ALU Operations of the Sprint Challenge
#
# Expected output:
# 30
# 22
# 23
# 184
# 2

10000010 # LDI R0 10
00000000
00001010
10000010 # LDI R1,20
00000001
00010100
10101011 # XOR  R0, R1
00000000
00000001
01000111 # PRN R0
00000000
10000010 # LDI R1, 23
00000001
00010111
10101000 # AND  R0, R1
00000000
00000001
01000111 # PRN R0
00000000
10000010 # LDI R1, 22
00000001
00010111
10101010 # OR R0, R1
00000000
00000001
01000111 # PRN R0
00000000
10000010 # LDI R1, 3
00000001
00000011
10101100 # SHL R0, R1
00000000
00000001
01000111 # PRN R0
00000000
10000010 # LDI R0, 3
00000000
00010100
10101101 # SHR R0, R1
00000000
00000001
01000111 # PRN R0
00000000
00000001 # HLT