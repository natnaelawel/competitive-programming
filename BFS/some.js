const calPoints = (ops)=>{
    let result = []
    for(let i = 0; i < ops.length; i++){
        switch(ops[i]){
            case "D": {
                result.push((result[result.length - 1]) * 2)
                console.log("after doubling", result)
                break;
            }
            case "C": {
                result.pop()
                console.log("after invalidating", result);

                break
            }
            case "+":{
                const sm = result[result.length - 1] + result[result.length - 2];
                result.push(sm)
                console.log("after adding lat two", result, sm);

                break
            }
            default: {
                console.log(ops[i])
                result.push(parseInt(ops[i]))
            }
        }
    }
    console.log(result)
    let ans = 0
    for(let i = 0; i < result.length; i++){
        ans += result[i]
    }
    return ans 

}

const ops = ["5", "2", "C", "D", "+"]

console.log(calPoints(ops))