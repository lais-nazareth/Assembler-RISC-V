addi x5, x0, 5      

addi x6, x0, 0     
nop
nop
nop

loop:
    add x6, x6, x5       

    addi x5, x5, -1      
    nop
    nop
    nop

    bne x5, x0, loop
    nop