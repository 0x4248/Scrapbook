! SPDX-License-Identifier: GPL-3.0
! fortran-filetest
!
! file.f90
!
! COPYRIGHT NOTICE
! Copyright (C) 2024 0x4248 and contributors
! Redistribution and use in source and binary forms, with or without
! modification, are permitted provided that the license is not changed.
! 
! This software is free and open source. Licensed under the GNU general
! public license version 3.0 as published by the Free Software Foundation.

program main
	implicit none ! Explicitly declare all variables
	
	! Write hello world to a file
	print *, 'Writing file...'
    open(1, file='test.txt', status='unknown')
    write(1, *) 'Hello, world!'
    close(1)
	print *, 'File written!'

end program main