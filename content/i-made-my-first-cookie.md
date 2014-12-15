Title: I made my first cookie!
Date: 2014-11-27 05:00
Author: Leta Montopoli
Slug: i-made-my-first-cookie

Margo and I have been working on our web-framework, Chapeau. To test out
its functionality and user-friendliness, we've been using Chapeau to
build various web-apps. This week we implimented a buzz-feed-style quiz.
To challenge ourselves (and Chapeau) we structured the app to have a
separate webpage for each question, and then a final webpage displaying
the result. This forced us to address the issues: 'Does Chapeau allow
data to be transfered between non-adjacent webpages?' and 'Does Chapeau
allow for the data to be accessed directly and used in a calculation'?
As we tried to answer these questions and broaden the functionality of
Chapeau, the framework took on several variations. In this blog post
I'll begin by describing how Chapeau works for very simple web-apps, and
then I'll continue by explaining some of the changes we made to Chapeau
as we worked towards our buzz-feed-style quiz.

#### Simple Web Apps

Chapeau's design makes very simple web-apps just that: very simple. To
make such an app, a developer needs only to define a dicitonary matching
URL's to their corresponding html pages. Then calling Chapeau's 'go'
function on the dictionary gets everything going. Pretty simple right?
Beleive it or not, with Chapeau, an app this simple can even pass
variables from an html form to the webpage that follows. The app itself
(by 'app' I mean the python code) does not need to be changed to include
this feature. Adding very basic variable passing to a Chapeau app is
just a matter of formatting your html pages accordingly. Here's how to
do it:

-   The form must specify either 'method = get' or 'method = post',
    since Chapeau deals only with post and get requests.
-   The form's action needs to specify the URL that this form redirects
    to.
-   The html page corresponding to this URL should have '%(key)s'
    wherever this key's value is meant to appear.

How is this all working? In the background Chapeau parses the request
made from the form's submission. Chapeau finds the user's input in this
request and stores it in a dictionary of key-value pairs called params.
The specified html file is then read in as a string with '%params'
tacked on to the end. Python's built in string formatting takes care of
the rest, and the page renders with the desired arguments! Easy-peasy.

But what if we wanted to mutate the user input in some way? Or what if
we wanted to *use* the input to perform some sort of analysis or
calculation? Perhaps we want to create some results for a quiz? Our
initial version of Chapeau could not handle such situations.

#### Adding Functions

To extend Chapeau's usability Margo and I decided that web developers
would have the choice to route a URL to a path or to a function. If a
URL is routed to a function then this function would have a few
structural constraints. Initially, these were the constraints we
implimented:

-   Chapeau will be passing a dictionary into the function, so the
    function must be defined to accept it. This dictionary will contain
    some of the request information and will look something like:
    '{'type': 'get', 'query': 'query\_string', 'path': 'url' , 'body':
    'user\_input\_from\_post\_form'}'. (Basically this dictionary stores
    all of the request information except for the headers.)
-   The function must return two objects: a path and a dictionary. The
    path will specify the next html page to be rendered and the
    dictionary will be the same one that the function receives, but
    possibly with some mutated data.

The dictionary that the function takes in gives the developer access to
the user input that was just aquired. If the developer wanted to mutate
this user input in anyway, they could do so. Alternatively, if the
developper wants user input to be saved so that it can be obtained
later, Margo and I figured this could be done as well. The developper
could create a global dictionary that they can add to when user input is
submitted, and that they could read from later. Problem solved. Except
not really.

More experienced developpers might already see the problem we've
created. Consider the buzz-feed-style quiz that Margo and I wanted to
create. Suppose that we implimented this app by storing the user input
in a global dictionary. This dictionary is updated after every question
is answered. When the results page needs to be rendered all of the user
input is obtained from the global dictionary. But suppose two clients,
client1 and client2, are taking the quiz simultaneously. Client1 inputs
their answer to question 1 first, and chooses 'grapes'. Before client1
finishes the quiz client2 submits their answer to question 1 as
'oranges'. When our app goes to fetch the results of client1, their
'grapes' answer will have been overwritten by 'oranges'. Afterall, we've
only implimented one global dictionary for our entire client base. Oups.

#### Finally, adding Cookies!

At this point Margo and I weren't really sure how to solve this issue.
How do we keep track of which answer corresponds to which client? For
advice, we turned to our trusted friend
[Greg](http://www.greghendershott.com) who suggested we use cookies!

**What is a cookie, and how do I make one?**

A cookie is a very small peice of data that will be sent from a server
and stored temporarily on a client's computer. To create a cookie, the
server needs to include a 'Set-Cookie' header in their HTTP response to
the client. This will prompt the client's browser to create a 'cookie'
to store the specified data. When a browser has a cookie from our server
any HTTP request it sends to us will include a 'Cookie' header
containing the data we asked it to store.

**How does this help our situation?**

Margo and I used cookies to store every quiz answer submited from a
client. Then, when the client's browser sends our server an HTTP request
asking for their results page, this request will include all of that
client's quiz answers - stored in the form of cookies! Great!

Now lets talk about how we implimented this. To create cookies Margo and
I changed the constraints of our functions (the ones that URL's are
routed to) as follows:

-   Chapeau will now pass to these functions both the dictionary
    containing the request information and a client object. So these
    functions must now accept two parameters! The dicitonary accepted
    contains everything the previous one does, but also includes
    '{header: {all of the headers and their values}}'.
-   The functions must call Chapeau's render function: render(client,
    path/to/html/file, args, header) before returning None.

Now that *all* of the request information is passed to the developper,
cookies can be read. Since the developer is now also in charge of
calling the render function, they have control over any headers they
want to include in their response. The header parameter in the render
function is optional, and when unspecified it will be set to None. The
args parameter is a dictionary of variables that we want to pass to the
html file. So, in our buzz-feed-style-quiz, every client's answer will
be saved in a cookie. When we want to render the results page all of the
incoming cookies can be read from the inputed dictionary of request
information. We can create another dictionary out of the received
cookies and can pass this dictionary into our render function to be
passed to our html file. Yay!

Thanks Margo for working on this project with me, its been an adventure!

