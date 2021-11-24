function bubbleSort(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        for (let j = 0; j < arr.length - i; j++) {
            console.log(arr[i], arr[j])
            if (arr[j] > arr[j+1]) {
                let temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    return arr
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
console.log(bubbleSort(unSortedArray))