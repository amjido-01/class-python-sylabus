// const arr = [1,2,3,4,3,5,3,3, 0];
// function getVal(arr, val) {
//     let res = 0;
//     for(let i = 0; i < arr.length; i++) {
//         if (arr[i] === val) {
//             res ++;
//         }
//     }
//     return res;
// }

// let result = getVal(arr, 0)
// console.log(result)


// const arr = [1,2,3,4,3,5,3,3, 0];
// const arr = [1,2,3,1]
// function containsDup(arr) {
//     let k = 1
//     for (let i = 0; i < arr.length -1; i++) {
//         if (arr[i] !== arr[i + 1]) {
//             arr[k] === arr[i + 1]
//             k++
//             return false
//         } else {
//             break
//         }
//     }
//     return true
// }

// let res = containsDup(arr)
// console.log(res);

// const arr = [1,2,3,4,3,5,3,3, 0];
// function containsDup(arr) {
//     let hashMap = {};
//     for (let i = 0; i < arr.length; i++) {
//         if (hashMap[arr[i]] === undefined) {
//             return true
//         }
//         hashMap[arr[i]] = true;
//     }
//    return false;
// }
// let res = containsDup(arr)
// console.log(res);
const arr = [1,3,5,7,9]
for (let i = 0; i < arr.length; i++) {
    if (i <= 2) {
        console.log(arr[i]);
    }
}