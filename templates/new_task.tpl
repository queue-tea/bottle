<font face="verdana">
		<p style="height:100%; position: fixed; z-index: 1;
			top: 0; left: 0; background-color: #FFC7C7;
			overflow-x: hidden; padding-top: 20px;">
	  <a href="https://www.w3schools.com/html/html_forms.asp">How to
			make HTML <br> forms</a><br><br></p>

  <header>
		<style>
		h1 {margin-left: 160px; padding: 0px 10px;
			background-color: #7ECDE0}
		</style>
	</header>

	<body>
		<h1>CMPS183: Homework 3</h1>
		<div style="margin-left: 160px; padding: 0px 10px;">
				<a href="/index">Home</a>
				<a href="/list">To Do List</a>
				<a href="/new">To Do Form</a><br>

				<form action="/new" method="GET">
					Task name:<br>
				  <input type="text" name="task"><br>
					Description:<br>
					<input type="text" size="30" name="description"><br>
					Due date:<br>
					<input type="date" name="due"><br>
				  <input type="submit" name="save" value="save">
				</form>
		</div>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
		<script src="js/todo.js"></script>
	</body>
	<footer>
		<p style="margin-left: 160px; bottom: 0; padding: 0px 10px;
			background-color: #7ECDE0">
	  <a href="#">About Us</a>
		<a href="#">Contact</a>
		<a href="#">Privacy</a>
		<a href="#">Credits</a></p>
	</footer>
