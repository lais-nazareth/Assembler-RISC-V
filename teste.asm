FOR: bge s2, t1, ENDFOR
 addi t0, t1, 10

ENDFOR: 
 add t0, t1, t2

jal x1, FOR
bge x0, t1, ENDFOR