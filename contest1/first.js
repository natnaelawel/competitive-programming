function bonAppetit(bill, k, b) {
    let sum = 0
    for(let i= 0; i< bill.length; i++){
        if(i !== k){
            sum += bill[i]
        }
    }
    result = parseInt(sum / 2, 10)
    if(result === b){
        console.log("Bon Apatit")
    }else{
        console.log(b - result)
    }

}