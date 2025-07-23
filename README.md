# Assembler-RISC-V
  Trabalho para a disciplina de Arquitetura de Computadores, na UFF - Universidade Federal Fluminense no Período 2025.1.
  Realizado por Amanda Lemos Ribas, Guilherme Da Hora Andrade Fontoura, Lais Ferreira Nazareth, Maria Eduarda D'Angelo.

Consiste em simular o comportamento do **RISC-V Pipeling**, utilizando Python orientado a objetos e a bibloteca PyQt, para a interface gráfica.

Para rodar o programa, certifique-se que há a biblioteca PyQt instalada:
    
    pip install PyQt5

Execute o arquivo main.py com python.

Ao iniciar a Interface, clique em Browse File e selecione o arquivo desejado. 
* Permite a leitura de arquivos .asm e .txt, desde que o .txt tenha o formato de código em Binário. Arquivos para a leitura estão localizados na pasta arquivosExemplos.
* Permite visualizar ciclo por ciclo, a partir do botão NEXT.
* Permite visualizar todoos os cíclos simultaneos, a partir do botao RUN.

As tabelas apresentam, respectivamente, da esquerda para a direita, os valores dos 32 registradores, o valor de cada endereço na memória, a visualização do pipeline em cada instrução e ciclo.

  Formato das instruções Suportadas: 
  
  |    INSTRUÇÃO    |     FORMATO 1     |     FORMATO 2     |
  |-----------------|-------------------|-------------------|
  |   add           | add rd, rs1, rs2  |                   |
  |   sub           | sub rd, rs1, rs2  |                   |
  |   mul           | mul rd, rs1, rs2  |                   |
  |   div           | div rd, rs1, rs2  |                   | 
  |   rem           | rem rd, rs1, rs2  |                   | 
  |   xor           | xor rd, rs1, rs2  |                   | 
  |   and           | and rd, rs1, rs2  |                   |
  |   or            | or rd, rs1, rs2   |                   |
  |   sll           | sll rd, rs1, rs2  |                   |
  |   slr           | sllr rd, rs1, rs2 |                   |
  |   addi          | addi rd, rs1, imm |                   |
  |   lw            | lw rd, imm(rs1)   |                   |
  |   sw            | sw rd, imm(rs1)   |                   |
  |   beq           | beq rd,rs1, label | beq rd, rs1, imm  |
  |   bge           | bge rd,rs1, label | bge rd, rs1, imm  |
  |   blt           | blt rd,rs1, label | blt rd, rs1, imm  |
  |   j             | j imm             | j label           |
  |   jal           | jal rd, imm       | jal rd, label     |
  |   jalr          | jalr rd, imm(rs1) | jalr rd, label    |
  * No código binário, todos os tipos de formatos são suportados.


### Sobre a implementação:
* A pasta **risc_data** contém os dicionários que contém dicionários que contém os parametros dos registradores (registers.py) e das instruções (instructions.py).
* A pasta **interface** contém os arquivos necessários para a implementação da interface, que recebe informações do arquivo pipeline/runPipelino para relacionar com as tabelas.
* A pasta **pipeline** contém arquivos nomeados com cada Instrução do Pipeline, que cada um simula cada execução, sendo conectados pelo arquivo **RunPipeline.py**, que contém uma operação para o RUN e outra para o NEXT.
* A classe main executa a interface que está conectada ao Pipeline.
* O PC inicia no 0 e anda de 1 em 1.
* Os registradores começam todos com 0
* A memória começa None
* Exemplos de Implementação: 
  - arquivosexemplos/memoria.asm: a memória preenchida está na posição 100 do vetor de memória.

Desconsiderar Arquivos e Pastas com OLD.
