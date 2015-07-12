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
1. Activate my virtual environment! :)
1. write documents in markdown in the content folder
2. execute the command `pelican` to take all of the files in the content folder and transform them into html files in the 'output' folder
2. use the command 'make devserver' to start up my localhost and see how my website would look.  updates will appear 
automatically on my localhost as I chance any of my source files.  At this point, changes have NOT been pushed to github.
3. 'make stopserver' when I want to stop the localhost
4. when I am happy with my markdown files, commit them locally.
5. "git push origin source" to push the updated commit to my github 'source' branch (i.e. as backup for my source files!)
6. use "make github" to push my output html files to my github master branch, effectively updating my blog with 
the new post.
7. When I'm done working on this for the day, deactivate my virtualenv. 


