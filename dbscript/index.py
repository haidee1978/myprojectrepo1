import psycopg2

def getmovieinfo():
    constr = """
    dbname = "'heideedb'"
    user = 'heidee'
    password = 'heidee123'
    host = 'pythonista.learning.edu'
    """
    conn = psycopg2.connect(constr)
    curr = conn.cursor()
    curr.execute("select * from Cd_details")
    rows = curr.fetchall()
    return rows[0]

def index(req):

    header = """
	<!DOCTYPE html>
<html lang=en>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="../../docs-assets/ico/favicon.png">

    <title>Jumbotron Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="jumbotron.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy this line! -->
    <!--[if lt IE 9]><script src="../../docs-assets/js/ie8-responsive-file-warning.js"></script><![endif]-->

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="bootstrap/js/html5shiv.js"></script>
      <script src="bootstrap/js/respond.min.js"></script>
    <![endif]-->

  </head>
	    """
    bodybegin = """
       <body>
        <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand">Haidee Rental System</a>
        </div>
        <div class="navbar-collapse collapse">
          <form class="navbar-form navbar-right" role="form">
            <div class="form-group">
              <input type="text" placeholder="Email" class="form-control">
            </div>
            <div class="form-group">
              <input type="password" placeholder="Password" class="form-control">
            </div>
            <button type="submit" class="btn btn-success">Sign in</button>
          </form>
        </div><!--/.navbar-collapse -->
      </div>
    </div>

    <!-- Main jumbotron for a primary marketing message or call to action -->
    <div class="jumbotron">
      <div class="container">
        <h1>Welcome to Haid's Movie World</h1>
        <p>Where your journey starts here...</p>
        <p><a class="btn btn-primary btn-lg" role="button">Have a nice day.. &raquo;</a></p>
      </div>
    </div>
    <div class="container">
      <!-- Example row of columns -->
      <div class="row">
        <div class="col-md-4">
        <a href="http://pythonista.learning.edu/~heidee/movie2.py"<h2>Movie Details</h2></a>
          <p>Star Trek Into Darkness,Elysium,Pacific Rim,Oblivion,After Earth,Man of Steel, World War Z Riddick,Iron Man 3,Ender's Game,Gravity,The World's End, The Wolverine,Europa Report,The Host,The Purge,The Hunger Games: Catchin...,Thor the Dark World,About Time,G>I Joe:Retaliation</p>
          <p><a href="http://pythonista.learning.edu/~heidee/movie2.py" class="btn btn-default" role="button">view details &raquo;</a></p>
        </div>
        <div class="col-md-4">
        <a href="http://pythonista.learning.edu/~heidee/customer.py"<h2>Customer Details</h2></a>
          <p>This Is The End,We're the Millers,The Heat,The World's End,Grown Up2, Don Jon, Identity Theif,The Hangover Part III,Movie 43,Dispicable Me2,Scary Movie 5,Grand Masti,The Increible Burt Wonderstane,The Interneship,Monster University'. </p>
          <p><a href="http://pythonista.learning.edu/~heidee/customer.py" role="button"> view details &raquo;</a></p>
       </div>
        <div class="col-md-4">
        <a href="http://pythonista.learning.edu/~heidee/returned.py"<h2> Returned CDs</h2></a>
          <p>The Place Beyond the Pines, Mud, The Butler,The Great Gatsby,Fruitvale Station,The Spectacular Now,Blue jasmine,Pain & Gain,World War Z,Don Jon,White House Down,Before Midnight,Elysium, Man of Steel, Spring Breakers, percy Jackson: Sea Monsters,The iceman,Side Effects,Runner,Runner,12 Years Slave</p>
          <p><a class="btn btn-default" href="#" role="button">View details &raquo;</a></p>
        </div>
      </div>

      <hr>

      <footer>
        <p>&copy; The Pride of Southern Mindanao Colleges</p>
      </footer>
    </div> <!-- /container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="../../dist/js/bootstrap.min.js"></script>
    """
    bodyend = """
           <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
             <script src="https://code.jquery.com/jquery.js"></script>
           <!-- Include all compiled plugins (below), or include individual files as needed -->
           <script src="js/bootstrap.min.js"></script>
           </body>
           </html>
    """

    panelbegin = """
      <div class="panel panel-default">
      <!-- Default panel contents -->
      <div class="panel-heading">Listing</div>
      <div class="panel-body">
      """
    tablebegin = """<table class="table table-hover table-condensed">"""
    tableend = "</table>"
    panelend = """
       </div>
      </div>
    """


    return header + bodybegin + panelbegin + tablebegin + tableend + panelend + bodyend
