<script type="text/javascript" src="temp.js"></script>

<?php

include 'api.php';

ob_start();
print_r($_FILES);
    file_put_contents("log.txt", ob_get_clean(), FILE_APPEND);
if($_FILES["file-upload"]["tmp_name"])
{
  if(!$_FILES["file-upload"]["error"])
  {
    file_put_contents("log.txt", $_FILES["file-upload"]["tmp_name"], FILE_APPEND);
      unlink("test/test.jpg");
    move_uploaded_file($_FILES["file-upload"]["tmp_name"], "test/test.jpg");
  }
    else
    {
    file_put_contents("log.txt", "Error1", FILE_APPEND);
    }
}
else
{
    file_put_contents("log.txt", "Error2", FILE_APPEND);
}

$path = 'test/test.jpg';
$type = pathinfo($path, PATHINFO_EXTENSION);
$data = file_get_contents($path);
$base64 = base64_encode($data);
 
//echo $base64;
 
$json = python_api($base64);
 

 
echo '<script> var json =' . $json . '; console.log(json);</script>';

?>

<!-- Compiled and minified CSS -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.5/css/materialize.min.css">

<!-- Material Design Icons courtesy of Google -->
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

<!--Import jQuery before materialize.js-->
<script src="https://code.jquery.com/jquery-1.9.1.min.js"></script>

<!-- Compiled and minified JavaScript -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.5/js/materialize.min.js"></script>

<!-- Turn the menu links into a hamburger icon -->
<script>
	$( document ).ready(function(){
		$(".button-collapse").sideNav();
	});
</script>
<style>

tr:nth-child(even){
  background-color: #acc0e0;
}

</style>


<html>
<head>
	<title>CodeOn - Team CHARUSAT</title>


</head>

<body bgcolor="#E6E6FA">

	<nav>
		<div class="nav-wrapper">
			<a href="#!" class="brand-logo">Team CHARUSAT</a>
			<a href="#" data-activates="mobile-demo" class="button-collapse"><i class="material-icons">menu</i></a>
			<ul class="right hide-on-med-and-down">
				<li><a href="menu1.html">Menu 1</a></li>
				<li><a href="menu2.html">Menu 2</a></li>
				<li><a href="menu3.html">Menu 3</a></li>
				<li><a href="menu4.html">Menu 4</a></li>
			</ul>
			<ul class="side-nav" id="mobile-demo">
				<li><a href="menu1.html">Menu 1</a></li>
				<li><a href="menu2.html">Menu 2</a></li>
				<li><a href="menu3.html">Menu 3</a></li>
				<li><a href="menu4.html">Menu 4</a></li>
			</ul>
		</div>
	</nav>
<br/>
<br/>

<center>
	<img src="test/test.jpg" alt="Image" height="70%" width="40%">
</center>
<br /><br />
	<div id="databaseholder"></div>


	<br/>
	<br/>
	<br/>

	<footer class="page-footer">
		<div class="container">
			<div class="row">
				<div class="col l6 s12">
					<h5 class="white-text">Team CHARUSAT</h5>
					<p class="grey-text text-lighten-4">Team CHARUSAT</p>
				</div>
				<div class="col l4 offset-l2 s12">
					<h5 class="white-text">Links</h5>
					<ul>
						<li><a class="grey-text text-lighten-3" href="#!">Link 1</a></li>
						<li><a class="grey-text text-lighten-3" href="#!">Link 2</a></li>
						<li><a class="grey-text text-lighten-3" href="#!">Link 3</a></li>
						<li><a class="grey-text text-lighten-3" href="#!">Link 4</a></li>
					</ul>
				</div>
			</div>
		</div>
		<div class="footer-copyright">
			<div class="container">
<!--				© 2018 Copyright Team CHARUSAT
				<a class="grey-text text-lighten-4 right" href="#!">More Links</a> -->
			</div>
		</div>
	</footer>
	
	<script>
		addData(json);
	</script>
	
</body>

</html>
