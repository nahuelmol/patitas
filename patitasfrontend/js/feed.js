var result = " ";

function calling_posts(){
  var urls    = 'http://localhost:8000/api/posts';
  var headersi = {
    	 'Origin': 'http://localhost:8080',
	     //'Allow-Control-Request-Method':'*',
    	 'Access-Control-Request-Method': 'GET',
    	 'Access-Control-Request-Headers': 'NCZ'
  }
var config = {
	url:urls,
	headers:headersi
}

axios.request(config)
  		.then((response) => {
      console.log(response.data[0].id)
      console.log(response.data[1].id)

  		result    = response.data[0].content;
      likes     = response.data[0].likes;
      share     = response.data[0].shared;
      responses = response.data[0].responses;
      user      = response.data[0].username;

      result1   = response.data[1].content;
      likes1    = response.data[1].likes;
      share1    = response.data[1].shared;
      responses1= response.data[1].responses;
      user1     = response.data[1].username;

      document.getElementById("lastuser").innerHTML     = user + " posted..";
      document.getElementById("lastcontent").innerHTML  = result;
      document.getElementById("lastlikes").innerHTML    = likes;
      document.getElementById("lastshare").innerHTML    = share;
      document.getElementById("lastresps").innerHTML    = responses;

      document.getElementById("prelastuser").innerHTML     = user1 + " posted..";
      document.getElementById("prelastcontent").innerHTML  = result1;
      document.getElementById("prelastlikes").innerHTML    = likes1;
      document.getElementById("prelastshare").innerHTML    = share1;
      document.getElementById("prelastresps").innerHTML    = responses1;

      var prelast     = document.getElementById("prelast");
      var preprelast  = document.getElementById("preprelast");


	}).catch(e=>console.log(e));

	
}

function calling_shares(name){
  //var urls    = 'http://localhost:8000/api/posts';
  //var headersi = {
  //     'Origin': 'http://localhost:8080',
  //     'Allow-Control-Request-Method':'*',
  //     'Access-Control-Request-Method': 'GET',
  //     'Access-Control-Request-Headers': 'NCZ'
  //}
  //var config = {
  //  url:urls,
  //  headers:headersi
  //}
  var template = Handlebars.compile("Handlebars <b>{{doesWhat}}</b>");
  // execute the compiled template and print the output to the console

  console.log(template({ doesWhat: "rocks!" }));
  document.getElementById("cosa").innerHTML = template({ doesWhat: "rocks!" });

  console.log(name);

}

function calling_likes(){
  //var urls    = 'http://localhost:8000/api/posts';
  //var headersi = {
  //     'Origin': 'http://localhost:8080',
  //     'Allow-Control-Request-Method':'*',
  //     'Access-Control-Request-Method': 'GET',
  //     'Access-Control-Request-Headers': 'NCZ'
  //}
  //var config = {
  //  url:urls,
  //  headers:headersi
  //}

  console.log(data);

}



calling_posts()



