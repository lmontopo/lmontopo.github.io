Title: Some things I learned when my computer crashed. 
Date: 2014-12-31
Categories: Blog

During my last two weeks at Hacker School I encountered some serious troubles with my computer.  Despite becoming overly emotional when I thought my computer was gone for good, I learned some cool things through this experience.  I learned some cool bash commands when [Casey][3] helped me try to diagnose the cause of my computer's distress.  Then, when my computer was unusable, I spent some time reading a bit about bash, and used Casey's computer to recover my blog. Finally, when I got my computer back in good health, I learned some lessons about good documentation practices and backing things up.  In this blog post I'll write about some of these things (and possibly digress into related topics as well): 

#### Bash Commands:

When Casey and I first realized my computer was abnormally slow, we tried to do some investigating.  We used some bash commands to see what processes were running and what system calls were being made.  Our hope was that we might detect a particular call that my computer was stuck on.  We didn't have much success with our investigation, but it was still super cool peaking behind the scenes!  Our experimentation also make me eager to learn more about the command line. So, while my computer was away being fixed, I spent some time away from the computer reading about bash. Here are some of the bash commands I've learned:

* `$ ps aux` : shows ALL current processes.  This is one of the commands Casey taught me while we were playing detective! 

* `$ dtruss` :  Another one that Casey taught me!  When dtruss is called on a particular process, your computer will show you all of the system calls that are happening for that process!  So cool! 

* `$ cal` : This one is kind of just for fun.  If you aren't familiar with this command, try it out! 

* `$ say something` :  This one is also just for fun.  The word 'something' can be replaced with whatever you want. [Cerek][2] tought me about this command when he made his computer sing rap lyrics. 

* `$ chmod` : changes the reading, writing and executing permissions of a file.  I read about this from a book, and then two days later I needed to use this command! I'll talk more in detail about this command in the next seciton. 

* `$ sudo` :  This is a command that I have been using for a while, and I thought I understood it.  My understanding was basically that there are certain commands that we don't have permission to call unless we first call `sudo` and provide our password.  While this is true, it misses the big picture of what sudo *does*.  I'll quote sudo's man page here because it provides a rather good explanation: "**sudo** allows a permitted user to execute a command as the superuser[^1] or as another user". In fact, `sudo another_user` can be called to carry out a command as if you were 'another_user'. Superuser is the default user which is used when no other user is specified.  So, calling `sudo` with no other argument will allow me to call commands as if I were the superuser and give me extra priveledges.  

