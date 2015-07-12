Title: Regular Expressions in Python - with LOTS of Examples!
Date: 2014-12-04 05:00
Author: Leta Montopoli
Slug: regular-expressions-in-python-with-lots-of-examples
Category: Blog
Tags: Regular Expressions, Python

Over the past several days I've learned a great deal about regular
expressions. I struggled initially with the subject, but I think things
have finally clicked. So, I'm going to write what I've learned! In this
blog post I am going to:

-   Explain what a regular expression is.
-   Introduce `re.split()` and use it to provide examples.
-   Explain some of the ways that the star, dot, and question mark can
    be used in a regular expression.
-   Explain, in detail, the plague of the backslash.

As I learned about regular expressions, I found examples to be
enourmously helpful. For this reason, there will be a TON of examples
throughout this blogpost.

#### What is a regular expression?

A regular expression is sequence of characters that represent a pattern
we would like to search for within a larger chunk of text. There are two
types of characters within a regular expression: ones that represent
themselves, called **ordinary characters**, and one's that don't
represent themselves, called **special characters**. Most common
characters, like the letter 'a', match to themselves in a python regular
expression.

#### Introducing the split function:

To use regular expression in Python you need to `import re`. This module
gives you access to many different methods. The ones I use the most are
`re.split(pattern, string)` and `re.match(patter, string)`. I find
`re.split()` easiest to understand, so we'll start there. We'll visit
`re.search()` later.

The `re.split(pattern, string)` is very similar to python's built in
split method for strings. It splits the inputed string over the pattern
expressed by the regular expression. By default, `re.split()` will
return a list of all the parts of the string, excluding the parts that
matched the pattern. If you would like the resulting list to include the
sections which match to the pattern then parenthesis are needed around
the regular expression:

##### Example 1: Introductiory Example:

```python
>>> import re
>>> text = 'Hackerschool is cool.'
>>> re.split("a", text)
['H', 'ckerschool is cool.']
>>> re.split("(a)", text)
['H', 'a', 'ckerschool is cool.']
```

As you can see, when we put parentheses around 'a', then 'a' is included
in the resulting list. But perhaps we have a pattern that is more than
one character long, and we want only part of the pattern to be kept in
the array. To do this brackets are put around the part of the regular
expression we want to keep. Check it out:

```python
>>> re.split("a(ck)", text)
['H','ck', 'erschool is cool.']
```

Here the 'a' is still left out because it wasn't included in the
parentheses!

#### Special Characters Star, Period and Question Mark:

We're going to use `re.split()` to explore what these special symbols
match to in a regular expression.

##### Example 2: The period:

According to Python's regular expression documentation, the period
matches any character except a newline.

so as you'd expect it is going to split on every character...

```python
>>> text = "Hackerschool is cool!"
>>> re.split("(.)", text)
['', 'H',
'', 'a', '', 'c', '', 'k', '', 'e',
'', 'r', '', 's', '', 'c', '', 'h',
'', 'o', '', 'o', '', 'l', '', ' ',
'', 'i', '', 's', '', ' ', '', 'c',
'', 'o', '', 'o', '', 'l', '', '!',
'']
```

It might be surprising to you that there are empty string elements
between each character. I was surprised! I don't really have a good
explanation for why this happens except to say that this is just the way
the split function works. It finds the pattern we are searching for, and
then says "OK, on the left side of this pattern instance we have (fill
in the blank) and on the right side we have (fill in the blank)". In our
example, since every character is an instance of the pattern, on either
side of each pattern instance there is only the empty string. We'll see
another occurence of this behaviour in a later example. If it doesn't
make sense to you now, hopefully it will then.

Now lets combine the dot with other characters:

```python
>>> re.split("(.ool)", text)
['Hackersc', 'hool', ' is ', 'cool', '!']
```

This makes sense - there were two occurences where there appeared "some
character followed by 'ool'".

Lets try a couple more examples just to make sure we get the hang of it:

```python
>>> re.split("(c.o)", text)
['Hackers', 'cho', 'ol is ', 'coo', 'l!']
>>> re.split("(c.h)", text)
['Hackerschool is cool!']

```

The first time we split over 'cho' and 'coo' since both are instances of
the pattern "'c' followed by some character followed by 'o'". The second
time we don't split the expression at all. Even though 'ch' is in
school, there is no character between the 'c' and the 'h'. So 'ch'
doesn't match to the regular expression 'c.h'. The lesson here is that
**'.' on its own matches to exactly one instance of any character**. Not
zero, not two, one.

