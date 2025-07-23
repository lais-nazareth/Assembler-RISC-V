addi a0, x0, 7       
addi a1, x0, 6      

jal ra, multiplica
nop                  
nop
nop

add t0, a0, x0       

multiplica:
    mul a0, a0, a1   
    nop
    nop
    nop   
    
    nop