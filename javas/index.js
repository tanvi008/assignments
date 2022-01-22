let display = document.getElementById('display');
buttons = document.querySelectorAll('button');
let displayValue= '';
for (x of buttons){
    x.addEventListener('click', (i) =>{
        buttonText = i.target.innerText;
        console.log('button text is '. buttontext);

        if (buttonText =='X'){
            buttontext ="*";
            displayValue += buttonText;
            display.value = displayValue;
        }
        else if (buttonText == "AC"){
            displayValue = "";
            display.value = displayValue;
        }
        else if (buttonText == "="){
            display.value = eval(displayValue);
        }
        else{
            displayValue += buttonText;
            display.value = displayValue;
        }
    })

}