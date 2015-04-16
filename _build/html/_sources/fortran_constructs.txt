==========
Constructs
==========

.. contents::
   :local:

Conditional
===========

.. list-table::
   :header-rows: 1
   :widths: 30 60

   * - Code
     - Meaning
   * - ::

           if (expression) action

     - **One logical condition** expressible as an action (e.g. print) or on a single line (e.g. x = a) i.e. no multi-line blocks are allowed
   * - ::

           if (expression) then
               block
           else if (expression) then
               block
           else
               block
           end if

     - **Multiple logical conditions** 
   * - ::

           block_a: if (expression) then
               block
           else if (expression) then block_a
               block_b: if (expression) then
                   block
               end if block_b
           else then block_a
               block
           end if block_a

     - **Named Blocks** for nested blocks 

   * - ::

           select case(number)
               case (:0)
                   block
               case (1:2)
                   block
               case (3)
                   block
               case (4:)
                   block
               default
                   block
           end select

     - **Select** - choose an action depending on the value of ``number`` (an integer)

       * ``case (:0)``  :math:`\Rightarrow` ```number`` is :math:`\le` 0
       * ``case (1:2)`` :math:`\Rightarrow` ``number`` is 1 or 2
       * ``case(3)`` :math:`\Rightarrow` ``number`` is 3
       * ``case(4:)`` :math:`\Rightarrow` ``number`` is :math:`\ge` 4
       * ``default``  :math:`\Rightarrow` ``number`` is none of the above


Iteration
=========

.. list-table::
   :header-rows: 1
   :widths: 30 60

   * - Code
     - Meaning
   * - ::

           do i = start, stop, step
            
           end do

     - **Iterator** - loops with an integer counter until stop is reached
   * - ::

           do while (expression) 
            
           end do

     - **Do-While** - loops with condition tested at start
   * - ::

           do 
               if (expression) exit
           end do

     - **Blank Do** - loops without condition until the if statement is true
   * - ::

           outer: do 
               inner: do i = start, stop, step
                    if (expression) cycle inner
                    if (expression) exit outer
               end do inner
           end do outer

     - **Nested Do** - contains outer and inner loops

       * ``outer: do`` :math:`\Rightarrow` Outer "blank" do loop
       * ``inner: do i = start, stop, step`` :math:`\Rightarrow` Inner "iterator" do loop
       * ``if (expression) cycle inner`` :math:`\Rightarrow` Repeat inner loop according to expression
       * ``if (expression) exit outer`` :math:`\Rightarrow` Exit outer loop according to expression
       * **Notice the use of named loops to distinguish between them**, i.e. "outer" and "inner" are names of loops

Statements
==========

.. list-table::
   :header-rows: 1
   :widths: 25 60

   * - Code
     - Meaning
   * - ::

           stop

     - Halts the program cleanly
   * - ::

           return

     - Leaves a subroutine or function
   * - ::

           exit

     - Leaves a loop
   * - ::

           cycle

     - Next iteration
   * - ::

           continue

     - Used in a do loop, which would otherwise end in an if (archaic)
   * - ::

           go to statement_number
     - Jumps to the specified statement number (archaic)

 
