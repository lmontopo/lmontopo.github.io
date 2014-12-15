Title: Interpreting the Interpreter: Episode 0
Date: 2014-10-17 04:00
Author: Leta Montopoli
Slug: interpreting-the-interpreter-episode-0

For a while now, I have been perplexed by the land of compilers and
interpreters. Thinking of

these things sparks all sorts of questions in my mind. For instance, if
a compiler compiles my program,

but the compiler is itself a program, doesn't something need to compile
the compiler? If so,

wouldn't this chain just go on forever? And, if I were to write my own
computer language (which I could,theoretically, do)

how would I go about doing so? And what's the difference between a
compiler and an interpreter?

Are interpreters and compilers things that I can write?!

In this episode, I will begin by trying to answer some of these
questions. In later episodes

I will describe my experiences writing a Lisp Interpreter. When I have
the interpreter all

set up and running, I'll present it, and explain it. But before we get
to that, I think its

worth while exploring what an interpreter IS, and how it differs from a
compiler.

Compilers and interpreters serve a similar purpose: they take

a piece of code written in some language that is foreign to your
computer, and they turn it into something that can

be executed on your machine. It's the way in which these two programs
work that differentiates them.

A **compiler** works by taking the inputed piece of code (this is called
the **source code**) and translating the

entire document into **machine code** (ie your machines native code,
written in 0s and 1s). The

compiler produces a new file, called the **object file** which can be
run directly on the machine,

without any intermediate translation. So, if I write a piece of code in
C++, for example,

then my compiler will read through the whole document, and will re-write
the set of instructions

I've written in C++ into machine language instructions. (Usually some
sort of optimization

is also involved, but we don't have to concern ourselves with that just
yet.) Since the code is

then executed from the object file, and no longer interacts with the
initial C++ document,

the C++ document could be deleted from your computer, and the code could
still be executed.

An **interpreter** on the other hand, executes the code directly as it
reads it. It doesn't create

another translated file first. An interpreter will just read a line of
code, will transform it into something it understands,

and then it it will execute it. I realize that this might all sound a
little vague, especially the part where I say the interpreter
"transforms it into

something it understands". What does *it* understand, anyhow? Well, lets
say we are writing

a lisp interpreter in python (as I will be doing soon!) and the
interpreter comes across a line of

code that reads "( + 1 1 )". Well, python doesn't understand this, but
if the interpreter changes

it to "1 + 1", then python does understand this. Hopefully that
clarifies things a little.

Of course, the discussion I provide of my experience writing an
interpreter should also help clarify things.

Another thing I'd like to mention is that languages are not always
either "interpreted" or

"compiled". Some languages, Python is one of them, are actually
implemented with both a compiler

and an interpreter. Although people often refer to Python as an
'interpreted language', its implementation has 2 parts: First, the
python code is

compiled into something called "byte-code". Then, an interpreter reads
and executes the byte-code!

Cool, eh? Big thanks goes to [Allison Kaptur](http://akaptur.github.io)
for explaining this to me and discussing interpreters

and compilers with me! You rock!

