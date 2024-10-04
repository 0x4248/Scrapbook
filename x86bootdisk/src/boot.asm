; SPDX-License-Identifier: GPL-3.0
; x86bootdisk
;
; boot.asm
;
; COPYRIGHT NOTICE
; Copyright (C) 2024 0x4248 and contributors
; This file and software is licenced under the GNU General Public License v3.0. 
; Redistribution of this file and software is permitted under the terms of the 
; GNU General Public License v3.0. 
;
; NO WARRANTY IS PROVIDED WITH THIS SOFTWARE. I AM NOT RELIABLE FOR ANY DAMAGES.
; THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY AND LIABILITY OF ANY KIND.
;
; You should have received a copy of the GNU General Public License v3.0
; along with this program. If you have not please see the following link:
; https://www.gnu.org/licenses/gpl-3.0.html

 
[ORG 0x7c00]
[BITS 16]
jmp start               ; Jump to start

start:  
    ; Sertting up the stack
    xor ax, ax           ; clear ax
    mov ds, ax           ; set ds to 0
    cld                  ; clear direction flag
   
    mov si, boot_msg     ; set si to msg
    call bios_print      ; call bios_print
    jmp bios_print       ; jump to bios_print
    hlt                  ; halt the system

boot_msg db 'Booted!', 0

bios_print:
    lodsb                ; load byte from si to al
    or al, al            ; check if al is 0
    jz done              ; if al is 0, jump to done
    mov ah, 0x0E          ; set teletype output
    mov bh, 0            ; set page number
   
    int 0x10             ; call bios interrupt
    jmp bios_print       ; jump to bios_print

done:
    ret


times 510-($-$$) db 0   ; Fill the rest of the sector with 0
db 0x55                 ; Boot signature
db 0xaa                 ; Boot signature
