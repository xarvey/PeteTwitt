#!/usr/bin/python

# Import the CGI, string, sys modules
import cgi, string, sys, os, re, random
import cgitb; cgitb.enable()  # for troubleshooting
import sqlite3
import session

#Get Databasedir
MYLOGIN="xiao67"
DATABASE="/homes/"+MYLOGIN+"/PeteTwitt/tweet.db"
IMAGEPATH="/homes/"+MYLOGIN+"/PeteTwitt/images"

##############################################################
# Define function to generate login HTML form.
def login_form():
    html="""
<HTML>
<HEAD>
<TITLE>Purdue Twitt</TITLE>
     <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="http://getbootstrap.com/assets/ico/favicon.ico">
    <title>Bootstrap 101 Template</title>

    <!-- Bootstrap -->
    <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" rel="stylesheet">
	<!-- Custom styles for this template -->
    <link href="http://getbootstrap.com/examples/signin/signin.css" rel="stylesheet">	

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
</HEAD>

<BODY BGCOLOR = white>


 <div class="container">

      <form class="form-signin" role="form" METHOD=post ACTION="login.cgi">
        <h2 class="form-signin-heading">Please sign in</h2>
        <input type="email" class="form-control" placeholder="Email address" required="" autofocus="" NAME="username">
        <input type="password" class="form-control" placeholder="Password" required="" NAME="password">
        <label class="checkbox">
          <input type="checkbox" value="remember-me"> Remember me
        </label>
	<INPUT TYPE=hidden NAME="action" VALUE="login">
        <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
	<br>
	Don't have an account?
	<button class="btn btn-primary btn-lg btn-block" data-toggle="modal" data-target="#myModal" align="right">
  		Sign Up
	</button>
	</form>
    

    </div> <!-- /container -->


<!-- Modal -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title" id="myModalLabel">Sign Up</h4>
      </div>
      <div class="modal-body">
          <form class="form-signin" role="form" METHOD=post ACTION="login.cgi">
        <h2 class="form-signin-heading">Please sign up</h2>
        <input type="email" class="form-control" placeholder="Email address" required="" autofocus="" NAME="username">
        <input type="password" class="form-control" placeholder="Password" required="" NAME="password">
	<INPUT TYPE=hidden NAME="action" VALUE="sign-up">
        <button class="btn btn-lg btn-primary btn-block" type="submit">Sign up</button>
	</form>
	
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>



  <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
</BODY>
</HTML>
"""
    print_html_content_type()
    print(html)


###################################################################
# Define function to test the password.
def check_password(user, passwd):

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    t = (user,)
    c.execute('SELECT * FROM users WHERE email=?', t)

    row = stored_password=c.fetchone()
    conn.close();

    if row != None: 
      stored_password=row[1]
      if (stored_password==passwd):
         return "passed"

    return "failed"

###################################################################
# Define function to sign up new user
def sign_up(user, passwd) :
	conn = sqlite3.connect(DATABASE)
    	c = conn.cursor();
	
	t = (user,)
	c.execute('SELECT * FROM users WHERE email=?', t)

	row = c.fetchone()
	
	if row == None: 
		u = (user,passwd)
		c.execute('INSERT INTO users VALUES(?,?)',u)
		conn.commit()
		conn.close()
		return "passed"
	
	conn.close()
	return "failed"

##########################################################
# Diplay the options of admin
def display_admin_options(user, session):
    html="""
        <!DOCTYPE html>
<!-- saved from url=(0038)http://getbootstrap.com/examples/blog/ -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="http://getbootstrap.com/assets/ico/favicon.ico">

    <title>Blog Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="http://getbootstrap.com/examples/blog/blog.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy this line! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  <style id="holderjs-style" type="text/css"></style></head>

  <body>

    <div class="blog-masthead">
      <div class="container">
        <nav class="blog-nav">
          <a class="blog-nav-item active" href="http://getbootstrap.com/examples/blog/#">Home</a>
          <a class="blog-nav-item" href="http://getbootstrap.com/examples/blog/#">New features</a>
          <a class="blog-nav-item" href="http://getbootstrap.com/examples/blog/#">Press</a>
          <a class="blog-nav-item" href="http://getbootstrap.com/examples/blog/#">New hires</a>
          <a class="blog-nav-item" href="http://getbootstrap.com/examples/blog/#">About</a>
        </nav>
      </div>
    </div>

    <div class="container">

      <div class="blog-header">
        <h1 class="blog-title">Purdue Twitt Main Page</h1>
      </div>

      <div class="row">

        <div class="col-sm-8 blog-main">

          <ul class="pager">
            <li><a href="http://getbootstrap.com/examples/blog/#">Previous</a></li>
            <li><a href="http://getbootstrap.com/examples/blog/#">Next</a></li>
          </ul>

        </div><!-- /.blog-main -->

        <div class="col-sm-3 col-sm-offset-1 blog-sidebar">
          <div class="sidebar-module sidebar-module-inset">
            <h4>About</h4>
            <p>Purdue Twitt is a Twitter-like Web application written in Python for CS390-Python</p>
          </div>
        </div><!-- /.blog-sidebar -->

      </div><!-- /.row -->

    </div><!-- /.container -->

    <div class="blog-footer">
      <p>
        <a href="http://data.cs.purdue.edu:6500/PeteTwitt/login.cgi">Back to top</a>
      </p>
    </div>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="./Blog Template for Bootstrap_files/jquery.min.js"></script>
    <script src="./Blog Template for Bootstrap_files/bootstrap.min.js"></script>
    <script src="./Blog Template for Bootstrap_files/docs.min.js"></script>
  

</body></html>
        """
        #Also set a session number in a hidden field so the
        #cgi can check that the user has been authenticated

    print_html_content_type()
    print(html.format(user=user,session=session))

