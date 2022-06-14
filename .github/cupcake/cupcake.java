
//https://www.hackerrank.com/challenges/marcs-cakewalk/problem?isFullScreen=true

package cupcake;

import java.util.List;

public class cupcake {
    public static void calculatecalorie(int[] calories) {
        //calculate minimum calorie consumption.
        //sort calories
        //apply the forumala math.power(x,0)+calories[0] + math.power(x,1)+calories[1],math.power(x,2)+calories[2]... 
        
        //Implementation
        calories = sortarray(calories);
        int minimumcalorie = 0;
        int pow = 0;
        for (int i = 0; i < calories.length; i++) {
            minimumcalorie = (int) (Math.pow(2.0, pow)*calories[i]) + minimumcalorie;
            pow = pow + 1;
        }
        System.out.println("the minimum miles necessary: " + minimumcalorie);
    }

    public static void calculatecalorie(List<Integer> calories)
    {
        calories = sortList(calories);
        int minimumcalorie = 0;
        int pow = 0;
        for (int i = 0; i < calories.size(); i++) {
            minimumcalorie = (int) (Math.pow(2.0, pow)* calories.get(i)) + minimumcalorie;
            pow = pow + 1;
        }
        System.out.println("the minimum miles necessary: " + minimumcalorie);
    }

    private static int[] sortarray(int[] calories){
        for (int i = 0; i < calories.length; i++) {
            for (int j = i + 1; j < calories.length; j++) {
                if (calories[i] < calories[j]) {
                    int temp = calories[i];
                    calories[i] = calories[j];
                    calories[j] = temp;
                }
            }
        }
        return calories;
    }

    private static List<Integer> sortList(List<Integer> calories) {
        for (int i = 0; i < calories.size(); i++) {
            for (int j = i + 1; j < calories.size(); j++) {
                if (calories.get(i) < calories.get(j)) {
                    int temp = calories.get(i);
                    calories.set(i, calories.get(j));
                    calories.set(j, temp);
                }
            }
        }
        return calories;
    }
}
