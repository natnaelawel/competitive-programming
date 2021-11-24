function countingSort(arr) {
    let max = arr[0];
    let min = arr[0]
    for (let i = 1; i < arr.length; i++) {
        if(arr[i] > max){
            max = arr[i]
        }
        if(arr[i] < min){
            min = arr[i]
        }
    }

    let numbers = Array.from(new Array(max-min + 1), (_) => 0)
    for(let i = 0; i< arr.length; i++){
        console.log(arr[i])
        numbers[arr[i] - min] += 1;
    }
    let sortedArray = []

    for(let i = 0; i < numbers.length; i++){
        for(let j = 0; j < numbers[i]; j++){
            sortedArray.push(min + i)
        }
    }

    return sortedArray
}




// let unSortedArray = [6, 4, 2, 5, 7, 1, 3]


let unSortedArray = getRandomizedArray(10)
console.log(unSortedArray)

function getRandomizedArray(max) {
    let numbers = Array.from(new Array(max), (_, i) => 0)
    for (let i = numbers.length - 1; i > 0; i--) {
        let rand = Math.floor(((Math.random() < 0.5 ? -1 : 1) * Math.random() * Math.floor(max - 1)));
        numbers[i] = rand
    }
    return numbers
}
// console.log(unSortedArray)
console.log(countingSort(unSortedArray))