Title: The struggles I had setting up this site.
Date: 2014-10-08 04:00
Author: Leta Montopoli
Slug: the-struggles-i-had-setting-up-this-site
Categories: Blog

For me, setting up my blog was not easy. I think part of this was that I
was impatient, and part of this was because IT IS HARD! I ran into many weird error
messages and I began to get quite impatient and frustrated. Thankfully I got Allison to help
me, and together we figured out what was going on and got things up and running. Here I will
explain what went wrong for me and how I fixed it. If you encounter similar difficulties, hopefully this
article will help you.

The main struggle I encountered began when I tried to publish my page
through Github. There are two different ways one can go about doing this: either as a
project page, or as a user page. Without knowing there was another option, I began
creating my blog as a Github project page. In order to do this, I had to create a repository
on Github, and then create branch of the repository called "gh-pages". "gh-pages" is where I
needed to push the pelican created "output" folder containing all the necessary html to
create the page. To make this push happen, I made use of the "gh-import" package which
can be installed using pip.

Here is what needed to be done next:

```python
$ ghp-import output$ git push or
igin gh-pages

```

Here, the first line commits changes made in my output folder to the
gh-branch of my LOCAL repository. (Local meaning, the repository on my own computer, not the
one store on Github.) The second line of this code pushes these changes to the remote
repository's gh-pages branch (ie. the branch of the repository stored on github).Then, in about ten
minutes time, my website was created with url https:://lmontopo.github.io/blog. (here, lmontopo
is my username on github, and blog was the repository I created).

I wish this were the end of the story, but unfortunately it is not. What
I realized when my webpage was published is that none of pelican's styling information was
being received. My webpage was just a simple plain text webpage and it looked
extremely ugly. What was puzzling was that when I viewed the page source I saw a line in
the code specifying the location of the style sheet as:

```python
<link rel="stylesheet" href="/theme/css/main.css" />

```

But when I clicked on this href, it couldn't find the file. Then I
looked in my github repository, and searched for that stylesheet file. I found it. It was
there. So why couldn't my computer find it? Well, it turns out that my computer was looking at the
wrong url. It expected my css style sheet to be found at "username.github.io/theme/css/main.css",
but in reality it was located at "username.github.io/repositoryname/theme/css/main.css".

So, at this point I found out that there was such thing as a github user
page, and I decided to change my page to be one of those instead. I should
clarify that this was not necessary, and this was not the only way to solve my problem!
Had I decided to stay with the gh-pages website, I would have needed to change my default
root directory. This probably is quite easy, although to be honest I don't know exactly
how it is done.

Since I decided to change to a user github page, this is how I
proceeded: I needed to create a new repository called username.github.io. To
github, this is a magic repository name. Github will know that you are publishing a user webpage
from the contents of this repository and it will do the work for you (just as gh-pages was
a magical branch name for the project pages site.) Then I deleted my old repository. Now, I
needed to tell my computer to connect remotely with this new repository as opposed to the old one.
(Just because the old repository is deleted, doesn't mean my computer won't try to find it.)
To do this I type in:

```python
$ git remote rm origin 
$ git remote add username.github.io https://github.com/username/username.github.io
```

The first line here removes the connection I had to the previous (now
deleted) repository on Github.  The second line adds a remote connection to the repository named
username.github.io found at https://github.com/username/username.github.io.

Great, now all I had to do was push the contents of my local repository
to the main branch of my new remote repository as follows:

```python
$ ghp-import output
$ git push origin -f gh-pages:master
```

This created a lovely new webpage for me! Notice, though, that here I
had to FORCE the push. Quite honestly, I am not clear on why this is happening. For now, I have
decided to create a new local branch called "writing" and I will use this for all of my
version control. This way I can continue to force push without worrying about anything being lost.
This may not be the most sophisticated way of handling things, but being quite new to git, I
am more than satisfied with this solution.

Another little glitch that occurred along the way, and how I solved it:

In the process of playing around with my computer, I somehow deleted the
pelicanconf.py file that pelican creates for you when you quickstart. This is the file
that specifies all of your settings. Since it was gone, I had lost my title, and the
default title "A Pelican Blog" appeared. Obviously, this wasn't desirable. This ended up being a
really easy fix because all I needed was to re-create this file and save it the
directory where my "content" folder is found. Then it integrates itself (somewhat magically) into the
html files. Just make sure that you have the correct formatting, as specified on
pelican's documentation site: <http://docs.getpelican.com/en/latest/settings.html>

