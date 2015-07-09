lmontopo.github.io
==================


This is the repository containing everything related to my blog.  The 'source' branch contains all of my .md files,
while the 'master' branch contains all of the resulting html files.  The 'master' branch is the one that github is 
using to publish my blog. 

##### Instructions for getting this blog setup on another computer (i.e. in case mine crashes!):

1. clone my repository
2. create a virtual environment
3. pip install -r requirements.txt
4. start writing and publishing with my usual workflow

##### This is my workflow:
1. write documents in markdown in the content folder
2. use the command 'make devserver' to start up my localhost and see how my website would look.  updates will appear 
automatically on my localhost as I chance any of my source files.
3. 'make stopserver' when I want to stop the localhost
4. when I am happy with my markdown files, commit them locally.
5. "git push origin source" to push the updated commit to my github 'source' branch
6. use "make github" to push my output html files to my github master branch, effectively updating my blog with 
the new post.



