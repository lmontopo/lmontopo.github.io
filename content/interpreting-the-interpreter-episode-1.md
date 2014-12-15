Title: Interpreting the Interpreter: Episode 1
Date: 2014-10-20 04:00
Author: Leta Montopoli
Slug: interpreting-the-interpreter-episode-1

**This episode will describe my experience in the initial phases of writing a Lisp interpreter.**
I will describe how I started, my thought processes as I progressed,
some of the code I wrote, how it worked, and, why,at day 3, I decided to start from scratch (almost). If you are only
interested in the final product,skip this episode! If, however, you'd like to get some insight as to how
a newbie handled thetask of writing an interpreter, read on!

Step one: recruit a friend. (This just makes the process a little more
fun, plus its great to have someone to bounce ideas off of!) I recruited Kuan. We decided that we'd each write our own interpreter,
but that we'd talk through all the stepstogether, work side by side, and help each other debug. Our plan has
worked out great so far! 

To start, and we grabbed our computers,retreated to a quiet room, and sat quietly for a few moments,
contemplating the task at hand. I found myself asking, "What do interpreters do again?", and then
answering my own question with, "Right, they 'interpret'and then execute the code". We figured that before our computers could
execute any code, the code must first be separating into small elements, or **tokens**. (The word
**token** is the technical name referring to the smallest element of any programming language.) In separating the code this way, we would later be able to instruct our computers toscan through these elements in order, making sense of each element
individually, before executing the expressions they form together. We figured a good way to go about **tokenizing**
would be to create a list of all of the tokens in the input. (Tokenizing is just the action of separating the
tokens. Don't worry if you aren't familiar with the terms token and
tokenization. I didn't know the meaning of these words until after I had already tokenized my
input!) This is the code Kuan and I came up with:

```python
holder = input.replace( '(' , '( ' )
holder = holder.replace( ')', ') ' )
holder = holder.split(' ')
holder = filter(lambda a: a != '', holder)
print holder
```

Here, 'holder' is what I decided to call the list that is constructed
from the input, because it 'holds' the input. Given, for example,

```python
input = "(/ (+ 3  2) (- 4 2))"

```

This program will return the list:

```python
holder = ['(', '/', '(', '+', '3', '2', ')', 
'(', '-', '4', '2', ')', ')']
```

Notice that before splitting the input, we added space around each of
the brackets. This accounts for the case where the user inputs two brackets side by side, or a number
right beside a bracket with no space.

Having successfully created a list, holder, to hold the contents of our
input, we begun writing an algorithm to evaluate this content. For starters, Kuan
and I decided we would limit ourselves to making our interpreter work
for basic math expressions. After that we would gradually worry about interpreting more complicated inputs.

When basic math is inputed the most nested expression should be
calculated first. We needed a way for the computer to find which math expression is the innermost one. We
created the following algorithm: 

1- Scan through the elements of holder from left to right in
search of the first ')'.

2 - Begin scanning again, this time in search of the last '(' we hit
before the first ')'.  

3- Extract whatever is inside of those brackets, and evaluate it. 

4- In holder, replace this innermost expression (including the brackets surrounding it) by its
result we just evaluated.  

5- Start again at 1. 

This process would continue until there were no more brackets and expressions
left to evaluate. At this point, we would have evaluated the entire
expression.

We were able to write a working piece of code that implemented this
algorithm, but it was sloppy and we'd only interpreted basic math. Kuan and I took a step back and
looked at how our algorithm would pan out moving forward. We
brainstormed how we could go about interpreting 'define' expressions and we realized
our current algorithm was going to get pretty complicated. Consider, for example, interpreting the expression:
'(define (func) (+ x 2))'.

If our current algorithm encountered this as input, it would find
'(func)' and would get stuck trying to evaluate it.  It seemed that before even beginning our algorithm, we'd have to first
scan the entire input looking for the key word 'define'. Then, every
time we find 'define', we'd have to find the set of brackets containing the entire 'define'
expression. This in itself is kind of cumbersome, but we're only the beginning. Once our entire 'define' expression is
isolated, we'd have to search within this expression to find the our function's name. This would be done by scanning from left
to right and searching for the first ')' we come across, and then scanning again until we found its
corresponding '('. Then we'd have to remember the contents of these brackets, and begin scanning again to
find the defined function's expression. Once the expression was found, we'd have to
assign the contents of the previous two brackets as the name of the function's expression we just found.

If you're getting confused, I don't blame you. Clearly this algorithm is
confusing. The reason it is confusing is because there are so many states the the computer is
required to keep track of at any moment. First we have to know we have found an expression
containing 'define', and that we are searching for the entire define expression. Then we isolate this expression, and
we have to remember that we are within the define expression and that we are searching for the right bracket that will contain the
function's name. Then we have to remember we have found the right bracket of the name of the function we are defining, and we're
searching for the left bracket containing the name, etc etc. SO MUCH TO KEEP TRACK OF!!!

We turned to some resources online to see how they were approaching
these things. We found

[Mary Cook's
article](https://www.hackerschool.com/blog/21-little-lisp-interpreter)
and [Peter Norvig's article](http://norvig.com/lispy.html) helpful.

They had taken the parsing stage one step further than we
did. Instead of storing the brackets as elements of the list, they
created a version of "holder" which was a nested list. So, in the example where "(define (func) (x +
2))" is inputed, their code would turn it into the following array:

```python
['define', ['func'], ['+', 'x','2']]
```

Kuan and I decided to figure out if/how this extra parsing step was
advantageous. After talking to Mary Cook in person about it (thanks Mary!) we got our answer:

Using the nested method allowed us to not have to keep track of as many
sates! Indeed, at each stage of interpreting, we could simply look at the outermost list, look at the
operator, and then act accordingly.

If we encountered a 'define' expression we could handle it as follows:
Given the new structure ofvholder we know that if our operator is define then holder[1] will be the
function's name. Likewise, we would know that the expression of this defined function could be
found at holder[2]. With this extra parsing step, there is no longer the need to scan through the list
searching for brackets, and keeping track of where we are. The nested structure of holder
replicates the actual structure of the input, and a lot of the pain and agony in our previous method is taken care of
for us here.

Having clearly understood the differences between our algorithm and the
popular one found online, and having seen the benefits of theirs over ours, we decided scratch
what we had and start again. (Of course, the little tokenizer I described above could stay.)

I would like to mention that I am HAPPY for the mistakes I made, as they
resulted in a great deal of learning. I am a big advocate of trying things your own way first, and
only changing your way once you've learned the merits of another way. Doing so results in a great
deal of learning you might otherwise miss out on.

In the next episode, I hope to introduce to you the final product, and
explain how it works!

Stay tuned!

