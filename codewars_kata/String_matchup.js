function solve(arr1,arr2){
    let count_array = [];
    var i, j;

    for(i=0;i<arr2.length;i++){
        let count = 0;
        for(j = 0; j<arr1.length; j++){
            if(arr2[i] == arr1[j]){
                count++;
            }
        }
        count_array.push(count);
    }

    return count_array;
}

console.log(solve(['abc', 'abc','xyz','abcd','cde'], ['abc', 'cde', 'uap']));