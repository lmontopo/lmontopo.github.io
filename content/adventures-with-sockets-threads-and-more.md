Title: Adventures with sockets, threads and more!
Date: 2014-11-11 05:00
Author: Leta Montopoli
Slug: adventures-with-sockets-threads-and-more

For a while now I've wanted to learn more about the internet, about
servers, and about how web apps *really* work. Last week I finished a
small flaks tutorial. I enjoyed the tutorial and I learned some cool
things by doing it, yet, I was feeling unsatisfied. The tutorial just
didn't hit the spot for me. I wasn't really sure what I was after, but I
knew it was something deeper. Yesterday I discovered sockets, and it was
dead on!

This blog post is going to be a (not so) little write up of some things
I've learned as I digging around in the world of sockets and other
networky type things. I'll start with a few questions I was thinking
about yesterday. I'll provide what I think are some decent and mostly
true answers to these questions. (Of course, if you find something in
this post that is just outright wrong, please do reach out to correct
me!). Then I'll introduce some code Susan and I wrote to make a simple
web chat service using sockets. Finally, a second round of questions and
answers will be presented. Enjoy!

#### QUESTIONS ROUND 1

##### What's a socket?

This is a question I've spent a great deal of time trying to answer.
Here's the answer I've settled on: A socket is some sort of abstract
object like that of a "file" on your computer. We could say that the
object type "socket" is built into the operating system of our computer
and allows users (or programs) to create instances of them at will.
Sockets are used as the endpoints of any bidirectional communication
channel. The socket contains the FROM IP address, the TO IP address, the
FROM port number, and the TO port
number.^[1](http://lmontopo.github.io/feeds/leta-montopoli.rss.xml#fn:fn-1)^
We can think about the function of sockets to be like plugging chords
into walls on the two ends of your communcation channel.

##### How does my computer communicate with my router?

The short answer: via radio signals. Modern computers come with a built
in wireless adapter which translates data from your computer into radio
waves. These radio waves can then be sent out into the world and picked
up by a router. Communication can occur in the other direction as well:
The router can send radio waves to a comptuer and the computer will
translate those waves into 0s and 1s so that it can understand the
message. One thing that I found interesting is that my computer is
always listening to the router. Sometimes my computer will hear messages
that aren't even addressed to it, in which case it won't accept these
messages. So there's a difference between "listening" and "accepting"
messages from the router. We'll come back to this!

##### Can older computers connect to the internet?

It depends. If your computer has the necessary internet handling
software but is simply lacking a translater, then yes. The modem,
afterall, is simply a translator. It takes signals (probably passed to
it through your phone line) and transforms these messages into 0s and 1s
that your computer can understand. But, this only makes your computer
internet ready if you're operating system can create sockets, and can
understand and work with internet protocols. Otherwise, extra software
would have to be implimented and I'm not exactly sure if this can always
be done.

##### SOME CODE

To learn more about sockets Susan and I implimented a chat service
between our two computers using sockets. I wrote the code for the
"server", and she wrote the code for the "client". If I ran 'server' on
my computer and then she ran 'client' on hers, we were able to chat back
and forth in our terminals! Anything I wrote in my terminal would be
sent to hers the moment I pressed enter. Likewise, messages she typed in
her terminal would be sent to mine when she pressed enter. It was like a
real world chat service! Here's our code:

```python
###SERVER (On Leta's Computer)im
port socketimport threadingserversoc
ket = socket.socket()port = 9999# c
lears the port right away preventing
"address already in use" errorsserv
ersocket.setsockopt(socket.SOL_SOCKE
T, socket.SO_REUSEADDR, 1)my_ip = 10
.0.7.65serversocket.bind((my_ip , po
rt))# queue up to 5 requests:servers
ocket.listen(5)clientsocket, addr =
serversocket.accept()def listen(conn
ection):    while True:        msg =
clientsocket.recv(1000)        if n
ot msg:            break        else
:            print 'friend says', ms
gdef write(connection):    while Tru
e:        message = raw_input('')
clientsocket.sendall(message)
clientsocket.close()t = thread
ing.Thread(target = write, args = [c
lientsocket])r = threading.Thread(ta
rget = listen, args = [clientsocket]
)t.start()r.start()

```

```python
#CLIENT (on Susan's computer)imp
ort socketimport threadingdef server
():    sock = socket.socket(socket.A
F_INET, socket.SOCK_STREAM)    HOST=
''    SOCKET_LIST = []    RECV_BUFF
ER = 4096    PORT = 9999    server_a
ddr = ("10.0.7.65", PORT)    print >
>sys.stderr, 'connecting to %s port
%s' % server_addr    sock.connect(se
rver_addr)    try:        t=threadin
g.Thread(target=send, args=[sock])
t.start()        print "hi!!!!
TESTING!!"        while True:
data = sock.recv(RECV_BUFFER)
print >>sys.stderr, 'Leta
says: %s' % data    finally:
print >>sys.stderr, 'closing socket
'        sock.close()

```

#### QUESTIONS ROUND 2

##### What is happening when I write "socket.listen"?

As mentioned earlier, your computer is constantly "listening" to
messages from your router. But its not necessarily ACCEPTING them.
Calling socket.listen() tells your computer to actively start accepting
messages that are addressed to the socket. So, as soon as my computer
sees some message addressed to a socket which has been told to listen,
the socket will send back a message saying something like, "OK, I am
willing to receive your message". And then the message will be sent and
received. (At least I think thats kind of how it goes.)

##### What is TCP? What is IP? Are they related?

TCP stands for Transmission Control Protocoll. IP stands for Internet
Protocol. Both are "protcols" in the sense that they outline the
standards by which machines are supposed to communicate with each other.
To see how they differ, lets walk through how Susan's and my computer
are dealing with our 'chat server'. Suppose I send the message "hello"
to Susan. When I send this message to Susan the string "hello" will be
wrappred with extra data necessary to satisfy TCP. Once this mesage
satisfies TCP it can be sent to my operating system, which will look at
it, realize that data needs to be sent out in the world, and will
package the data with yet another layer so it adheres to IP. This
message is then translated to radio waves to be sent to the router. Upon
receiving my message the router will pass the package to Susan's
computer. When Susan's computer receives the package it translates the
data back into 0s and 1s and then begins unpacking it. Her operating
system will take off the outtermost layer of packaging: that associated
with IP. Her computer will find that the contents of this package adhere
to TCP. Susan's computer will make sure that TCP is followed. Since TCP
is a protocol which ensures that messages are sent in order, this means
that within the TCP packaging Susan's computer might find some data that
says "Hey! I'm packet number 13 sent from Leta's computer to yours. Have
you gotten package 1 through 12 already? You can't open me up until
you've received all the ones that come before." And her computer will
respond saying something like "Yes, I have gotten all the messages that
come before, so I can now open you up". Susan's computer will then pass
the package to the application (the chat service) which will unpack the
data to find the message I sent: "hello".

I know this is pretty confusing. I'm still wrestling with these concepts
myself. Lets recap: On the senders side, the package gets wrapped with
all sorts of layers and then this package gets passed around, and on the
receivers side, the package gets unpacked layer by layer. Each layer is
associated with another protocol. Underneath the IP packaging, data can
be sent adhering to TCP or adhering to other protocols. Indeed, TCP is
not the only one. As I mentioned above, TCP is a protocol that ensures
that data is sent in a particular order, and it ensures that a response
be sent back to the sender to communicate if/when the data was received.
Another protocol is UDP: User Datagram Protocol. It does not ensure that
delivery has occured and does not ensure that messages are delivered in
order. We're not going to get into why UDP might be used over TCP, but
the point I wanted to make was that IP can encapsulate many different
types of messages. TCP is just the one that happened to be used in the
chat server Susan and I implimented.

##### What is a thread?

Have you ever heard the term "multi-threaded programming" and wondered
what the heck people were talking about? If so, read on! Consider a chat
server where I could type a message to Susan, and then I couldn't type
one again until I had her response. That would kind of suck, wouldn't
it? So what this means is that in a good chat service, my server can be
waiting for me (the user) to input a message, and can simultaneously be
listening for any incoming messages from Susan. The key here is that we
want our program to be doing **two things simultaneously**. Looking at
the code for Server, above, we see that what I want is for the function
"write" and the function "listen" to be running concurrently. And the
way I implemented this was through threads. Each thread refers to a
different task that we want to be carried out, and threading is the
process of running them simultaneously. Conclusion: Threading rocks!

##### Are sockets being used when I use my browser to visit a webpage?

YES! Often multiple sockets are used to transfer the information of one
a single webpage to your computer. Generally speaking, each HTTP request
has its own socket that it connects with. This socket will close as soon
as the request has been made and received. Some web pages have 100s of
GET or POST (or other) HTTP requests. This means that 100s of sockets
will be created, opened, and closed on my computer in the short time it
takes to load the webpage in my browser. I have been told that this is
actually starting to change. I don't know very mucha about this, but I
think HTTP is starting to allow a single socket to handle more than one
HTTP requests.

<div class="footnote">

------------------------------------------------------------------------

1.  <div id="fn:fn-1">

    </div>

    A Port is just this idea that we've implimented on our computers so
    that we can have several things going on on one computer. Its kind
    of like apartments on an apartment building. If we have to have
    several separate things going on at different addresses within the
    same machine, ports is the way we've done
    that. [↩](http://lmontopo.github.io/feeds/leta-montopoli.rss.xml#fnref:fn-1 "Jump back to footnote 1 in the text")

</div>