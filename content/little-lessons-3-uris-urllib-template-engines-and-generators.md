Title: Little Lessons 3: URI's, 'urllib', Template engines, and generators.
Date: 2014-11-19 05:00
Author: Leta Montopoli
Slug: little-lessons-3-uris-urllib-template-engines-and-generators

I've learned so many fun little lessons over the past week, its time for
another post!

#### What is a URI? Is it the same as a URL?

URI stands for uniform resource identifier. A very common form of a URI
is the URL, which stands for uniform resource locator. The URL is just
the address of a website - ie. the thing you type into your browser when
you want to visit a webpage. Apparently, sometimes, the terms URI and
URL are used interchangeably. But, if you want to be precise, know that
a URL is a type of URI. Time to dig a little deaper into URL's...

#### What meant by the 'path' and the 'query' of a URL?

The wikipedia page,
[here](http://en.wikipedia.org/wiki/Uniform_resource_locator), does a
good job at explaining the URL. I'll summarize what I learned from it
here. The URL consists of several different parts. I'll introduce these
parts and discuss them with respect to this example:
http://www.cineplex.com/Search?Query=Interstellar

-   The very first part of the URL is the **protocol**. It specifies
    which application protocol is being used to obtain the resource. In
    our example the application protocol is 'http'.
-   The **domain name** can be an IP address or a registered and easier
    to remember name associated to an IP address. In our example the
    domain name is 'cineplex.com'. If you are creating a server on your
    own computer, your domain name might be 'localhost'.
-   After the domain name a **port number** can optionally be specified.
    By default we are directed to port 8000, and so it is almost always
    unnecessary to manually specify a port.
-   A single domain name or IP address can host a multitude of files.
    The particular file/resource that a URL is after is specified by the
    **URL path**. It specifies the address of the particular file we are
    requesting and is analogous to the way in which we specify the path
    to a particular file within our own computer. In our example the URL
    path is '/Search'.
-   The **query string** contains data (usually inputed by the user)
    which will be passed to some sort of software running on the server.
    The example I've shown is the result of typing "Interstellar" into
    the search bar on the cineplex homepage. "Interstellar" was passed
    to the servers computer and used in some program to figure out the
    output. Then the results were passed back to me in the webpage with
    URL "http://www.cineplex.com/Search?Query=Interstellar". The query
    string part of the URL is '?Query=Interstellar'. As far as I know,
    the query string always starts with a question mark.

#### urllib.uncode('string') is great! Here's why:

As I may have previously mentioned, I have decided to write my own web
framework. Not because I think I can do a better job than the existing
frameworks, but because I want to learn more about what is happening
behind the scenes with web development. An issue I encountered as I
developped my framework involved html forms and processing user input.
If a user inputed any special characters, like '!', '\~', '?', etc., my
browser would encode these characters and send my server an http request
with these encodings. For example, '!' was encoded as '%21'. Why is the
browser doing this? Although its tempting to think that this character
encoding is just a pain in the butt, its actually pretty useful! Indeed,
some characters in the URL have a special meaning. The question mark,
for example, is always used to signify the begining of a query. So
whenever the *USER* inputs characters which have (or may have) a special
meaning, the browser will encode these characters to avoid confusion.
The places where these characters are used by the browser to indicate a
special meaning, they are NOT encoded. So, to make this clear, when a
user inputs "?" into a form, it will be encoded. But if a query string
is present, the "?" at the begining of the query will not be encoded.
And this makes my life alot easier when I have to parse through the raw
http requests. I can guarantee that whenever I see a "?" it is
signifying the begining of a query string, and NOT some user input.
Great! But now, I DO have to worry about decoding the encoded characters
so that they can correctly be passed as a variable to an html page. How
do I decode a special character from its encoded represenation? Using
the python's urllib module!! Check it out:

```python
>>> urllib.quote('!!!')'%21%21%2
1'>>> encoded_input = urllib.quote('
&!?')>>> print encoded_input%26%21%3
F>>> decoded_input = urllib.unquote(
encoded_input)>>> print decoded_inpu
t&!?>>>

```

#### What is a template engine?

A template engine provides a way for users to put variables and possibly
even logic into their html templates. Templating engines consist of a
templating language and a templating compiler. The templating language
specifies syntax that will be understood to mean specific things in your
html template. So, for example, you could say that two curly braces will
enclose any variables and that a curly brace and a percent sign will
enclose any python logic. Then, you're compiler will parse this html
template and then will see which parts need to perform logic or input
variables, and will ultimately translate the template into an html page
void of any logic or variables, that can be displayed by your browser.
Often, template engines are part of what makes up a web framework.

#### Generators are a kind of python object!

You know how you can write lists like:

```python
>>> [x for x in 'abcdefg']['a',
'b', 'c', 'd', 'e', 'f', 'g']

```

This way of specifying a list is called a **list comprehension**. I just
found out yesterday that if we write the same thing but instead use the
non-square embraces, then we create something called a generator. Check
it out:

```python
>>> (x for x in 'abcdefg')<gener
ator object <genexpr> at 0x10b323910
>>>>

```

Woah! So whats a generator? I honestly don't know. Yet. All I know is
that its a different kind of python object, one which I had previously
no idea about. By typing in \`dir((x for x in 'abcdef')) we can see the
collection of methods that generators have, and it is, obviously, a
different collection than the methods associated with lists. I hope to
come back to generators in the future to explain why they are used and
what they are good for!

#### Hexadecimal Numbers in Python

Have you ever seen numbers starting with 0x in python, and not really
known what they were for? I have seen these around, and always just
thought they were some sort of complicated encoding. In reality, numbers
begining with 0x are just hexidecimal numbers - ie. numbers with base 16
instead of 10. (If you aren't familiar with hexidecimal numbers, no
worries. You can read up on it
[here](http://simple.wikipedia.org/wiki/Hexadecimal_numeral_system).) So
we can write:

```python
>>> 0x1117>>>

```

since 11 is the base 16 representation of the decimal number 17. Mystery
solved.

