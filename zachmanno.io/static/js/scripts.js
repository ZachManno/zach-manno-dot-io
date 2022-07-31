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
	callServerTraffic();
});

function callWeather() {
  fetch('https://ml20kezqk5.execute-api.us-east-1.amazonaws.com/weather')
  .then(response => response.json())
  .then(data => {
    console.log(data);
    console.log(data.iconUrl);
    $("#weatherID").text('It is ' + Math.round(parseFloat(data.temp)) + ' degrees in Philadelphia right now!');
    $("#openWeatherIconDiv img").attr("src", data.iconUrl);
  }
  );
}


function callServerTraffic() {
    var serverPutJson = { id: 'mainwebservercount', number: 1 }

    fetch('https://9mzlqvh22e.execute-api.us-east-1.amazonaws.com/increment', {
    method: 'PUT', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    headers: {
      'Content-Type': 'application/json',
      "Accept": "application/json"
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(serverPutJson) // body data type must match "Content-Type" header
  }).then(data => {
    console.log('Page views data: ', data.json().then(r => {
    console.log("r: ", r);
    $("#pageViewsId").text(r.count + ' total views');
    }
    ));
  });

}