.data
str_4: .string "Funcion Suma"

.text
.globl _start

_start:
	
	la a0, str_4
	li a7, 4
	ecall

	li a0, 10
	li a7, 11
	ecall
	
	# Guardando parametros
    li a0, 666
	li a1, 1
	
	# Apilando valores
	addi sp, sp, -8
    sw a0, 0(sp)
	sw a1, 4(sp)
	
    # Llamando a la funcion
	call suma
	
	# Liberando espacio en pila
	addi sp, sp, 8
	
	# Imprimiendo valor (a0 ya contiene el retorno)
	li a7, 1
	ecall

	li a0, 10
	li a7, 11
	ecall
	
	li a0, 0
	li a7, 93
	ecall


suma:
	# Carga del parametro desde la pila
	lw a0, 0(sp)
	lw a1, 4(sp)
	
	# Realizando operación suma
	mv t1, a0
	mv t2, a1
	add t0, t1, t2
	li t3, 4
	sw t0, 0(t3)

	# Agregando valor de retorno
	li t3, 4
	lw a0, 0(t3)
	
	# Retornar control
    ret