##### Example 3: The period and the star.

The star represents 0 or more repititions of the previous character
expressed in the regular expression. Whenever possible, the star will
'suck up' as much as it can. Because of this behaviour, star is called a
**greedy character**.

```python
>>> text = "I like reading scify books."
>>> re.split("(s.i)", text)
['I like reading ', 'sci', 'fi books.']
>>> re.split("(s.*i)", text)
['I like reading ', 'scifi', books.']
>>>
```

Without the star, the regular expression 's.i' will match to 'sci'. When
the star is added the regular expression matches to more stuff! The
expression 's.\*i' matches to 'scifi' because the star indicates that
the dot can be repeated 0 or more times. Because the star is greedy it
soaks up as many repetitions as possible.

Lets see what happens when we change the text to "I like science
books.".

```python
>>> text = "I like science books."
>>> re.split("(s.*i)", text)
['I like ', 'sci', 'ence books.']
```

Now that there is only one 'i' in the text, there are no more characters
that the star can suck up, so, "s.\*i" matches to 'sci'.

##### Example 4: The Question Mark

The question matches either 0 or 1 repetitions of the preceeding regular
expression. Here are some examples:

```python
>>> text = "There are num sections in this document."
>>> re.split("(e.*)", text)
['Th', 'ere are num sections in this document.', '']
>>> re.split("(e.?)", text)
['Th', 'er', '','e ', 'ar', 'e ', 'num s', 'ec', 'tions in this docum', 'en', 't.']
>>>
```

When we use the question mark instead of the star there are many more
matches to the regular expression! The question mark is basically the
oposite of a greedy character.

Also, notice the occurence of an empty string between the 'er' and the
'e'. Since we are splitting over the 'er' and the 'e' the split
functions wants to put something on either side of these that isn't
something else we're splitting over. The only thing between the 'er' and
the 'e' is the empty string. Hopefully this examples helps to understand
the whole empty string phenomenon.

##### Example 5: Combining the dot, star, and question mark:

Lets see what happens when we combine all three: the dot, the star, and
the question mark.

```python
>>> text = "There are num sections in this document."
>>> re.split("(e.*?)", text)
['Th', 'e', 'r', 'e', 'ar', 'e', ' num s', 'e', 
'ctions in this docum', 'e', 'nt.']
>>>
```

Placing the question mark after a the star makes the regular expression
match to the minimal number of characters possible. We'll see this more
in the next example...

##### Example \#4: Application to my Template Engine:

I have been working on writing my own template engine. In my language,
variables will be contained within double curly braces. I used regular
expressions to parse the html template and find all of the variables.
Lets see an example:

```python
>>> html_text = "<html><title> Hello {{name}}.</title> Today is {{day}}.</html>"
>>> re.split("({{.*?}})", html_text)
['<html><title> Hello ','{{name}}', '.</title> Today is ','{{day}}', '.</html>']
```

Just to make sure we understand what the star and question mark are
doing, lets see what happens when either one is removed:

```python
>>> re.split("({{.*}})", html_text)
['<html><title> Hello ', '{{name}}.</title> Today is {{day}}', '.</html>']
>>> re.split("({{.?}})", html_text)
['<html><title> Hello {{name}}.</title> Today is {{day}}.</html>']
```

When the question mark is removed, the star acts greedily and soaks
everything up until the last occurence of '}}'. When the star is
removed, we have no match to our pattern at all. This is because the
variable names inside the curly braces are more than 1 character long.

#### The plague of the backslash:

Now we have a handle on those special functions, lets explore the ...
dun dun dun... THE BACKSLASH!

Beleive it or not, the regular expression for a backslash is FOUR
backslashes. Woah. Lets walk through why this is the case:

In python, a backslash is a special character, and so to represent a
backslash we actually need to use two backslashes. So in python two
backslashes represents one. I'm not even talking about regular
expressions yet, I'm just talking about python strings. Lets verify
this:

```python
>>> backslash = "\\"
>>> len(backslash)
1
>>> print backslash
\
```

Neat!

Ok, so this means that we actually have to write a regular expression
which will match to two backslashes instead of to a single backslash.
Now, in regular expression land, backlash is one of those special
characters we talked about previously. They don't match to themselves.
The regular expression for a backslash is also two backslashes. So,
since we want to match to the python string `\\` the regular expression
to do so becomes `\\\\`.

I hope you've enjoyed this introduction to regular expression in Python.
If anything is confusing, don't hesitate to contact me!

