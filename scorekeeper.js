var p1button=document.querySelector("#p1");
var p2button=document.querySelector("#p2");
var reset=document.querySelector("#reset");
var p1=document.querySelector("#p1score");
var p2=document.querySelector("#p2score");
var newinput=document.querySelector("input");
var limit=document.querySelector("p span");

var gameover=false;
var p1score=0;
var p2score=0;
var winningscore=5;

p1button.addEventListener("click",function(){
	if(!gameover)
	{
		p1score++;
		if(p1score === winningscore){
			p1.classList.add("winner");
			gameover=true;
		}
		p1.textContent=p1score;
	}

});

p2button.addEventListener("click",function(){
	if(!gameover)
	{
		p2score++;
		if(p2score === winningscore){
			p2.classList.add("winner"); 
			gameover=true;
		}
		p2.textContent=p2score;
	}
});

reset.addEventListener("click",rest);
	
function rest(){
	p1score=0;
	p2score=0;
	p1.textContent=0;
	p2.textContent=0;
	p1.classList.remove("winner");
	p2.classList.remove("winner");	
	gameover=false;
}

newinput.addEventListener("change",function(){
	limit.textContent=newinput.value;
	winningscore=Number(newinput.value);
	rest();
});