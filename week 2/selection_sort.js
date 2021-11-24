function selectionSort(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        let minIndex = i
        for (let j = i+1; j < arr.length; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j
            }
        }
        swap(arr, minIndex, i)
    }
    return arr
}


function swap(arr, i, j){
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
console.log(selectionSort(unSortedArray))