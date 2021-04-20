import java.util.ArrayList;

/**
 * Input: A String with delimiters such as '/'
 * Output: An array of substring seperated by the define delimiter
 * Don't use string to array converter, everything will be processed on string
 * Don't use arraylist parsing to return that specified amount of returned items
 */

public class string_split_delimiter {
    // Standardize string 
    public static ArrayList<String>  string_split(String input, String delimiter){
        ArrayList<String> sub_str = new ArrayList<String>();

        // get original input string length
        int input_len = input.length();

        // loop to get it work!
        while(input_len != 0){
            // get first delimiter position in the string
            int delimiter_pos = input.indexOf(delimiter);

            // error handler when no delimiter is found so exit the program
            if(delimiter_pos == -1){
                break;
            }
            
            // call temp_str to store substr to delimiter_pos 
            String temp_str = input.substring(0, delimiter_pos);

            // append temp_str to sub_str
            sub_str.add(temp_str);

            // define new_input_str to update the input one
            String new_input_str = input.substring(delimiter_pos + 1, input_len);
            
            // update the input_str with new str
            input = new_input_str;

            // update input_len 
            input_len = input.length();
        }

        return sub_str;
    }
    
    public static void main(String[] args) {
        String input_str = "Hello/world/hhehehel/weoiwoeiwoeiowie/wewewewe";
        String delimiter = "/";

        System.out.print(string_split(input_str, delimiter));
    }
}