/*!
* Start Bootstrap - Blog Home v5.0.7 (https://startbootstrap.com/template/blog-home)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-blog-home/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
$(document).ready(function(){

	//=== do some code stuff...

	//===finally, bind my events...
	callWeather();
});

function callWeather() {
  fetch('https://ml20kezqk5.execute-api.us-east-1.amazonaws.com/weather')
  .then(response => response.json())
  .then(data => {
    console.log(data);
    $("#weatherID").text('It is ' + data.temperature + ' degrees in Philadelphia right now!');
  }
  );
}