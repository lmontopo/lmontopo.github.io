Title: Lisp Interpreter: Episode 3 (The Finally!)
Date: 2014-11-18 05:00
Author: Leta Montopoli
Slug: lisp-interpreter-episode-3-the-finally

Let me start off by apologizing for the delay. I've been hesitant to
write this post for several reasons, including:

1.  Presenting and explaining my entire lisp interpreter is a BIG (and
    therefore daunting) task.
2.  There are parts of my code that I'm not entirely satisfied with and
    I *may* refactor these parts in the future. For this reason, I've
    been debating waiting until I finish refacturing to write this post.
3.  The parts of my code that I'm unsatisfied with are pretty ugly and
    are a pain to read. Which leads me to the next point...
4.  Will anyone actually read this?

I have decided to go ahead and write this blog post anyway. Even if no
one reads it, I think that I'll benefit from writing it. As far as the
ugly bits go, I'm trying to not let 'perfect' be the enemy of 'good
enough'. This project is far from perfect but that OK. I worked hard on
it, it works, I learned lots during the process, and those are the
things that matter most. Besides, I've gotten really excited this week
about some other projects, so it could be a while before I get back to
refacturing the interpreter.

OK. Lets get started. Here are the first ten lines of code:

```python
from __future__ import divisionf
rom termcolor import coloredfrom sys
import exit#------GlOBAL LISTS-----
-symbol = ['+', '-', '*', '/', '<',
'>','<=', '=','>=', 'abs', 'list', '
if', 'not',            'set!', 'begi
n', 'let', 'define', 'lambda', 'quot
e']special = ['set!', 'begin', 'let'
, 'define', 'lambda', 'cond', 'quote
', 'if',     'list', 'map', 'cons',
'car', 'cdr']

```

The first 3 lines just specify any functions I'll be using from built in
libraries. Next, two important global lists are introduced. The list,
'symbol', specifies strings that have a special meaning and will
therefore be treated differently from other strings of characters. The
list 'special' is a list of all of the built in Scheme functions which
disrupt the flow of the interpretation. All functions, including
addition, subtraction, etc. will be treated in the same way. But our
interpreter will treat these 'special' functions differently.

Next, we introduce my class of exceptions and some instances of that
class:

```python
# --- EXCEPTIONS ---class MyErro
r(Exception):    def __init__(self,
msg):        self.msg = msgif_error
= MyError("Error: you need to specif
y by a consequence and an alternate.
")dict_error = MyError("Error: can't
find element in dictionary. Imprope
r input.")unexpected_error = MyError
('Error: unexpectedly entered parse
function with no input.')too_many =
MyError("Error: too many arguments w
ere inputed.")quote_error = MyError(
'Error: quote only takes one operand
.')let_error = MyError('Error: let m
ust be followed by a list.')

```

Then, we start doing some of the gritty work: tokenizing and parsing. I
have implemented both my tokenizer and my parser as functions. When we
call them, the output of the tokenizer will be fed as input to my
parser. Here is my tokenizer:

```python
# ---- TOKENIZE ------ def token
izer(holder):    holder = '(' + hold
er + ')'    holder = holder.replace(
'(' , ' ( ' )    holder = holder.re
place( ')', ' ) ' )    final = filte
r(lambda a: a != '', holder.split('
'))    return final

```

The tokenizer takes my user's raw input - something like `(+ 2 2)`. It
begins by putting extra braces around the entire thing. It then adds
space around all the braces before splitting the input into an array
where each element is a separate token. The input splits over spaces,
which is why it was necessary to add extra space around the braces. far
so good, but why did I begin by adding extra braces?! Seems kind of
wierd, right?

The reason for this seemingly cooky choice was to accomodate inputs like
the following: `(define x 3) x`. This is a valid Scheme expression which
evaluates to 3. Suppose that I do not add extra brackets around the
entire statement. Then, when I go to actually *interpret* the input, it
becomes difficult to know when the end of the user input has been
reached. In fact, I did NOT initially add these extra brackets in my
tokenization, but my interpreter evaluated `(define x 3) x` to be `None`
instead of `3`. It simply stopped evaluating after `(define x 3)`.
Knowing when the end of the user input has been reached, however, is
quite easy if we have an outter set of brackets enclosing everything. Of
course, adding extra brackets came with its own set of issues. I needed
to make sure that my interpreter could differentiate between expressions
like `(3)` and `3`. Although '3' is a valid Scheme expression, `(3)` is
not, and I was essentially changing my input to always look like `(3)`.
Thanks to Mary Cook, I came up with a pretty clever solution to this
issue, which we will come accross later.

Continuing on... the parser! Writing this parser was my first encouter
with recursion! Here's the code:

```python
# ---- PARSER ----- def parse(to
kens):    if len(tokens) == 0:
raise unexpected_error    token =
tokens[0]    tokens = tokens[1:]
if token == '(':        parsed_input
= []         while tokens[0] != ')'
:            to_append, tokens = par
se(tokens)            parsed_input.a
ppend(to_append)        tokens = tok
ens[1:]                 #pops off th
e ')' part        #we add a conditio
n to check if last return        if
len(tokens) > 0:            return p
arsed_input, tokens     #if not last
return, need to return current vers
ion of tokens        elif len(tokens
) == 0 :            return parsed_in
put             #if last return, onl
y want to return new list of tokens
else:        return chec
k_type(token), tokens

```

To better understand this function, lets look at how
`parse(['(', '(', +, '1', '1', ')', ')'])` would be processed, line by
line. Line 3 is not satisfied, so we skip to line 6 and 7. Here Token
will be set to `'('`, tokens will become
`[ '(', '+', '1', '1', ')', ')']`. Since the condition on line 9 is
satisfied, we then enter this branch and continue on with line 10 where
`parsed_input` is initialized as an empty list. Then we enter the while
loop on line 12, and in line 13 we recurse back into our parse function
by calling `parse(tokens)`.

Now in the second level of our parse function. In this level we execute
line 6 and 7 again, setting `token` as `'('`, and `tokens` to
`['+', '1', '1',')', ')']`. Since `token` is still `'('`, line 10 will
again be executed, creating another `parsed_input` list, and then diving
into our 3rd level of recursion on `parse`.

In this 3rd level, token is `'+'` and tokens is `['1', '1', ')', ')']`.
Since token is not `'('` we skip down to the else condition and execute
line 23. Since we have yet to define the function check\_type, just
pretend that this line returns token and tokens. Having returned those
values, we come out of the 3rd layer of recursion and back into the 2nd,
at line 13. Here, `to_append` is set to '+', and tokens is
`['1', '1', ')', ')']`. Line 14 is then executed, and `parsed_input`
becomes `['+']`. We continue looping through this while loop, going into
a 3rd layer of recursion, coming back into two, and appending
`parsed_input` until `parsed_input` looks like ['+', '1', '1'] in our
second layer of recursion. At this point the tokens[0] will be ')', so
we break out of the while loop. Line 15 remouves ')' from tokens,
leaving tokens as [')']. Then since the length of tokens is positive
line 19 is executed.

Now we exit the second layer of recursion and are back into the first
parse call. `to_append` becomes `['+', '1', '1']`, and `tokens` is
`[')']`. The original `parsed_input` is updated to `[['+', '1', '1']]`,
the while loop ends, and line 15 is executed, changing `tokens` to `[]`.
Since the `len(tokens)` is zero line 20 is executed and `parsed_input`
is the final return. We have exited all levels of the parse function,
effectively parsing the input!

This blog post will be continued... I have written enough for one day.

