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
        
        else if (buttonText == "MC"){
            display.value = "0";
            display.value = displayValue;

        }
        else if(buttonText == 'sin'){
            display.value = Math.sin(display.value );
        }
        else if(buttonText == 'cos'){
            display.value  = Math.cos(display.value );
        }
        else if(buttonText == 'tan'){
            display.value = Math.tan(display.value );
        }
        else if(buttonText == 'log'){
            display.value  = Math.log(display.value );
        }
        else if(buttonText == '1/X'){
            display.value  = 1 / eval(display.value );
        }
        else if(buttonText == 'MOD'){
             
            displayValue += '%';
            display.value  = displayValue ;

        }
        
        else if(buttonText =='X²' ){
            display.value = eval(display.value) * eval(display.value);
        }
        else{
            displayValue += buttonText;
            display.value = displayValue;

        }
    })

}