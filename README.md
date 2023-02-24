# Write Number in Expanded Form

You will be given a number and you will need to return it as a string in [Expanded Form](https://www.mathsisfun.com/definitions/expanded-notation.html).

This kata is constructed from a 2 part Codewars kata:
- https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python
- https://www.codewars.com/kata/58cda88814e65627c5000045/train/python

## Part 1

```
>>> from src import expander
>>> expander.expanded_form(12)
'10 + 2'
>>> expander.expanded_form(42)
'40 + 2'
>>> expander.expanded_form(70304)
'70000 + 300 + 4'
>>>
```

NOTE: All numbers will be whole numbers greater than 0.

## Part 2

```
>>> from src import expander_part2
>>> expander_part2.expanded_form(807.304)
'800 + 7 + 3/10 + 4/1000'
>>> expander_part2.expanded_form(1.24)
'1 + 2/10 + 4/100'
>>> expander_part2.expanded_form(7.304)
'7 + 3/10 + 4/1000'
>>> expander_part2.expanded_form(0.04)
'4/100'
>>>
```
