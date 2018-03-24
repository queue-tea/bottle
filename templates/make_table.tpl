
<font face="verdana">
		<p style="height:100%; position: fixed; display:block; z-index: 1;
			top: 0; left: 0; background-color: #FFC7C7;
			overflow-x: hidden; padding-top: 20px;">
	  <a href="https://www.w3schools.com/jsref/event_onclick.asp">How to
			use buttons <br> in HTML/Javascript</a><br><br>
		<a href="https://stackoverflow.com/questions/16091823/get-clicked-element-using-jquery-on-event">
		How to use jQuery <br> on events</a><br><br></p>

  <header>
		<style>
		h1 {margin-left: 160px; padding: 0px 10px;
			background-color: #7ECDE0}
		body {height:100%;}
		</style>
	</header>

	<body>
		<h1>CMPS183: Homework 3</h1>
		<p style="margin-left: 160px; padding: 0px 10px;">
				<a href="/index">Home</a>
				<a href="/list">To Do List</a>
				<a href="/new">To Do Form</a><br>
		<p style = "margin-left: 160px; padding: 0px 10px;">
			<button> <a href="/list">Show all</a></button>
			<button> <a href="/showcompleted">Show completed</a></button>
			<button> <a href="/showtodo">Show to do</a></button>
			<button> <a href="/sortposted">Sort by Posted Date</a></button>
			<button> <a href="/sortdue">Sort by Due Date</a></button>
			<button> <a href="/sortupdated">Sort by Updated Date</a></button>
		</p>
		<div style="margin-left: 160px; padding: 0px 10px;">
		<table border="1">
		<tr><td>Task</td><td>Notes</td><td>Date Posted</td><td>Due Date</td><td>Date Updated</td></tr>
		%for row in rows:
		  %id, task, description, posted, due, updated, status = row
		  <tr>
		  <td>{{task}}</td>
			<td>{{description}}</td>
			<td>{{posted}}</td>
			<td>{{due}}</td>
			<td>{{updated}}</td>
			<td><form action="/edit/{{id}}"><input type="submit" value="Edit" /></form></td>
			<td><form action="/delete/{{id}}"><input type="submit" value="Delete" /></form></td>
		  </tr>
		%end
		</table>
	  </div>

	</body>
	<footer>
		<p style="width:100%; margin-left: 160px; position:fixed; bottom: 0; padding: 0px 10px;
			background-color: #7ECDE0">
	  <a href="#">About Us</a>
		<a href="#">Contact</a>
		<a href="#">Privacy</a>
		<a href="#">Credits</a></p>
	</footer>
</font>
