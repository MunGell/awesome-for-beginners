console.log(" nazmus sakib");
var count =0;
function setapplicationtitle()
{
 const titleElement =document.getElementById('title');
console.log(titleElement);
titleElement.innerText="Counter App"; 
}
setapplicationtitle();
const incrementButton = document.getElementById('increment');
// --- this part of code is for showing alert when + Button is clicked !!!
// function increaseCount()
// {
//      alert(' Increase Button Clicked!!!');
// }
//  incrementButton.addEventListener('click',increaseCount);

const countshow= document.getElementById('counter');
function increaseCount()
{
   if(count>=10)
   {
    alert('OverFlow !!!!');
   }
   else
   {
    count=count+1;
    countshow.innerText=count;
   }
    
}
incrementButton.addEventListener('click',increaseCount)

const decrementButton =document.getElementById('decrement');


// --- this part of code is for showing alert when - Button is clicked !!!
// function decreseCount()
// {
//      alert('Decrese Button Clicked !!!');
// }
// decrementButton.addEventListener('click',decreseCount);

const showdecrement=document.getElementById('counter');
function decrementCount()
{
    if(count===0)
    {
        alert("Negative Value is not acceptable !!!!");
    }
    else
    {
        count=count-1;
    showdecrement.innerText=count;
    }
    
}

decrementButton.addEventListener('click',decrementCount);



//  const counterElement=document.getElementById('counter');
//  counterElement.innerText=3;