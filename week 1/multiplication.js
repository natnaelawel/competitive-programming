
const sumPostive = (number1, number2) => {
    let [greater, smaller] =
        number1.length > number2.length ? [number1, number2] : [number2, number1];
    let result = "";
    let carry = 0;
    let digitDif = greater.length - smaller.length;
    for (let k = 0; k < digitDif; k++) {
        smaller = "0" + smaller;
    }
    for (var i = smaller.length - 1; i >= 0; i--) {
        sum = parseInt(greater[i]) + parseInt(smaller[i]) + carry;
        if (sum > 9 && sum % 10) {
            carry = parseInt(sum / 10);
        }
        else {
            carry = 0;
        }
        if (i === 0 && carry) {
            result = `${carry}${sum % 10}` + result;
            console.log(result, " is result");
        } else {
            result = `${sum % 10}` + result;
        }
    }
    return result;
}

function multiply(number1, number2) {
    isNegative = false;
    if (number1[0] === "-" || number2[0] === "-") {
        isNegative = true;
    }
    if (number1[0] === "-" && number2[0] === "-") {
        isNegative = false;
    }
    if (number1[0] === "-") {
        number1 = number1.slice(1);
    }
    if (number2[0] === "-") {
        number2 = number2.slice(1);

    }
    let [upper, lower] =
        number1.length > number2.length ? [number1, number2] : [number2, number1];
    let result = [];
    step = 0
    for (var i = lower.length - 1; i >= 0; i--) {
        let carry = 0;
        rowResult = ""
        for (var j = upper.length - 1; j >= 0; j--) {
            product = lower[i] * upper[j] + carry
            rem = product % 10
            pro = Math.floor(product / 10);
            rowResult = rem + rowResult
            carry = pro;
        }
        for (let k = 0; k < step; k++) {
            rowResult = rowResult + "0";
        }
        result.push(rowResult)
        step++
        console.log(rowResult)
    }
    finalResult = "0"
    for (let m = 0; m < result.length; m++) {
        console.log(result[m])
        finalResult = sumPostive(finalResult, `${result[m]}`)
    }
    if(finalResult[0] === "0")return "0";
    return isNegative ? '-' + finalResult : finalResult;
}

console.log(multiply("-1234", "0"))

