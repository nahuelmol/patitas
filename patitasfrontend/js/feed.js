var result = " ";

function calling_posts(){
  var urls    = 'http://localhost:8000/api/posts';
  var headersi = {
    	'Origin': 'http://localhost:8080',
	'Allow-Control-Request-Method':'*',
    	'Access-Control-Request-Method': 'GET',
    	'Access-Control-Request-Headers': 'NCZ'
  }
var config = {
	url:urls,
	headers:headersi
}

axios.request(config)
  		.then((response) => {
      console.log(response.data[0])

  		result    = response.data[0].content;
      likes     = response.data[0].likes;
      share     = response.data[0].shared;
      responses = response.data[0].responses;
      user      = response.data[0].username;

      document.getElementById("lastuser").innerHTML     = user + " posted..";
      document.getElementById("lastcontent").innerHTML  = result;
      document.getElementById("lastlikes").innerHTML    = likes;
      document.getElementById("lastshare").innerHTML    = share;
      document.getElementById("lastresps").innerHTML    = responses;

      var prelast     = document.getElementById("prelast");
      var preprelast  = document.getElementById("preprelast");


	}).catch(e=>console.log(e));

	
}

calling_posts()



