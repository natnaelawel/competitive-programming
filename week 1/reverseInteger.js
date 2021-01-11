const { reverse } = require("dns");

function reverseInteger(number){
    let reversed = 0;
    while(number !== 0){
        let rem = number % 10
        number = parseInt(number / 10) 
        
        reversed = (reversed * 10) + rem
    }
    if(reversed > (2 ** 31 -1))return 0
     
    return reversed
}

console.log(reverseInteger(-12030))