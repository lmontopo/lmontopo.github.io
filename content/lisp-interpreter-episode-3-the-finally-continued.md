Title: Lisp Interpreter: Episode 3 (The Finally!) ... Continued.
Date: 2014-11-24 05:00
Author: Leta Montopoli
Slug: lisp-interpreter-episode-3-the-finally-continued

In last week's episode we inspected how my program tokenizes and parses
the user's input. In the spirit of finishing this series of blog posts,
I have decided today to present an overview of how the rest of my
program works. We'll walk through the basic algorithm that my program
follows, pausing at some of the more exciting and important parts. I'll
do my best to skip over the less exciting bits of code, while still
providing enough information to convey the general ideas. If anyone
would like to see the code in its entirety, feel free to check it out on
my github account: <https://github.com/lmontopo/Lispeter>. As always, I
welcome any questions or comments about either this blog post or the
code i'm describing. Lets begin!

After the user's Scheme input is parsed and tokenzied, it is passed to a
function which 'unwraps' it. This funciton is called 'outer\_evaluate'.
Remember how, in the tokenzier, the input gets wrapped in an extra set
of parenthesis? My 'outer\_evaluate' function is how I dealt with this.
It evaluates from left to right each of the internal expressions within
the parsed expression and then it spit out the result of the last
expression. Here's the function:

```python
def outter_evaluate(list_input,env):
	evaluated_list = []
	for expression in list_input:
		evaluated_list.append(evaluate(expression, env))
	return evaluated_list[-1]
```

Here, 'evaluate' is the main function that interprets the parsed input.
Inside 'evaluate' the input is classified as either a list or an atom
and is passed to the 'is\_cons' and 'is\_atom' functions respectively.
The 'is\_atom' function is pretty straightforward since atoms are
self-evaluating, but I'll take a bit of time to describe how the
'is\_cons' function works.

When 'is\_cons' is called it inspects the first element of the list that
is inputed. Assuming that our input is a valid Scheme expression, we
expect the first item in this list to be a function. 'is\_cons' will
check to see if this function is in our pre-defined list of special
functions. (Recall that special functions are the ones that change the
flow of the interpretation.) Once the program has decided if the
function is special or not, input is directed to either the
'is\_special' or 'is\_regular' function, whichever is appropriate. Lets
talk a bit about both of these functions.

The 'is\_special' function consists of a case by case evaluation of what
to do for each special operator. I'll just present a subset of this
function because the whole thing is a little long and overwhelming.
Here's some of it:

```python

def call_special(list_input, env):
	head, rest = list_input[0], list_input[1:]

	if head == "map":
		if len(rest) == 2:
			new_head, list_to_act_on = rest[0], evaluate(rest[1], env)
			new_list = []
			for item in list_to_act_on:
				new_item = interpret("(%s %s)" %(new_head, item), env)
				new_list.append(new_item)
			return new_list


	if head == 'define':
		if len(rest) == 2:
			if type(rest[0]) is str:
				env.add_values(rest[0], rest[1])
			else:
				name = rest[0][0]
				expression = MakeLambda(rest[0][1:], rest[1:])
				env.add_values(name, expression)
		else:
			raise too_many

	if head == 'lambda':
		func = MakeLambda(rest[0],rest[1:])
		env.add_values('lam', func)
		return 'lam'
		

	if head == 'quote':
		if len(list_input) == 2:
			return rest[0]
		else:
			raise quote_error
```

The input is split into the 'head' and 'rest', the 'head' being the
special operator. Each special function has a corresponding bit of code
which indicates how to interpret that kind of expression. Notice that
when we encounter 'lambda' and 'define' operators we use some sort of
'MakeLambda' magic. Don't worry, i'll come back to explaining this
magic, but first I want to present the 'call\_regular' function, where
more magic appears!

```python
def call_regular(list_input,env):
	new_list_input =[]

	for term in list_input:
		new_list_input.append(evaluate(term,env))

	list_input = new_list_input
	head, rest = list_input[0], list_input[1:]
	return env.fetch(head).do_fun(rest, env)
```

In contrast to the 'call\_special' function which outlines a specific
proceedure for each special operator, the regular functions are all
dealt with in exactly the same way. This is something I'm quite proud
of. Its just so *pretty*!

Again, notice the magic... I'm calling some 'do\_fun' method on some
'env.fetch' thing... What is all this?! To explain whats going on here,
I'll start by talking about environments. I implimented a class called
Scope to keep track of my environment throughout the evaluation process.
Here it is:

```python
# --- DEFINING SCOPE --- 
class Scope(object):
	def __init__(self, env, parent = None):
		self.env = env
		self.parent = parent

	def add_values(self,key,value):
		self.env[key] = value

	def fetch(self, key):
		if key in self.env.keys():
			return self.env[key]
		elif self.parent != None:
			return self.parent.fetch(key)
```

