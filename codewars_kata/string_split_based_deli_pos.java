import java.util.ArrayList;

public class string_split_based_deli_pos {

    public static ArrayList<String> string_split(String input, String delimiter){
        ArrayList<String> output = new ArrayList<String>();
        String input_clone = input;

        // Get length of the delimiter as well
        int deli_len = delimiter.length();

        // Seek for the first position of the delimiter
        int deli_pos = input_clone.indexOf(delimiter);

        // Start a loop to be timed out by the deli_pos when it is -1
        do{

            // Cut left from the begining of string to the deli_pos - 1
            String temp = input_clone.substring(0, deli_pos);

            // Add temp to output
            output.add(temp);

            if(deli_len == 1){
                // update input_clone with new value
                input_clone = input_clone.substring(deli_pos + 1, input_clone.length());
            }
            
            else if(deli_len > 1){
                // update input_clone with new value + deli_len
                input_clone = input_clone.substring(deli_pos + deli_len, input_clone.length());
            }
            
            deli_pos = input_clone.indexOf(delimiter);

            // Catch if there are nothing left
            if(deli_pos == -1){
                output.add(input_clone);
            }

        }while(deli_pos != -1);

        return output;
    }

    public static void main(String[] args) {
        String input = "Hello//??/World///woeiwoei?/wewewe", delimiter = "//??/";

        System.out.println(string_split(input, delimiter));
    }
}
