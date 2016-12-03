function codeAddress() {
	setInterval(getData,2000);
	setInterval(updateTime,500);
}

function getData(){
	$.ajax({
		type: 'GET',
		url : '/queue/dequeue',
		success: function(data){
			console.log(data);
			if(data.key == 'end'){
				document.getElementById('agenda').innerHTML = '';
				document.getElementById('weather').innerHTML = '';
				document.getElementById('news').innerHTML = '';
				document.getElementById('reply').innerHTML = data.value;
				setTimeout(() => {
					console.log('done');
					document.getElementById('reply').innerHTML = '';
				}, 2000);
			} else {
				if (flag){
					document.getElementById('reply').innerHTML = '';
				}
				document.getElementById(data.key).innerHTML = data.value.replace(/(?:\r\n|\n\r|\n|\r)/g, '<br />');
				flag = (data.key = 'reply');
			}
			
		},
		async: false,
		timeout : 2000,
		dataType: 'json',
	});
}

function updateTime(){
	document.getElementById('time').innerHTML = (new Date()).toLocaleString();
}

var flag = false;
window.onload = codeAddress;
