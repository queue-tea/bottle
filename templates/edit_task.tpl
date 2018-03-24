<!doctype html>
<html>
<font face="verdana">
		<p style="height:100%; position: fixed; z-index: 1;
			top: 0; left: 0; background-color: #FFC7C7;
			overflow-x: hidden; padding-top: 20px;">
	  <a href="https://www.w3schools.com/tags/tag_style.asp">How to
			style HTML <br> without a CSS file</a><br><br>
		<a href="https://www.w3schools.com/html/html_formatting.asp">
		How to format text <br> in HTML text</a><br><br>
		<a href="https://www.w3schools.com/html/html_images.asp">
		How to add images <br> in HTML </a><br><br>
		<a href="https://www.w3schools.com/html/html_tables.asp">
		How to make tables <br> in HTML </a></p>

  <header>
		<style>
		h1 {margin-left: 160px; padding: 0px 10px;
			background-color: #7ECDE0}
		</style>
	</header>

	<body>
		<h1>CMPS183: Homework 2</h1>
		<div style="margin-left: 160px; padding: 0px 10px;">
		<form action="/edit/{{no}}" method="get">
			Task name:<br>
		  <input type="text" name="task" value="{{old[0]}}"><br>
			Description:<br>
			<input type="text" size="30" name="description"><br>
			Due date:<br>
			<input type="date" name="due"><br>
		  <select name="status">
		    <option>complete</option>
		    <option>incomplete</option>
		  </select>
		  <br>
		  <input type="submit" name="save" value="save">
		</form>
	  </div>
	</body>
	<footer>
		<p style="margin-left: 160px; bottom: 0; padding: 0px 10px;
			background-color: #7ECDE0">
	  <a href="#">About Us</a>
		<a href="#">Contact</a>
		<a href="#">Privacy</a>
		<a href="#">Credits</a></p>
	</footer>
</font>
</html>
