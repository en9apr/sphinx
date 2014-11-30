Questions on Print, Expressions and Variables
=============================================

Question 1
----------

Which of the following are syntactically correct strings?

* ``'She shouted "Hello!" very loudly.'`` 
* ``"Hello, world."`` 
* ``[Hello]`` (not a string - string must use quotation marks)
* ``Hello`` (not a string - string must use quotation marks)
* ``'This is great!'`` 

Question 2
----------

To display a value in the console, what Python keyword do you use?

``print``

Question 3
----------

In the following code, the one line starting with #. What does this line mean to Python?::

    tax_rate = 0.15
    income = 40000
    deduction = 10000
    # Calculate income taxes
    tax = (income - deduction) * tax_rate
    print tax

* This text is used as a file name for the code.
* The text is stored in a special variable called #.
* This is a syntax error.
* This text is printed on the console.
* **This is a comment aimed at the human reader. Python ignores such comments.**

Question 4
----------

Which of the following arithmetic expressions are syntactically correct?

* ``7 / +4``
* ``9 + * 4`` (syntax error - two operators are together)
* ``(8 + (1 + (2 * 4) - 3))``
* ``(7 - 2) / (3 ** 2)``
* ``9 - (2 - (4 * 3)`` (syntax error - parenthesis not closed)

Question 5
----------

You would like to make it so that the variable ounces has the value 16, thus representing one pound. What simple Python statement will accomplish this?

* ``16 = ounces`` (syntax error)
* ``ounces = 16``
* ``ounces := 16`` (syntax error)

Question 6
----------

A gram is equal to 0.035274 ounces. Assume that the variable mass_in_ounces has a value representing a mass in ounces. Which arithmetic expressions below using the variable mass_in_ounces represent the equivalent mass in grams?

* ``0.035274 * mass_in_ounces``
* ``mass_in_ounces / 0.035274`` (correct)
* ``0.035274 / mass_in_ounces``
* ``mass_in_ounces * 0.035274``

Question 7
----------

Which of the following can be used as a variable name?

* ``ounces``
* ``16ounces`` (syntax error - cannot start variable with digits)
* ``number123``
* ``my-number`` (syntax error - dash is a minus sign)
* ``MYnumber`` (ok but unconventional)
* ``__number__`` (ok but only for special variables)

Question 8
----------

Assume you have values in the variables x and y. Which statement(s) would result in x having the sum of the current values of x and y?

* ``x += y`` (this)
* ``x = x + y`` (this)
* ``y += x``
* ``x += x + y``

Question 9
----------

Python file names traditionally end in what characters after a period? Don't include the period.

``py``

Question 10
-----------

We encourage you to save your Python files where?

* Nowhere — Python automatically saves your files for you
* On your computer only
* **In "the cloud" and on your computer**
* In "the cloud" only
