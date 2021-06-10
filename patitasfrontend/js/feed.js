var result = " ";

function calling_posts(){
  var urls    = 'http://localhost:8000/api/posts';
  var headersi = {
    //'Access-Control-Allow-Origin': '*',
    //'Content-type': 'application/json; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
  }
	

	axios.get(urls,headersi)
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



