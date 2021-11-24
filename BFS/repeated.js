const findErrorNums = (nums)=>{
    let dups = null
    let sum = 0 
    for(let i = 0; i< nums.length; i++){
        let prevArray = nums.slice(0, i)
        if(prevArray.includes(nums[i])){
            dups = nums[i]
        }else{
            sum += nums[i]
        }
    }
    let allSum = nums.length * (nums.length + 1)/ 2
    return [dups, allSum - sum]
}

const makeMap = (nums) => {
    let map = {}
    for(let i = 0; i< nums.length; i++){
        map[i] = map[i] ? map[i] + 1 : 0
    }
}

const nums = [1, 2, 3, 4, 3]

console.log(findErrorNums(nums))