* `$ alias alias_name="command"` : creates an alias for the command!  An **alias** is a shortcut for other bash commands.  A useful tutorial (with examples!) on this topic can be found [here][1].  Here is the first alias I made (with [Geoff][4]'s help!).  It is awesome and I highly recommend making one yourself. 

```bash
$ alias gr="log --graph --full-history --all --color --pretty=tformat:%x1b[31m%h%x09%x1b
[32m%d%x1b[0m%x20%s%x20%x1b[33m(%an)%x1b[0m -n15"
```

After making this alias I can just type `git gr` into my command line to produce a pretty graphical representation of my git log.  Great! 


#### What is SSH? 

Throughout hacker school I had heard the term "ssh" come up in conversation a few times, but I never paused to ask about it.  That is, until [Julia][6] set up an ssh server on "www.hackers.cool" and invited us to all get accounts! I learned some stuff about ssh, I set up an account on Casey's computer, and, once I got my computer back from being fixed, I transfered my account from Casey's computer to my own! Here's what I learned:

**SSH** stands for secure shell.  As far as I understand, it is a way that 'clients' can log onto a server computer remotely via a command line interface.  So, in terms of hackers.cool, once I had set up my account I could go into my terminal, type in `ssh leta@hackers.cool` and I would be remotely connected to the harckers.cool server!  Then, I could type in fun little things like "$ echo hey everyone", and the message would message appear not only in my terminal but on the server terminal and on everyone else's terminal who was ssh'ed in.  Another thing I can do after loggin in, is type 'irc' which stands for internet relay chat.  This will bring me to a an old school style chat room with other hackers.cool clients! 

**How I set up my hackers.cool account**:  
On www.hackers.cool you can click on "sing up here" for instructions.  It will ask you for a username and will ask you to provide a public ssh key. Then Julia will do somehting to add you to the system, and you should be good to go!  But **what is an ssh key**?  [Github][5] describes this well by saying that "SSH keys are a way to identify trusted computers without involving passwords".  I'm not exactly sure how they work, but some sort of cryptogrophy is involved for security. 

**How did I transfer my account from Casey's computer to my own?**  
Once my computer was back from the dead I had to figure out how to use my hackers.cool account from my own computer. I couldn't yet login by typing `ssh leta@hackers.cool` into my command line (I tried!).  Indeed, the public ssh key recognized by hackers.cool was actually on Casey's computer, not mine!  So, I grabbed a USB stick and moved the .ssh directory onto my computer.  I still wasn't able to log into hackers.cool.  When I tried to I got an error message.  I don't remember exactly now what the error message was, but it said something about the permissions of files in my .ssh directory not being secure enough.  It seemed to me that the permissions of these files must have changed during the transfer from Casey's computer to my own.  So I used **chmod** to change them!  Here are the details: 

**How I used chmod**:    	
I used the command `chmod 700 file` for both files within my .ssh directory.  The number 7 signifies permission to read, write ane execute.  The number 0 specifies no permissions at all. The first digit refers to the user's permissions, the second digit to the 'groups' permissions, and the third to the world.  So by specifying 700, I gave the user reading, writing and executing permissions but gave no permissions to anyone else. The next time I tried to log in with "ssh leta@hackers.cool" I was successful! (The [wikipedia page][7] gives a more thorough description of how chmod can be used.)

#### Tips about Pip:

It can actually be super helpful to keep track of any dependencies for a particular project.  I realized this when my computer crashed and none of my git repos included any meta-data about their dependencies. In the future I'm going to use this very easy way to keep track of my python dependencies for each project: 

1. First, setup a virtual environment for each project, with all of the dependencies installed in this virtual environment.  If this is my setup, then `pip freeze` will produce a list of all the pip packages installed for this project. (Note:  without a virtual environment for each project, `pip freeze` would simply produce a list of ALL dependencies for ALL projects.) 
2. Make a requirements page by typing: `pip freeze >> requirements.txt`.
3. Include the requirements page in my remote repo!
4. When I want to run a project on another computer I can run ` pip install -r requirements.txt` and all of the documented packages will be install by pip! Easy!  



#### Documenting Your Workflow and Backing Things Up

**Include source files in your github repo!**
When my computer crashed and I wanted to write a blog post from Casey's computer, it occured to me how much it sucked that I only saved my html output, and not my source files of my blog.  With the help of some awesome hackerschoolers, I was able to retreive some old files and get things back up and running.  But, the whole process would have been a lot smoother had I simply included my markdown files in my github repo! 

**Add a README with your workflow!**
Once I had Casey's computer all set up for me to work on my blog, I added a README file to my github repo, speciying my workflow.  This ended up helping me dramatically once I got my own computer back.  Sometimes in the moment I think "oh, I'll remember my workflow".  But maybe I won't!  It's worth taking a minute to include a readme with your workflow, in case you don't remmeber it. :) 

And generally.... **Back things up.**

<sub> [1]: The superuser is a fairly new concept to me, but this is what I understand so far: A superuser is a user on a computer that has all the special priveledges used for system administration.  Different operating system's have different names for the superuser.  This is not a user that you create  yourself on your computer, it is there without you doing anything.</sub>

[1]: https://www.digitalocean.com/community/tutorials/an-introduction-to-useful-bash-aliases-and-functions
[2]: http://todayincode.tumblr.com/
[3]: http://rodarmor.com/
[4]: http://www.zephyrizing.net/
[5]: https://help.github.com/articles/generating-ssh-keys/
[6]: http://www.flowerhack.com/
[7]: http://en.wikipedia.org/wiki/Chmod

