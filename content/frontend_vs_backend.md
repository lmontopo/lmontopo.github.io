Title: What's frontend, what's backend?
Date: 2016-11-06 05:00
Author: Leta Montopoli
Slug: frontend-backend
Category: Blog
Tags: Web


Last week a co-worker of mine asked me to clarify for him what the difference was between backend and frontend web development.  I had been asked this quesiton before, but this was the first time I felt I provided a clear explanation and was able to instill knowledge.

So, here, I'd like jot down a lof of the key points which I think helped to clarify the meaning of and the difference between 'frontend' and 'backend' development:

* **Backend code is run on the server computer while frontend code is run on the client computer.**  
* Being a *fullstack developer* means that you write (or can write) both backend and frontend code. 
* The backend takes care of any logic that the server needs to run before a response can be sent to the client.  This includes things like retreiving data from a database, authenticating a user or making some calculations.
* The frontend code takes care of any logic that needs to run locally - on the clients computer - in response to user interactions.  This includes any subsequent network calls for updated data.
* Frontend code is usually written in JavaScript, which your browser can interpret.

#### Why can't I write frontend in Python (or can I)?
* Just like all browsers know how to turn HTML and CSS into pretty pages, all browsers know how to 
interpret JavaScript;  **All browsers have built in JavaScript interpreters.** 
    * Check it out!  In Chrome right click on a page and click on the 'inspect'.  Then click on the 'console' tab.  You are now looking at a JavaScript Interpreter!  For fun, write the following: `alert('Leta is cool')`.
* Python interpreters aren't currently built into browsers.  It's not that they *couldn't be* it's just that they *aren't*.  If I wanted to write frontend logic in Python I'd have two choices: 
    1. Write a browser plugin to be able to interpret Python, and prompt users to install it to view my web app. *(This type of thing has been done in order to run Java on the frontend! Remember those annoying Java plugin installation promps?)*
    2. Compile my Python code down to JavaScript before sending it to the client.  This is a bit of a hack, though, because technically javaScript is still what would be running on the client side.


#### Where do HTML and CSS fit in?

* Often HTML and CSS are considered frontend.  The reason being is that, like JavaScript, they are interpreted by your browser.
* I consider HTML to be backend only in the context of a template that will be compiled by a template enginge.  In this case one is writting an HTML page with added template language logic which will render more HTML depending on the data that is fed into it. 
* To me, this falls under the backend umbrella because the templatign engine will turn this template into a finished HTML file on the surver side before sending the final HTML file to the client.
* Some people agree with me on this distinction, others disagree (and that's OK!)

#### Further readings

If you're curious to know a little more, specifically about why / how JavaScript became the only language built into browsers, I recommend reading [this](https://www.reddit.com/r/learnprogramming/comments/3frml2/why_is_javascript_the_only_frontend_programming/?st=iv70e8ah&sh=d65bf9be) thread on reddit.  I found it to be well explained and pretty thorough! 