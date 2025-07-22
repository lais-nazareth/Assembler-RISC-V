addi a0, x0, 7       
addi a1, x0, 6      

jal ra, multiplica
nop                  

add t0, a0, x0       

multiplica:
    mul a0, a0, a1      
    
    jalr x0, ra, 0
    nop