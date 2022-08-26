.. _chapter-hazard:

Example: A Game of Chance
=========================

Hazard is a game of chance that was popular in medieval England.  To
play, a designated player named the *caster* throws a pair of
six-sided die and any number of other players can place bets on the
caster's rolls. In this chapter, we will first describe the game and
then write code to simulate it.

The game proceeds in rounds.  At the start of a round, the caster
chooses an integer, known as the *main*, in the range 5 to 9
inclusive. The caster then rolls both dice in the *come out roll*.  
The terminology for this part
of Hazard is complex and does not add a lot to our understanding of
the game.  Without affecting the accuracy of our simulation, we will
simply refer to the the sum of the come out roll as the *chance*.   

Here are the rules for the come out roll:

- If the chance is equal to the caster's chosen main, the caster immediately wins the round.  
- If the chance is 2 or 3, the caster immediately loses the round.
- If the chance is 11 or 12, then:

  * If the caster's main is 5 or 9, the caster loses the round.  
  * If the caster's main is 6 or 8, the caster wins the round if the chance is 12 and loses the round otherwise.
  * If the caster's main is 7, the caster wins the round if the chance is 11 and loses the round otherwise. 

If none of these conditions is met, the caster will continue to roll
the dice until a throw matches the main or the chance.
The caster wins the round if their last throw matches the chance and loses the
round if it matches the main.

Here is a table that summarizes these rules:

+---------------+-------------------------+--------------------------+---------------------+
|                          **Come out roll**                                               |
+---------------+-------------------------+--------------------------+---------------------+
| *Main*        | *Caster wins immediately| *Caster loses immediately| *Caster continues to|
|               | on a chance of*         | on a chance of*          | throw on chance of* |
+===============+=========================+==========================+=====================+
| 5             | 5                       | 2, 3, 11, 12             | Any other value     |
+---------------+-------------------------+--------------------------+---------------------+
| 6             | 6, 12                   | 2, 3, 11,                | Any other value     |
+---------------+-------------------------+--------------------------+---------------------+
| 7             | 7, 11                   | 2, 3, 12                 | Any other value     |
+---------------+-------------------------+--------------------------+---------------------+
| 8             | 8, 12                   | 2, 3, 11                 | Any other value     |
+---------------+-------------------------+--------------------------+---------------------+
| 9             | 9                       | 2, 3, 11, 12             | Any other value     |
+---------------+-------------------------+--------------------------+---------------------+

The caster continues playing rounds until they lose two consecutive rounds, 
at which point another player becomes the caster.

To make this description more concrete, 
let's play a few rounds with a chosen main of 5.

+-----------+------+-----------+-------------------------------+
| **Round One**                                                |
+-----------+------+-----------+-------------------------------+
| *Main*    |*Roll*| *Result*  | *Notes*                       |
+===========+======+===========+===============================+
| 5         | 9    | Continues | Come out roll, chance is 9    |
+-----------+------+-----------+-------------------------------+
| 5         | 7    | Continues | Does not match main or chance |
+-----------+------+-----------+-------------------------------+
| 5         | 7    | Continues | Does not match main or chance |
+-----------+------+-----------+-------------------------------+
| 5         | 9    | Wins      | Roll matches chance           |
+-----------+------+-----------+-------------------------------+

In this round, because the caster rolls a 9 in the come out roll, the
chance is 9.  This value does not match any of the special cases for
the first roll, so the caster continues to roll the dice.  Neither of
the next two rolls (7 and 7) match either the chance or the main, and
so the caster rolls once more.  In their final roll, the caster throws
a 9, which matches the chance, and wins.


+-----------+------+-----------+-------------------------------+
| **Round Two**                                                |
+-----------+------+-----------+-------------------------------+
| *Main*    |*Roll*| *Result*  | *Notes*                       |
+===========+======+===========+===============================+
| 5         | 4    | Continues | Come out roll, chance is 4    |
+-----------+------+-----------+-------------------------------+
| 5         | 6    | Continues | Does not match main or chance |
+-----------+------+-----------+-------------------------------+
| 5         | 11   | Continues | Does not match main or chance |
+-----------+------+-----------+-------------------------------+
| 5         | 12   | Continues | Does not match main or chance |
+-----------+------+-----------+-------------------------------+
| 5         | 5    | Loses     | Roll matches main             |
+-----------+------+-----------+-------------------------------+

In the second round, because the caster rolls a 4 in the come out
roll, the chance is 4.  This value does not match any of the special
cases, so the caster continues to roll the dice.  The next three
rolls (6, 11, and 12) do not match the chance or the main, so the
caster rolls the dice a fifth time.  The final roll is a 5, which
matches the main, and the caster loses the round.

+-------------+------+-----------+---------------+
| **Round Three**                                |
+=============+======+===========+===============+
| *Main*      |*Roll*| *Result*  | *Notes*       |
+-------------+------+-----------+---------------+
| 5           | 11   | Loses     | Come out roll |
+-------------+------+-----------+---------------+

In the third round, the caster rolls an 11 in the come out roll and
immediately loses.  Since the caster has lost two rounds in a row, they
pass the dice on to another player. 

Given that brief explanation, let's look at some code for simulating
this game.  The first thing we need to do is simulate
rolling a pair of dice.

Rolling dice
------------

In Hazard, we throw of pair of dice and add the face values
together.  Because we will use this computation often in our simulation, 
it makes sense to write a very short function to do it:

