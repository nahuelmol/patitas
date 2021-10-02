var result = " ";

function calling_posts(){
  var urls    = 'http://localhost:8000/db/posts/';

  axios.get(urls,{withCredentials: true})
  		.then((response) => {
      var posts = response.data.posts;
      var each;
      var each_cnt;

      for(var i=0; i < posts.length; i++){
         
         var newDiv = document.createElement('div');
         newDiv.id = 'r'+i;
         newDiv.className = 'each_block';


         var target = document.createElement('BUTTON');
         target.id = 'btn'+i;
         target.className = 'btns';
         var cnt = document.createElement('div');
         cnt.className = 'content';

         var text = document.createElement('p');
         text.className = 'txt';


         toAdd.appendChild(newDiv);
         newDiv.appendChild(target);
         newDiv.appendChild(cnt);
         cnt.appendChild(text);
      }
      document.getElementById('sel').appendChild(toAdd);

      each = document.getElementsByClassName('btns');
      each_cnt = document.getElementsByClassName('content');
      each_text = document.getElementsByClassName('txt');

      for(var j = 0; j<posts.length;j++){
          //console.log(posts[j]);
          each[j].innerHTML = 'Like';
          each_text[j].innerHTML = posts[j].content;
          //each_cnt[j].innerHTML = 1;
          console.log(each[j]);
      }


  }).catch(e=>console.log(e));


  var toAdd = document.createDocumentFragment();
}

calling_posts()

