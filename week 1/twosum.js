function twoSum(nums, target) {
    let myMap = new Map();
    let result = [];

    for (let i = 0; i < nums.length; i++) {
        let num = nums[i];
        let diff = target - num;
        if (myMap.has(diff)) {
            result[0] = myMap.get(diff);
            result[1] = i
        } else {
            myMap.set(num, i)
        }
    }
    return result
}

console.log(twoSum([2, 7, 11, 15], 9))