Title: What I learned from Crista Lopes
Date: 2014-10-11 04:00
Author: Leta Montopoli
Slug: what-i-learned-from-crista-lopes
Categories: Blog

The resident at Hacker School during my first week was Crista Lopes. She
has given some great lectures, and she's taught me some cool things!

##### Different Styles of Writing Code

On Monday night she spoke to us about coding styles, the topic of her
latest book. Crista explained that there are many different styles of code to work with, but that
often programmers get stuck in one way of coding. No style is "better" than another, but some work
better in certain situations. Crista suggests that when we set out to write a program we ask
ourselves, "what are our constraints?". Our constraint could be something we need to
minimize/avoid, or something we want to maximize/include. Examples of constraints include minimizing
the number of lines in our code, including functions, not including functions, and
maximizing efficiency. Theses constraints produce different "styles" of code. As a programmer, it is
good to familiarize ourselves with these different styles so that we can write in whichever
style is best suited for a particular project.

##### Data Types and Data Structures

On Wednesday Crista gave a really helpful introductory lecture on data
types and data structures.  Before this lecture I had little knowledge on the subject. I had heard
the words before but not really understood their meanings. Here is how she explained the two
concepts:

A **data type** is something more conceptual. It refers to our ideas of
what can be done with the data and what we want to do with the data.

The term **data structure**, on the other hand, refers to how we
*implement* the data type. When we talk about data structure we are referring to how a "data type" is actually
storred in memory on our computer and how we can access that data.

Crista talked about two common implementations of data in our computer:
the array, and the list. An array is a continuous portion of memory in our computer with
slots to put our data in. Each slot takes up the same amount of memory, and the total amount
of memory is fixed. Any slot of the array can be accessed directly. A list, on the other hand,
is NOT continuous. Different elements of the list can be stored in any location on the computer's
harddrive. Your computer knows which item is first in the list and each item will point to the
location in memory where the next item on the list is located.

*Ok... but why does all of this matter?!* Well, Crista provided us with
an example to illustrate why these things are important: Suppose we have a list of 500 contacts on
our computer. Our list contains the names and telephone numbers of each contact. We can call
this data type a "contact list". We have some choices as to how we can implement this
data. One option would be to use the list implementation described above. In this case, to find a
contact's telephone number we must scan through the list, starting from the top, until we arrive at
the name we are looking for.   Another option would be to implement our contact list as a hash
function.

*What is a hash function?!*

I think the best way to illustrate the hash function is by example, the
way Crista described it. In our contact list scenario, an example of a hash function would be
something that acts as follows:

For each contact, the computer associates to it the number of letters in
that contact's first name. Then an array, lets call it a, is created in memory. The nth cell of a
will "point" to a new list, containing only the contacts whose names have n letters. From there the
search starts from the top down, but the list is (hopefully) much smaller in size. Using this hash
function is much more efficient than just creating one list containing all of the contacts.
Indeed, computers can compute simple mathematical calculations like this one extremely
quickly, while scanning through lists is a more time consuming task.

At this point, I'd like like to clarify something about data structures
and types: What certain programming languages refer to as "lists" and "arrays" are not
necessarily implemented as such. Likewise, what is implemented as a list or array or hash function in a
programming language is not necessarily called a list, array or hash function. I know that this is kind of
confusing, but here are some examples to clarify the situation. What Python calls a "list" of n elements is
actually implemented as an array with more than n slots. The array is created longer than necessary,
leaving several slots empty. This makes the array easier to append (ie. add elements to). Another
example in Python is the data type "dictionary", which is actually implemented as a hash
function.

##### Objects, Functions, Etc.

On Thursday, I came to Crista with a few questions about some
terminology that had been confusing me. I didn't really understand what was meant by the terms "functional
programming" and "object oriented programming". I wondered, "are these terms referring to
particular languages or are they referring to a style of writing code"? According to Crista,
these terms mostly apply to the style a program is written in. However, the terms are sometimes used to
describe languages.   (No wonder I was confused!) Crista explains that when you step far
enough away, you can see certain trends in programming languages too.
Some languages might tend towards the functional style, while others might tend towards
the object oriented style, for example. In reality, though, most languages pull from all different
ideas. Python is an example of this. Although Python is often called "object oriented",
Python also has functions! Most languages combine these ideas as does Python, though there are some
exceptions. Haskel, for example, is a purely functional programming language.

This leads me to the next question: What is an object and why is it important? Although I've created classes
and objects in Python programs, I wasn't sure I really understood the point. Crista
provided me with an explanation that I liked. She explained how objects are constructs which
"wrap around" your data, so that you can't access it directly. This protects the data
so that it is less likely to be accidentally corrupted. There are other ways that data can
be protected if a language doesn't use classes, but this is just one of those ways.

**Thanks Crista for visting Hacker School this week!!!!**