#################################################################
def create_new_session(user):
    return session.create_session(user)

##############################################################
def new_album(form):
    #Check session
    if session.check_session(form) != "passed":
       return

    html="""
        <H1> New Album</H1>
        """
    print_html_content_type()
    print(html);

##############################################################
def show_image(form):
    #Check session
    if session.check_session(form) != "passed":
       login_form()
       return

    # Your code should get the user album and picture and verify that the image belongs to this
    # user and this album before loading it

    #username=form["username"].value

    # Read image
    with open(IMAGEPATH+'/user1/test.jpg', 'rb') as content_file:
       content = content_file.read()

    # Send header and image content
    hdr = "Content-Type: image/jpeg\nContent-Length: %d\n\n" % len(content)
    print hdr+content

###############################################################################

def upload(form):
    if session.check_session(form) != "passed":
       login_form()
       return

    html="""
        <HTML>

        <FORM ACTION="login.cgi" METHOD="POST" enctype="multipart/form-data">
            <input type="hidden" name="user" value="{user}">
            <input type="hidden" name="session" value="{session}">
            <input type="hidden" name="action" value="upload-pic-data">
            <BR><I>Browse Picture:</I> <INPUT TYPE="FILE" NAME="file">
            <br>
            <input type="submit" value="Press"> to upload the picture!
            </form>
        </HTML>
    """

    user=form["user"].value
    s=form["session"].value
    print_html_content_type()
    print(html.format(user=user,session=s))

#######################################################

def upload_pic_data(form):
    #Check session is correct
    if (session.check_session(form) != "passed"):
        login_form()
        return

    #Get file info
    fileInfo = form['file']

    #Get user
    user=form["user"].value
    s=form["session"].value

    # Check if the file was uploaded
    if fileInfo.filename:
        # Remove directory path to extract name only
        fileName = os.path.basename(fileInfo.filename)
        open(IMAGEPATH+'/user1/test.jpg', 'wb').write(fileInfo.file.read())
        image_url="login.cgi?action=show_image&user={user}&session={session}".format(user=user,session=s)
        print_html_content_type()
	print ('<H2>The picture ' + fileName + ' was uploaded successfully</H2>')
        print('<image src="'+image_url+'">')
    else:
        message = 'No file was uploaded'

def print_html_content_type():
	# Required header that tells the browser how to render the HTML.
	print("Content-Type: text/html\n\n")

##############################################################
# Define main function.
def main():
    form = cgi.FieldStorage()
    if "action" in form:
        action=form["action"].value
        #print("action=",action)
        if action == "login":
            if "username" in form and "password" in form:
                #Test password
                username=form["username"].value
                password=form["password"].value
                if check_password(username, password)=="passed":
                   session=create_new_session(username)
                   display_admin_options(username, session)
                else:
                   login_form()
                   print("<H3><font color=\"red\">Incorrect user/password</font></H3>")
	elif (action == "sign_up"):
		#Create new account
		if "username" in form and "password" in form:
               		#Test password
			username=form["username"].value
			password=form["password"].value			
			if sign_up(username,password) == "passed":
				session=create_new_session(username)
				login_form()
			else:
				login_form()
				print("<H3><font color=\"red\">Username already exists.</font></H3>")
        elif (action == "new-album"):
	  new_album(form)
        elif (action == "upload"):
          upload(form)
        elif (action == "show_image"):
          show_image(form)
        elif action == "upload-pic-data":
          upload_pic_data(form)
        else:
            login_form()
    else:
        login_form()

###############################################################
# Call main function.
main()
