addi s0, zero, 3
nop
nop
nop
nop
nop
addi s1, zero, 5
nop
nop
nop
nop
nop
addi s2, zero, 2
nop
nop
nop
nop
nop
addi s3, zero, 1
nop
nop
nop
nop
nop

add t0, s0, s1
nop
nop
nop
nop
nop
add t1, s2, s3
nop
nop
nop
nop
nop
sub s4, t0, t1
nop
nop
nop
nop
nop

addi t0, zero, 1
nop
nop
nop
nop
nop
addi s3, zero, 0
nop
nop
nop
nop
nop
addi t1, zero, 4
nop
nop
nop
nop
nop
loop:
 bge t0, t1, END
 nop
 nop
 nop
 nop
 nop	
 add s3, s3, t0
 nop
 nop
 nop
 nop
 nop 
 addi t0, t0, 1
 nop
 nop
 nop
 nop
 nop
 j loop
 nop
 nop
 nop
 nop
 nop
END:


