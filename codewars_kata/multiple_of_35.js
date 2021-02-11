function solution(number){
    let sum = 0;

    var i, j;

    for(i=3;i<number;i++){
        if(i%3==0 || i%5==0){
            sum = sum + i;
        }
    }

    return sum;
}

console.log(solution(10));