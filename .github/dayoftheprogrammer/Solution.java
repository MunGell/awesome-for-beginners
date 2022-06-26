//https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true
package dayoftheprogrammer;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'dayOfProgrammer' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts INTEGER year as parameter.
     */

    public static String dayOfProgrammer(int year) {
    // Write your code here
    if (year >= 1700 && year <= 1917) //Julian calendar
    {
        if(year % 4 == 0)
        {
            return "12.09"+"."+ year;
        }
        else
        {
            return "13.09"+"."+year;
        }
    }else if (year == 1918)
    {
        return "26.09.1918";
    }
    else
        if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)) // Gregorian
        
        {
            return "12.09"+"."+ year;
        } 
        else
            return "13.09"+"."+year;
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int year = Integer.parseInt(bufferedReader.readLine().trim());

        String result = Result.dayOfProgrammer(year);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

