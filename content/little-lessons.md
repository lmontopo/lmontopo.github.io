Title: Little Lessons
Date: 2014-10-27 04:00
Author: Leta Montopoli
Slug: little-lessons

This blog post will be dedicated to some of the little (but important!)
lessons I've learned over the past week. Enjoy!

#### The list method "extend" returns None.

Before I explain this lesson, let me just back up for a second and
address the lingo "method". Only recently have I been able to add this word to my vocabulary, so
I'll take the time to explain it briefly here. A method is actually just a function that is associated
with a class. It is usually called on an instance of that class. If you've written some
code in Python you've probably already used methods, even if you didn't know the lingo. Now
lets talk about extend, a method invoked on lists! Here's a little example to illustrate what it does:

```python
>>> list = [1,2,3]>>> list.exten
d([4,5])>>> print list[1,2,3,4,5]

```

Now, consider the following bit of code. Warning: It will produce an
error!

```python
>>> list = [1,2,3,4,5] >>> list.
extend([6,7]).extend([8,9])

```

I expected to get the list with entries 1 through 9 in return, but
instead I was greeted with the following message: "AttributeError: 'NoneType' object has no
attribute 'extend'"
^[1]. I
was working with Julia Tufts at the time, and we were both intrigued by this
message. So we did a little playing around and realized that although the method 'extend' alters the list instance
it is invoked on, the method actually returns None. So when we extend doubly, in one line, as I did
above, list.extend([6,7]) returns None, and then we try to extend None with [8,9], producing an error. Cool!

#### Recursion.

For a while now I've had a vague idea of what recursion was, but my
vague idea caused me to believe I actually had a REAL idea of what it was. I didn't. Here's a little
example that Kuan Butts gave me which really cleared up my confusion: Suppose we want to write a
function that, when given a number, will write out that number as 1 + 1 + 1 .... etc. Here's a simple way to
use recursion to write that code:

```python
def plus_one(num):    if num ==
1:        print num    else:
print '1', '+'         return plus_
one(num-1):

```

Here, the "base case" is when num == 1. This is when the recursion
stops, and you start jumping back out of the layers of recursion.

#### Writing automated tests is useful!!

Previous to hacker school I had written some automated testing for the
sake of learning how to do it. I learned the very basics of how to write an automated test,
and then I never used this knowledge because I didn't see the point. I reasoned, "why would I waste
time writing code to test my code, when I could just test it on my own?" After all, I
had been testing my code on my own all along anyway, and I had been getting by just fine! And I wasn't
wrong! I really had been making out just fine. But then I got to hacker school and started working on
bigger, more involved projects. At some point I was having a hard time keeping track of all the things I
needed to test. I had a list of inputs to test, but many times I forgot exactly what each of them was
testing for. It started getting a little out of control, and it was at this point, that writing automated tests
became a valuable tool for me! It was magical to be able to write all of my tests in one file, with
comments, and be able to quickly run those tests every time I made a change to my project.

So, the moral of the story is: If you are working on small projects and
you can keep track of your own testing and debugging, then by all means skip the automated tests! But know that they aren't
pointless. They have their uses, even if its not for your project.

#### What's a cache?

The other day I boldly decided to pair with Susan Steinman on her NY
Public Library app, even though I had no experience with the things she was doing. When we met up she told me she
was working on improving her "cache" and since I didn't know what a cache was, I asked. A cache, I discovered, is
just a database on a web application that stores stores previously requested data. Have you ever
noticed that when you search something on the internet that you've previously
searched, often the results come faster the second time around? This is caching at work! I'll use Susan's
app as an example. Suppose someone has used her app to search for the book 1984 by George
Orwell. Then, suppose I use her app and search for the same book. Her cache will already have
stored the results of the previous 1984 book search, so my inquiry can obtain the data directly from her cache instead of trying
to retrieve the information all over again from the NY Public Library database. Thanks Susan for
pairing with me!

[1]:

    Ok so I realize now that this may be a bit confusing since the error
    specifies that it is an attribute error instead of a *method* error. I'm not
    exactly clear on the difference between an attribute and a method, but I am pretty sure that a
    method IS an attribute. I think the word "attribute" is just a more general term. So for now, we'll
    go with that! Hopefully later I'll write a blog post to clear up the difference!