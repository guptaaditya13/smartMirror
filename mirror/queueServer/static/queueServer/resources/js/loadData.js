function codeAddress() {
	// while(true){
		setInterval(getData,2000);
		setInterval(getData,500);
	// }
}
function getData(){
	$.ajax({
		type: 'GET',
		url : '/queue/dequeue',
		success: function(data){
			console.log(data);
			document.getElementById(data.key).innerHTML = data.value;
		},
		async: false,
		timeout : 2000,
		dataType: 'json',
	});
}
function updateTime(){
	document.getElementById('time').innerHTML = new Date().toLocaleString();
}
window.onload = codeAddress;