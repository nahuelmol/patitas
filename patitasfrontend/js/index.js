
function getCookie(name) {  
        var dc = document.cookie;  
        var prefix = name +"=";  
        var begin = dc.indexOf("; " + prefix);  
        if (begin == -1) {  
            begin = dc.indexOf(prefix);  
            if (begin != 0)return null;  
        } else {  
            begin += 2;  
        }  
        var end = document.cookie.indexOf(";", begin);  
        if (end == -1) {  
            end = dc.length;  
        }  
        return unescape(dc.substring(begin + prefix.length, end));  
} 

var result = getCookie('message');
document.getElementById('msg_receptor').innerHTML = result;
console.log(result);

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
