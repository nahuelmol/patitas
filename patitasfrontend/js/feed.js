

function calling_posts(){
  var urls    = 'http://localhost:8000/api/posts';
  var headersi = {
    //'Access-Control-Allow-Origin': '*',
    //'Content-type': 'application/json; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
  }
	var config = {
    method:'get',
    url:'posts',
    baseURL: 'http://localhost:8080/api/',
    headers:headersi
	}

	axios.get(urls,headersi)
  		.then((response) => {
  		var result = response.data;

    	console.log(response.data[0].content);
    	console.log(response.status);

	}).catch(e=>console.log(e));

	
}

calling_posts()

