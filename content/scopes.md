Title: Scopes got me again!
Date: 2014-12-15
Categories: Blog

In a previous blog post I wrote about some of the struggles I encountered with scoping when Margo and I worked on our web framework Chapeau.  This week, scopes got me again!  This time, while I was working on my Template Engine. 

I think that, as a new programmer, its not totally surprising that I've been a bit naive and carefree about scopes and global variables.  However, I think that making mistakes was a good way for me to learn.  Having been tricked by scoping issues twice now, I'll be much more careful with these matters in the future.  

In this blog post I'm going to present a peice of code I wrote as an example.  It illustrates in a straightforward manner the issues I was facing with my Template Engine.  After presenting the code, I'll explain what is problematic about it. I'll present some examples tests I wrote for it, I'll show the weird things that the tests were doing, and I'll explain what I initially thought was happening and what I learned was *actually* happening. 

Here's the example file which I've named string_maker.py

```python
class HTMLString(object):
	def __init__(self, value = ""):
		self.value = value
		
	def update(self, html_text):
		self.value = self.value + html_text

my_HTML = HTMLString()

def add_to_string(text):
	my_HTML.update(str(text))
```
First the class HTMLString is defined with attribute 'value', initially set to be the empty string.  This class also contains a method, update, which adds an inputed string to the end of value.  An instance of this class called my_HTML is created and a function, 'add_to_string()', is defined.  This function basically turns some input into a string format and calls my_HTML's update method on that string. 

This code is pretty simple and it does a satisfactory job of concatinating more characters to the end of an existing string.  But notice that only one string is ever being added to.  Indeed, we only have one instance of the StringHTML class.  If we wanted this program to produce two different strings, well it can't (or at least I don't think it can in its current state).  This isn't really an issue unless, say, this code was part of a larger program intended to work as a template engine...  So consider for a moment that the strings we are creating in this program are HTML pages.  Perhaps these webpages will be sent back to a web-app which wants multiple web-pages.  If more than one HTML page is being created, then our program would have to terminate, and then start up again, in between HTML pages.  That's not really ideal.  

Since my Template Engine has code that is similar to string_maker.py, we can already can see that I wasn't going about things in the smartest way.  I did realize this at some point but I wanted to get some working tests up and running before improving my code.mSo lets write some tests for string_maker.py!  I started with this:

```python
from string_maker import *
import unittest 

class TestMain(unittest.TestCase):

	def test_simple(self):
		add_to_string('<html>Hey!</html>')
		self.assertEqual(my_HTML.value, '<html>Hey!</html>')

```

And received this lovely little message back:

```
Ran 1 test in 0.000s

OK

```

Gotta love that!

Now lets add another test function to this class, and we'll call add_to_string() multiple times in this test to make sure that it will keep updating as we expect.   Here's what we'll add:

```python

	def test_call_multiple(self):
		add_to_string('<html>One')
		add_to_string('two')
		add_to_string('three</html>')
		self.assertEqual(my_HTML.value, '<html>Onetwothree</html>')

```

At this point I expect an error.  Afterall, I know that string_maker.py can only create one html page at a time.  So lets run the test and see. 

```
$ python test.py
.F
======================================================================
FAIL: test_class (__main__.TestMain)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test.py", line 8, in test_class
    self.assertEqual(my_HTML.value, '<html>Hey!</html>')
AssertionError: '<html>Onetwothree</html><html>Hey!</html>' != '<html>Hey!</html>'

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

A single error, as expected.  What I didn't expect was for the first test, test_simple, to be the failing test!  This lead to a nice lesson about Python Unittests: **Tests do not run in the order that you declare them**.  Cool! 

At this point I get all naive and think "OK, I can fix this, here's how":

```python
from string_maker import *
import unittest 

class TestMain(unittest.TestCase):

	def test_simple(self):
		my_HTML = HTMLString()
		add_to_string('<html>Hey!</html>')
		self.assertEqual(my_HTML.value, '<html>Hey!</html>')

	def test_call_multiple(self):
		my_HTML = HTMLString()
		add_to_string('<html>One')
		add_to_string('two')
		add_to_string('three</html>')
		self.assertEqual(my_HTML.value, '<html>Onetwothree</html>')

```
I figured, if I just re-instantiate my class inside each function, then my_HTML.value will be whiped clean at the begining of each test.  Problem solved, right?  Wrong....


```python
$ python test.py
FF
======================================================================
FAIL: test_call_multiple (__main__.TestMain)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test.py", line 16, in test_call_multiple
    self.assertEqual(my_HTML.value, '<html>Onetwothree</html>')
AssertionError: '' != '<html>Onetwothree</html>'

======================================================================
FAIL: test_class (__main__.TestMain)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test.py", line 9, in test_class
    self.assertEqual(my_HTML.value, '<html>Hey!</html>')
AssertionError: '' != '<html>Hey!</html>'

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=2)
```

AHHH!! WHAT IS HAPPENING!?  My instinct was to think that UnitTests just work in reallly wierd ways that I don't understand.  So I figured I experimented. 

The next thing I tried was this: Instead of re-instantiating HTMLString inside each test function I defined one of UnitTest's magic setUp functions.  When running unit tests, if you define a function called `setUp()`, then Python will know to run this function before every other test funciton.  So I made a setUp function to perform `my_HTML = HTMLString()`.  And then I got the same errors as I did when I never re-instantiated at all.  Its like my program didn't even run my setUp function at all!  I tried doing the same thing but with a tearDown() function, and again had no luck.  

I was so confused.  I got my awesome friend [Amanda][1]'s help, and she suggested that, instead of writing `from string_maker import *`, that I just import the functions I needed to run my code.  This was a good idea, but it didn't work either.  Amanda was awesome though, because she asked me all sorts of questions, and those questions helped me realize what I was doing wrong! Here's what I learned:

When I re-instantiate the `my_HTML = HTMLString()` inside each of my test functions, I am creating a local instance of this class.  Local, meaning, in the scope of the function.  Then I call `add_to_string` which updates the *global* instance of my_HTML (ie. the instance of the class that is in my code string_maker.py)
.  **These are not the same object!** So I update the global instance, and then assertEqual on the local instance, which of course still have an empty value string. 

If this isn't making sense, remember that when you create a function you create a scope for that function.  When a function encounters a name its not familiar with, it will first check within its own scope, ie within its own definition, to see if there is anything by that name defined there.  If there isn't, then it will look for things outside of its own scope. As soon as it finds something, it uses it.  

Take Away:  **You can have a local variable and a global variable that have the same name, but they are not the same thing!!!!** 

[1]: http://programmingforwitches.tumblr.com
