input=document.querySelector('#inputarea');
output=document.querySelector('#outputarea');

input.addEventListener('input',()=>{
    let slidervalue=input.value;
    output.innerText=`${slidervalue} sqft.`;
});

calc=document.querySelector('#calc');

