Title: Interviews are oportunities to learn
Date: 2015-01-29 05:00
Author: Leta Montopoli
Slug: interviews
Category: Blog
Tags: Python

Over the past month I've had my first experience interviewing for development positions.  Its been a somewhat nerve-racking experience but also, at times, enjoyable.  I've come to realize that the best way to approach an interview is with an attitude of excitement and an openness to learn.

A couple days before my first 'technical' interview I was feeling pretty overwhelemed.  Tom, a Hacker School facilitator, reminded me that **its public knowledge that I haven't been programming forever**.  He continued to explain that its OK I don't know everything, and that I'm not expected to.  This was exactly the reminder I needed to hear. Of *course* I don't know everything.  I'm just starting out in this field!  Sonali suggested I have fun with my interviews and that I view them as opportunities to learn.  

Their words of wisdom have really helped me make the most of my interviews. When I stopped putting pressure on myself to be something I'm not (an experienced programmer who knows everything) I could relax, be open to learning, and be genuinely engaged in conversations about programming.  Regardless of whether or not they lead to a job, I am counting my interviews thus far to be a success because of the way I handled them.  I was genuine, I had fun, and I learned cool things.  Win.


On that note, here's a neat Python thing I learned during a recent technical interview[^*]: 

#### A Python Function's Default Arguments Are Mutable:


Without running the python code, guess what the following lines would return in an interactive Python interpreter.  (Actually try to guess them before reading my answer! I've added a blank line where you should be guessing):


``` python
>>> def test(a = []):
...	a.append(1)
...	return a
>>> b = test()
>>> b

>>> c = test()
>>> c 

>>> d = test(c)
>>> d

```

Have you guessed yet?!
... 

My guess was `[1]`, `[1]`, `[1,1]` but the correct answer is `[1]`, `[1,1]`, `[1,1,1]`.

**What does all of this mean and what does it tell us about the way Python handles default arguments?**

It means that the default argument binding[^%] happens at the function's *definition* not at the function's *execution*.  In other words, the statement `a = []` is evaluated when the function definition statement is executed, but not when the function is called and its body is executed.

Lets dig a little deeper.  Recall that in Python everything, including functions, is an object. When a function definition is executed a new function object is created.  This function object will have an attribute called `func_defaults` that contains the values of the default arguments.  

```python
>>> test.func_defaults
([1,1,1],)
```

Like usual object attributes, func_defaults can be mutated.  In our example, the default argument is mutated when the body of the function is executed. Since the line of code that sets func_defaults to `[]` is run only when the object is instantiated, these mutations affect the default value for subsequent calls on the function. 

I hope this makes sense!  Feel free to ask questions if it doesn't. :) Also, some useful resources can be found [here][1] and [here][2].  

And to anyone out there currently undergoing interviews: Try to have fun.  Above all else, be yourself.  You are already impressive.


[1]: http://stackoverflow.com/questions/1132941/least-astonishment-in-python-the-mutable-default-argument
[2]: http://effbot.org/zone/default-values.htm
[^*]: The interviewer agreed that I could write about his question! :)
[^%]: Arugment 'binding' is just a fancy way of specifying that a variables name (ex. `a`) gets assigned to a peice of data (ex. `[]`).