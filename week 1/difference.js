function getUpperAndLower(number1, number2) {
  return number1.length > number2.length || parseInt(number1[0]) > parseInt(number2[0]) ? [number1, number2] : [number2, number1];
}

function sumNegative(number1, number2) {
  let isNegative = false;
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
  let [upper, lower] = getUpperAndLower(number1, number2)
  let result = "";
  let carry = 0;
  let digitDif = upper.length - lower.length;
  for (let k = 0; k < digitDif; k++) {
    lower = "0" + lower;
  }
  for (var i = lower.length - 1; i >= 0; i--) {
    isNegative = carry === 0 ? true : false
    // console.log(carry)

    let upperValue = parseInt(upper[i]) - carry;
    let lowerValue = parseInt(lower[i]);
    console.log('upper value is ', upperValue, ' lower value is ', lowerValue)
    if (upperValue >= lowerValue) {
      sum = upperValue - lowerValue;
      carry = 0;
    } else {
      sum = 10 + upperValue - lowerValue;
      carry = 1;
    }
    console.log('sum is ', sum)
    result = `${sum % 10}` + result;
  }

  resultLength = result.length;
  updatedResult = result
  for (let j = 0; j <= resultLength; j++) {
    if (result[j] === "0") {
      updatedResult = result.slice(1);
    } else {
      break;
    }
  }
  result = result.replace(/^0+/, '');
  console.log(isNegative)
  return isNegative ? '-' + result : result;
}
1
console.log(sumNegative("1030", "-999"));
console.log(sumNegative("2", "4"));