Every scope object consists of an environment and a parent. The
environment is a dictionary containing variables/functions and their
values/expressions. The parent of a scope instance is the smallest scope
containing it. If a scope's parent is not specified then it gets the
default parent, 'None'. The global scope will have a None parent but all
other scopes should have a legitimate parent, possibly the global scope.

Lets inspect the methods of the Scope class. The 'add\_values' method
simply updates the environment by adding more key value pairs. The
'fetch' method looks up variables in the scope's environment. Notice
that if we have no luck looking up a variable in the current
environment, then fetch will redirect us to our parent's environment.
This means that even if our current scope is not the global scope, all
of the variables in the global environment can still be accessed. But,
since we look in our current scope first, it also means that we can
re-define any of the global variables in our current scope, and, when we
fetch for the values of these variables, we'll get the appropriate,
re-defined, value.

By now we should understand that `env.fetch(head)` is returning the
value of the key 'head' from the dictionary in our current scope. What
we have yet to discuss is what 'MakeLambda', and 'do\_fun' are refering
to. Here's the bit of code that defines these terms:

```python
# ------ CLASSES OF FUNCTIONS ------
class MakeLambda(object):
	def __init__(self, first, second):
		self.first = first
		self.second = second
		self.params = self.first
		self.exp = self.second[-1]

	def do_fun(self, args, env):
		zipped = zip(self.params, args)
		temp_scope = Scope({}, env)
		for param, arg in zipped:
			temp_scope.add_values(param, arg)
		return evaluate(self.exp, temp_scope)


class MakePyFun(object):
	def __init__(self, everything):
		self. everything = everything

	def do_fun(self, arguments, env):
		if len(arguments) > 1:
			return self.everything(arguments)
		elif len(arguments) == 1:
			return self.everything(*arguments)

```

These classes are used to create function objects. I use the MakePyFun
class to make function objects out of the built-in, non-special, Scheme
functions. I use MakeLambda to make function objects for user defined
functions. (You'll remember that this MakeLambda was called when the
user input contained either 'lambda' or 'define' expressions.) The main
difference between these two classes is that functions created with the
MakeLambda class have a defined set of parameters which are specified in
their definition. This means that instances of MakeLambda cannot operate
on an arbitrary number of arguments. In comparison, functions defined
using the MakePyFun class, *can* be called on an aribitrary number of
arguments. One very important thing to notice, though, is that both the
MakePyFun class and the MakeLambda class have 'do\_fun' methods which do
essentially the same thing: They take in some arguments and evaluate the
function on those arguments. This is how the 'call\_regular' function
needed only to fetch the value of 'head' in our current scope and call
'do\_fun' on the result. It didn't matter whether the result of fetch
was an instance of MakeLambda or of MakePyFun, because both have the
'do\_fun' method!

At this point I've pretty much described all of the exciting aspects of
my program. But, before wrapping up this blog series, I think I owe it
to anyone who's made it this far to present a nice solid example.

Consider the user input `((define (f x)(+ x x))(f 4))`. After this
expression is tokenized and parsed it will enter the 'outer\_evaluate'
function as: `[['define', ['f', 'x'], ['+', 'x', 'x']], ['f', '4']]`.
'Outter\_evaluate' then calls 'evaluate' on the first item in this list,
`['define', ['f', 'x'], ['+', 'x', 'x']]`. Evaluate decides that this is
a list, and passes it on to the 'is\_cons' function. 'is\_cons' decides
that 'define' is a special function and passes the expression to
'call\_special'. In 'call\_special', 'head' is assigned to 'define' and
'rest' to `[['f', 'x'], ['+', 'x', 'x']]`. Since the
`if 'head' == 'define'` condition is satisfied, it's consequent block of
code is executed. This assigns 'name' to 'f' and 'expression' to
`MakeLambda(['x'], ['+', 'x', 'x'])` and adds them as a key-value pair
to our current environment. The first part of the user input has now
been evaluated, and control is turned back over to the `outter_evaluate`
function which calls `evaluate(['f', '4'])`. From 'evaluate' we are
redirected to 'is\_cons' and then to 'call\_regular'. In 'call\_regular'
the value of 'f' is fetched from our current environment, returning the
MakeLambda object we previously instantiated. It's 'do\_fun' method is
called with argument '4', returning `evaluate(['+', 'x', 'x'], env)`
where env contains `{'x' : '4'}`. This time 'evaluate' directs us once
again 'is\_cons' which directs us to 'is\_regular'. Here, both x's
evaluate to 4. and then we fetch '+' from our environment. We will not
find '+' in our current environment, but will find it in the global
environment. `env.fetch('+')` will return the instance of 'MakePyFun'
associated to addition. This will be called on the arguments
`['4','4']`, and finally, 8 will be returned. Phew.

And finally, I have finished my series of interpreting the interpreter.
I've learned alot through this project, and had a lot of fun in the
process. Thanks again to the awesome [Allison
Kaptur](http://akaptur.com) for suggesting this project to me and for
your encouragement along the way. To anyone else out there who is
contemplating writing a lisp interpreter, I whole heartedly encourage
you to do so!

Thanks for reading!

