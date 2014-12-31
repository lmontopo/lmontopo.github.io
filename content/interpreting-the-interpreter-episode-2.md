Title: Interpreting the Interpreter: Episode 2
Date: 2014-10-30 04:00
Author: Leta Montopoli
Slug: interpreting-the-interpreter-episode-2
Category: Blog

** Confession: I am not yet ready to present my final, finished, Lisp
Interpreter. It will be coming soon, but not today. Today I will
describe the rollercoaster ride of an experience taking on this project
has been for me. Then I'll focus in on a couple things I've learned
along the way. **

Last week Sumana asked me how my interpreter was going, and I explained
to her the mixed feelings I was having about the project. I told her how
somedays I feel things are goings great - I'm learning lots, the project
is challenging, and I'm excited! But other days I feel discouraged. I'll
put a lot of energy and effort into writing a peice of code for my
project only to later realize that this peice of code will not be used
at all. Apparently, this experience is not uncommon. There is an analogy
between this experience and hill-climbing which goes something like
this: Suppose there are many hills in a region, and we would like to
reach the top of the tallest one. When we are climbing uphill we feel
like we are making great progress. We feel the effort we are putting in
is getting us very close to our goal! But then we get to the top and we
discover we've been climbing a smaller hill and that the top of the
largest hill is still far away. Furthermore, we realize that to get
there, we actually have to go back down the hill we just climbed. When
Suman described to me this analogy, I felt releived. This was EXACTLY
what I had been experiencing!! It was good to know that I wasn't alone
in feeling this way. And she reminded me that this was all part of the
learning process. Indeed, in climbing these smaller hills, I've still
learned a great deal!

Here is one of the small hills I climbed, and the lessons I learned in
doing so.

#### All the way back to basic math.

Basic math was one of the first thing that Kuan and I tackled when we
begun writing our Lisp Interpreters. I thought I had conquered that task
long ago, but this week I realized I wrong. The code I had written to
interpret basic math looked something like this:

```python
if head in ['+', '-', '*', '/','<', '>', '<=', '=','>=']:    
	if head == '=':            
		result = eval(str(rest[0]) + '==' + str(rest[1]))
		return result    
	else:
	result = eval(str(rest[0]) +head + str(rest[1]))            
	return result

```

Here, head is the name given to the first element in a list. In this
case head is the operator. Notice that this code works for only two
operands. What I realized this past week is that Scheme actually accepts
math expressions with more than 2 arguments. For example, "(+ 1 1 1)" is
a legitimate scheme expression. And unfortunately, my current code
wouldn't interpret it. In the end, I changed the code to look like this:
(I'll just present a couple of functions, so that you get the idea)

```python
# ---- Defining Basic Math and Bool Functions ----  
def add(args):
	return sum(args)

def subtract(args):    
	return reduce(lambda x, y: x -y, args)

def equal(args):    
	return args[1:] == args[:-1]

def less(args):
	return args[:-1] < args[1:]

# ----Interpreting Basic Math and Bool Functions ---- 
if head == '+':
	return add(rest)
if head == '-':    
	return subtract(rest)
if head == '=':
	return equal(rest)
if head == '<':
	return less(rest)

```

As you can see, I made use of Python's built in sum function which can
handle multiple operands. Since there isn't a similar function built in
for subtraction, I made one with the reduce function. Since this is the
first time I've used the reduce function I'll describe to you what it
does. Reduce takes two arguments: a function and a interable. I used a
list as an iterable, and I used lambda to define the function. Reduce
will take the function and will apply it cumulatively over the inputed
iterable. So, in my subtraction example, if I call subtract([4, 2, 1])
then it will calculate ((4 - 2) - 1) and will return 1.

Notice that I didn't use the reduce function for evaluating boolean
statements. I tried to use it, but I was getting wonky results. This is
what I tried:

```python
def equal(args):    
	return reduce(lambda x, y: x == y, args)

```

To test this equal function, I input [1,1,1] and [2,2,2]. The expression
"equal([1, 1, 1])" would return True while "equal([2, 2, 2])"" would
return False. After taking the time to think about it, I realized what
was happening. When I set my input to [1, 1, 1], "(1 == 1)" will first
be evaluated and will return True. Then it will take True, and will
evalute "(True == 1)", which will again return True! Indeed, in Python
(and if I'm not mistaken, in most computer languages) True is 1 and
False is 0. This expalains why equal([2, 2, 2]) returns False. Python
would first evalute (2 == 2) returning True. Then it will evaluate "True
== 2" and return False. Pretty neat eh? Sometimes it pays off to take
the time to really think about how your code is working, and why it
isn't returning what you anticipate.

In the end, I was able to define a successful equal function as
described above, by:

```python
def equal(args):    
	return args[1:] == args[:-1]

```

Lets go through what this does when we input, say, args = [arg1, arg2,
arg3, arg4]. Two smaller lists are constructed: args[1:] = [arg2, arg3,
arg4] and arg[:-1] = [arg1, arg2, arg3]. Then the statement "[arg2,
arg3, arg4] == [arg1, arg2, arg3]" is evaluated. Notice that this is
essentially evaluating (arg2 == arg1 and arg3 == arg2 and arg4 == arg3),
which return True exactly when all the elements in the list are equal. I
really like this function because I feel its really simple and clean and
straight-forward.

So, as you can see, there were moments this past week when I had to step
WAYYY back and re-write code I thought I was already done. But, in doing
so, I learned some really fun and cool things. Don't be discouraged if
you have to go back to something you thought you had finished! It could
turn out to be fun!

