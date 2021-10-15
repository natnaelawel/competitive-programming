function countingSort(arr) {
    let max = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if(arr[i] > max){
            max = arr[i]
        }
    }
    let numbers = Array.from(new Array(max + 1), (_, i) => 0)

    for(let i = 0; i< arr.length; i++){
        numbers[arr[i]] += 1;
    }
    let sortedArray = []

    for(let i = 0; i < numbers.length; i++){
        for(let j = 0; j < numbers[i]; j++){
            sortedArray.push(i)
        }
    }

    return sortedArray
}




// let unSortedArray = [6, 4, 2, 5, 7, 1, 3]


let unSortedArray = getRandomizedArray(10)

function getRandomizedArray(max) {
    let numbers = Array.from(new Array(max), (_, i) => i + 1)
    for (let i = numbers.length - 1; i > 0; i--) {
        let rand = Math.floor(Math.random() * Math.floor(max - 1));
        let temp = numbers[i]
        numbers[i] = rand
        numbers[rand] = temp
    }
    return numbers
}
console.log(unSortedArray)
console.log(countingSort(unSortedArray))