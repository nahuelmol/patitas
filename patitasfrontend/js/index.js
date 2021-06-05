

function normal_response() {
	console.log("HOLA");
	axios.get('https://api.github.com/users/mapbox')
  		.then((response) => {
    	console.log(response.data.login);
    	console.log(response.status);
	});

  	fetch('https://jsonplaceholder.typicode.com/todos/1')
  		.then(response => response.json())
  		.then(json => console.log(json.title))
}
