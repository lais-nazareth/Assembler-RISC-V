addi s0, zero, 3
addi s1, zero, 5
addi s2, zero, 2
addi s3, zero, 1

add t0, s0, s1
add t1, s2, s3
sub s4, t0, t1

addi t0, zero, 1
addi s3, zero, 0
addi t1, zero, 4
loop:
 bge t0, t1, END
 add s3, s3, t0
 addi t0, t0, 1
 j loop
END: