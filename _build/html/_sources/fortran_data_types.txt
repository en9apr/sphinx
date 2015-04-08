==========
Data Types
==========

.. contents::
   :local:

Primitive Data Types
====================

Fortran does not initialise values, these will be "undefined" unless you give an initial value:

Initialisation
--------------

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Data Type
     - Meaning
   * - ``integer(specs) [, attrs] :: i = 1, j = 0``
     - **Integer** declaration with default 4 bytes (with list and initialisation)
   * - ``real(specs) [, attrs] :: r = 1.0e-7``
     - **Real** declaration with 4 bytes
   * - ``double precision(specs) [, attrs] :: d = 2.0d-12``
     - **Double precision** declaration with default 8 bytes, equivalent to real(kind=8)
   * - ``complex(specs) [, attrs] :: z = cmplx(1.0, 1.0)``
     - **Complex** declaration with default 8 bytes
   * - ``logical(specs) [, attrs] :: b = .true., c = .false.``
     - **Boolean** declaration with default 4 bytes
   * - ``character(specs) [, attrs] :: s = "string_1", t = "string_2"``
     - **String** declaration with default 1 byte

Specifications
--------------

.. list-table::
   :header-rows: 1
   :widths: 40 50

   * - Specification
     - Meaning
   * - ``real(kind = 8) :: value = 3.142d20``
     - Real declaration with **8 bytes** (double precision)
   * - ``character(len = 10) :: s = "string_1"``
     - String declaration with length **10 bytes** (10 characters)
   * - ``character(len = *) :: s``
     - String declaration with length **declared elsewhere**

1 Byte
~~~~~~

Specifications are based on bytes and a byte is:

* **One** character
* An integer between **-128 and 127**
* The logical values ``.true.`` and ``.false.``

Range of Values
~~~~~~~~~~~~~~~

The meaning of the specifications is in the possible range of values:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Exponent
     - Range
   * - ``integer :: short_integer = 3000``
     - -2147483648 to 2147483647
   * - ``integer(kind=8) :: long_integer = 30000000``
     - -9223372036854775808 to 9223372036854775807
   * - ``real :: small_number = 1.0e10``
     - 1.175E-38 to 3.402E+38
   * - ``real(kind=8) :: large_number = 1.0d50``
     - 2.225D-308 to 1.798D+308

Attributes
----------

Quite a lot of the time we use double precision, so I used that is this example

.. list-table::
   :header-rows: 1
   :widths: 40 50

   * - Specification
     - Meaning
   * - ``real(kind=8), parameter  :: pi = 3.142``
     - Real **constant** with 4 bytes
   * - ``real(kind=8), intent(in) :: x``
     - Real variable is expected as an **input**
   * - ``real(kind=8), intent(out) :: y``
     - Real variable is expected as an **output**
   * - ``real(kind=8), external :: f``
     - Result of function f is real and is evaluated **externally** (like a lambda function in python - function names used as arguments to other functions)
   * - ``real(kind=8), dimension(n) :: array_one``
     - Array of **rank** 1 (1D), with **shape** 1xn containing real values and **extent** of possible indices is 1 (default)
   * - ``real(kind=8), dimension(0:10) :: array_two``
     - Array of **rank** 1 (1D), with **shape** 1x11 containing real values and **extent** of possible indices 0 to 10
   * - ``real(kind=8), allocatable, dimension(:,:) :: array_three``
     - Array of **rank** 2 (2D), with **shape determined elsewhere** containing real values and **extent** of possible indices is 1 (default)

Other attributes I haven't used yet include:

* ``pointer`` - behaves like ``allocatable``, except it uses existing memory not new memory
* ``target`` - the variables to which ``pointer`` is associated
* ``public`` - variables are used externally
* ``private`` - variables are used internally
* ``optional`` - used if the variable is optional on the argument list
* ``save`` - to preserve values between successive calls
* ``intrinsic`` - not sure what this means - **how could you declare an intrinsic variable?**

Substrings
----------

Let's say we had the string ``string = "12345"``

To extract elements, use ``string(start : end)`` where start and end are the indices of the start and end values.

.. list-table::
   :header-rows: 1
   :widths: 20 20

   * - Code
     - Meaning
   * - ``s1 = string(2:5)``
     - ``"2345"``
   * - ``s2 = string(:3)``
     - ``"123"``
   * - ``s3 = string(3:)``
     - ``"345"``

Initialise a Range of Values to the Same Value
----------------------------------------------

Fortran allows us to **initialise a range of values** to the same value using the ``data`` statement:

``data nlist /clist/``

* ``nlist`` is a list of names of variables, arrays, elements of arrays, substrings, implied do lists
* ``clist`` is either ``c`` or ``r*c`` where ``r`` is the number of values to initialise and ``c`` is the value to give 

.. list-table::
   :header-rows: 1
   :widths: 20 20

   * - Code
     - Meaning
   * - ``data i, j, k /3*0/``
     - Initialise all the values to zero

Fortran 77
----------

To be able to read old Fortran, we might need these definitions. I am filling this table out to decode Ferzinger and Peric's notation (which uses old formatting)

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Data Type
     - Meaning
   * - ``integer``  ``integer*2``  ``integer*4``  ``integer*8``
     - Integer with 2, 4 and 8 bytes (4 is default)
   * - ``real``  ``real*4``  ``real*8``  ``real*16``
     - Real with 4, 8 and 16 bytes (4 is default)
   * - ``double precision``
     - Double precision 8 bytes
   * - ``complex``  ``complex*8``  ``complex*16``  ``complex*32``
     - Complex with 8, 16 and 32 bytes (8 is default)
   * - ``logical``  ``logical*1``  ``logical*2``  ``logical*4``  ``logical*8`` 
     - Boolean with 1, 2, 4 and 8 bytes (4 is default)
   * - ``character``  ``character*n`` 
     - String with n bytes (1 is default)
   * - ``parameter(a = 2.12, b = 5.32)``
     - List of typeless constants (bad for giving type)
   * - ``common a, b, c``
     - List of global variables (bad for encapsulation)
   * - ``dimension a(n)``
     - Array declaration