.. literalinclude:: hazard.py
   :pyobject: throw_dice

We chose to use a constant for number of sides for the die, but we could have 
easily written this function to take the number of sides as
an argument.

Playing a round
---------------

The work needed to play a round is sufficiently complex that it makes
sense to encapsulate it in a function.  Since the caster chooses the main, 
this function will need to take the main as a parameter.  
The only detail that matters for the
rest of the game is whether the caster won the round.
We can return this information as a boolean: ``True`` for a win and
``False`` for a loss.  Putting these design decisions together gives
us the following function header:

.. literalinclude:: hazard.py
   :language: python
   :lines: 14-22

To simulate the come out roll, we first call our
``throw_dice`` function and save the result in a variable named
``chance``.

Next, we need to translate the rules for the come out roll.  At the
top-level, this computation requires a conditional with four branches.
The first two branches are straightforward: if each condition holds, the caster
wins in the first case (``return True``), and loses in the second
(``return False``).  

.. literalinclude:: hazard.py
   :language: python
   :lines: 26-29


To determine the outcome of the third case, we need a nested
conditional that branches on the value of ``chosen_main``.  

.. literalinclude:: hazard.py
   :language: python
   :lines: 30-37

Notice that the outcome of the second branch of the inner conditional
is not ``True`` or ``False`` but instead depends on whether the value
of ``chance`` is 11 or 12.  Since ``chance`` can only have one of
these two values, we can compute the output with a simple boolean
expression: ``chance == 12``.  The output of the third branch is
computed similarly, using the boolean expression ``chance == 11``.

Finally, if none of the first three conditions of the outer
conditional statement hold, then Python executes the body of the ``else`` branch.  


.. literalinclude:: hazard.py
   :language: python
   :lines: 39-44

In this case, the caster continues to throw the dice until a roll
matches either the chance or the main.  Let's look at how to encode
this condition in two parts: The expression ``(roll == chance) or
(roll == chosen_main)`` will be true when the roll matches either the
chance or the main.  Since our loop should continue only when that
condition does not hold, we can simply negate this expression to get
the proper test for the loop: (``not ((roll == chance) or (roll ==
chosen_main))``)

Notice that we again return the result of evaluating a boolean
expression.

A note about using parenthesis in expressions: because ``not`` has
higher precedence than ``or``, the parenthesis surrounding the
expression ``((roll == chance) or (roll == main))`` in the while loop
test are necessary for correctness.  The rest of parenthesis
surrounding expressions in this function, in contrast, are not
necessary for correctness.  Some programmers include parenthesis to
increase clarity, while others consider them unnecessary distractions.
You can decide for yourself.

We can put these pieces together to get the following complete function: 

.. literalinclude:: hazard.py
   :pyobject: play_one_round

Simulating a player
-------------------

We will also encapsulate the code for simulating an individual caster's turn 
in a function.  Similar to ``play_one_round``, this function will take
the chosen main as a parameter.  The betting rules for Hazard are
complex so, for now, our simulation will simply count the number of
rounds that the caster wins.  

.. todo::

  Add the next paragraph once we have added the betting section to the list chapter.

  We will return to this example to add
  code that simulates the betting process in a later chapter when we have
  more computational tools at our disposal.

Recall that the caster plays rounds until they lose two in a row.
Keeping track of the number of consecutive losses is the trickiest
part of this function.  We'll use a variable, ``consecutive_losses``,
that we initialize to zero because the caster has not yet played or
lost any rounds. We will call ``play_one_round`` to simulate a round
and update ``consecutive_losses`` as appropriate: on a loss, we will
increment its value.  On a win, we will reset it to zero.

As soon as the caster has lost two consecutive rounds, the test for
the while loop will be false and the function will return the number
of rounds won.


.. literalinclude:: hazard.py
   :pyobject: simulate_caster


.. todo:: 

    Possible later example for list of lists: add in betting.  The
    Wikipedia article (https://en.wikipedia.org/wiki/Hazard_(game))
    includes a table that was used to determine the odds given the
    values of the main and chance.

    Function could take the initial bet for the caster plus a list
    with bet amounts for the possible chances.  Nice example because
    the zero index of chance bet amount list would represent 5.
    Simple example of transforming a value to compute an index.

Estimating win rate
-------------------

Finally, we can easily reuse our function ``play_one_round`` to print
a table of estimated per-round win rates for the different possible choices for
main.  There is a tradeoff between accuracy and computation time: simulating 
more rounds takes more time to compute
but produces a more accurate result.  Rather than hard-coding a specific number
of rounds, we'll write our function to take the number of rounds as a
parameter and let the user make this tradeoff.

We will use a pair of nested loops to generate the table.  The outer
loop will iterate over the possible values for main (``range(5,
10)``). Why ``10``?  Recall that ``range`` generates a sequence of
values from the specified lower bound up to, but not including, the
specified upper bound.  The inner loop will both simulate the desired
number of rounds and keep track of the number of rounds won for the
current value of ``chosen_main``.

.. literalinclude:: hazard.py
   :pyobject: print_win_rate_table

Notice that for this computation, we need to start with a fresh win
count for each possible value of ``chosen_main``, so the value of
``win`` gets reset to zero for each iteration of the outer loop.  As
we noted in our earlier discussion of loops, initializing variables in
the wrong place is a very common source of bugs.


