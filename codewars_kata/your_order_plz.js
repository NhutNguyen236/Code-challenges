function order(words){
    let order_string = [];
    let words_list = [];

    // split string into a list
    words_list = words.split(" ");
    
    // catch situation of an empty list
    if(words.length != 0){
        // access to each one in list to find number
        /**
         * Algorithm 
         * Access to each element first
         * extract number from the element
         * push the element to the order_string with position of the extracted number and minus with 1
         */
        var i;
        for(i=0; i<words_list.length; i++){
            var pos_number = words_list[i].match(/(\d+)/);
            order_string[parseInt(pos_number[0]-1)] = words_list[i];
        }
    }
    else{
        return order_string = "";
    }
    
    return order_string.join(" ");
}

console.log(order(""));

