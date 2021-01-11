
function sockMerchant(n, ar) {
    let pairs = new Map()
    let count = 0;
    for(let i = 0; i< ar.length; i++){
        if(pairs.has(ar[i])){
            let value = pairs.get(ar[i]) + 1
            pairs = pairs.set(ar[i], value)
        }
        else{
            pairs.set(ar[i], 1)
        }

        if(pairs.get(ar[i]) % 2 === 0){
            count++
        }
    }
    return count

    
}

let socks = [10 ,20 ,20 ,10 ,10 ,30, 50 ,10 ,20]
console.log(sockMerchant(socks.length, socks))