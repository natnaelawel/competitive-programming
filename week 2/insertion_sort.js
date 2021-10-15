function insertionSort(arr) {
    for (let i = 1; i < arr.length; i++) {
        let current = arr[i]
        let j = i - 1
        while (j >= 0 && arr[j] > current) {
            arr[j + 1] = arr[j]
            j--
        }
        
        arr[j + 1] = current;
        console.log(arr)
    }
    return arr
}


function swap(arr, i, j) {
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
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
console.log(insertionSort(unSortedArray))