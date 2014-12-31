Title: Little Lessons: Episode 2
Date: 2014-11-06 05:00
Author: Leta Montopoli
Slug: little-lessons-episode-2
Categories: Blog

Seeing as there are a whole **bunch** of "little lessons" that I'd like
to write down and keep track of, I've decided to extend my previous blog
post "Little Lessons" into a whole series! Get ready!

#### Mutating Iterables:

Suppose we have a list and we'd like to mutate some (or all) of its
elements as we iterate through them. Supposing that the way in which we
want to mutate each element isn't too complicated, this seems like a
straight forward task.

The case I was initially looking at consisted of a list where each
element of my list was either True or False. I wanted to go through the
list and change some of the False entries to True. As is the case with
many tasks in computing, this task was a little trickier than I
initially expected. For the purpose of this lesson, it will suffice to
consider a simple list of integers. Here we go!

```python
>>> list = [1,2,3,4]
>>> print list
[1, 2, 3, 4]
>>> for item in list:
...     item +=2
... 
>>> print list
[1, 2, 3, 4]
```

I'm not sure about you, but this was not exactly what I was expecting
the first time I tried it. Lets add an extra print statement to better
see whats going on.

```python
>>> for item in list: 
... 	item += 1
... 	print item 2345
```

It seems that our code is understanding, and executing, "item += 1",
yet, the list itself is not being mutated! HOW CAN THIS BE SO?! After a
bit of research Julia and I found our answer: when items of a list are
iterated with this 'for item in list' statement, Python creates an
element 'item' which is a copy of the value of that list element. This
item is an entirely separate object than the elements of the list, and
so changing 'item' has no effect on our list. Here's how you *can*
change the elements in the list, as intended:

```python
>>> list = [1, 2, 3, 4]
>>> for i in range(len(list)):
...     list[i] += 1
...
>>> list
[2, 3, 4, 5]

```

Yay! Notice how we access the elements of the list DIRECTLY.

#### User-defined Exceptions/REPL/Errors vs Exceptions

Yesterday I added the finishing touches to my Lisp Interpreter. (Expect
a long and detailed post about that very soon!) My program was
interpreting Scheme as I intended it to, but it wasn't very user
friendly. I decided to turn it into a REPL. The acccronym REPL stands
for "Read, Evaluate, Print, Loop". What a REPL does is exactly what you
might think: it will read user input, evaluate it, print the result back
to the user, and then wait for further input. Using a while loop and
using Python's raw\_input() command, it was pretty straightforward to
get my interpreter to work like a REPL for non-erroneous user input.
However, if the input was erroneous then the entire program crashed.
Somehow, I needed my program to ACCEPT erroneous input and respond to it
with an appropriate error message. The way I went about doing this was
by creating my own class of Exceptions! That's right: since everything
in Python is an object, Errors and Exceptions are themselves objects,
and we can create our very own classes of them!

Lets step back for a minute and quickly discuss what is meant by the
terms "Error" and "Exception" in Python. I found the distinction to be a
little confusing at first. It turns out that the term "Error" is a broad
category which can be divided into two different types: Syntax Errors
and Exceptions. Syntax errors are errors which are produced because
characters or strings are misplaced, missing, or added when they
shouldn't be. In comparison, the errors which occur during execution are
refered to as "exceptions". These errors indicate that the *meaning* (as
opposed to the syntax) of the code is erroneous.

Great, now lets talk about how I implemented my own class of exceptions!
The implimentation of this class required very little code:

```python
class MyError(Exception):    
	def __init__(self, msg):        
		self.msg = msg
```

Then I created several different instances of this class. Each instance
refers to a different type of error that could occur, and each had a
message associated with it. Here is the function I implement in my
program which takes care of all things to do with being a REPL:

```python
def repl(env):    
	try:         
		x = raw_input('> ')        
			try: 
				print interpret(x, env)
			except MyError, e:   
				print(colored(e.msg, 'red'))         
		return repl(scope)    
	except KeyboardIterrupt:        
		exit()
```

Here my code "tries" to print out the result of calling the interpret
function on the user input. If any isntance of MyError occurs, then it
will instead return the message associated to that instance of MyError.
Notice the second parameter, 'e'. It makes reference to the particular
instance of MyError which was raised and saves me from having to specify
case by case all of the instances of MyError which could be encountered.
For the record, 'e' is not some MAGIC variable that has a special
meaning in Python. It is simply what I chose to name the second
parameter. I could easily change 'e' to 'blah' and the code will work
the same. (I actually tested it out to check!)

