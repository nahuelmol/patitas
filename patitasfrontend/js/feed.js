

function calling_posts(){

	headers = {
		method: 'GET',
  		//mode: 'no-cors',
  		url:'http://localhost:8000/api/posts/',
  		headers: {
    		'Access-Control-Allow-Origin': '*',
    		'Content-Type': 'application/x-www-form-urlencoded',
    		//'Content-Type': null,
    		//'Authorization': null,
    		'X-Requested-With': 'XMLHttpRequest'
  		},

  		//withCredentials: true,
  		//credentials: 'same-origin'
	}

	axios.request(headers,{crossOrigin: null})
  		.then((response) => {
  		var result = response.data;

    	console.log(response.data);
    	console.log(response.status);

    	//document.getElementById("something").innerHTML = result;
	}).catch(e=>console.log(e));

	
}

calling_posts()

