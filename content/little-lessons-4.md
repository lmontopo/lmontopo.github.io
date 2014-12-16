Title: Little Lessons Episode 4: Pip tips, bash scripts, ssh, and backing things up! 
Date: 2014-12-16
Categories: Blog

First of all, let me just clarify that I'm not really going to be talking about bash scripts, but more so just about some cool bash commands I've learned.  I just wanted to say 'bash scripts' instead of 'bash commands' because it rhymed with 'tips' and sounded super cool.  Sorry if this is dissapointing to anyone.  Maybe someday soon i'll actually talk abotu bash scripts!  Today, I hope you enjoy the following: 

##### Here are some Tips about Pip:

You can type into the command line:

```
$ pip freeze
```
and it will list out all of the packages you have installed via pip.  This is great because then you can quickly make a `requirements.txt` file, include it in your git repository, and then anyone who clones your project can simply write:

```
pip install -r requirements.txt
```
and all of the documented packages will automatically be install by pip! So cool!  I have recently used this is my repository for 


