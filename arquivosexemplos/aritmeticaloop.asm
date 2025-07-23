addi s0, zero, 3
addi s1, zero, 5
addi s2, zero, 2
addi s3, zero, 1
nop

add t0, s0, s1

nop
nop

add t1, s2, s3
nop
nop
nop

sub s4, t0, t1
addi t0, zero, 1
addi s3, zero, 0
addi t1, zero, 4
nop
nop
nop

loop:
 bge t0, t1, END
 nop
 nop
 nop
 add s3, s3, t0
 nop
 addi t0, t0, 1
 nop
 nop
 j loop
 nop
END:

