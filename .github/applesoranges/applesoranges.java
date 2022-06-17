//https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true
package applesoranges;

import java.util.List;

public class applesoranges {
    
    public static void countapplesoranges(int s, int t, int a, int b, int[] apples, int[] oranges) {
        int applecount = 0;
        int orangecount = 0;
        for (int i = 0; i < apples.length; i++) {
            apples[i] = apples[i] + a;
        }
        for (int i = 0; i < oranges.length; i++) {
            oranges[i] = oranges[i] + b;
        }

        for (int i = 0; i < apples.length; i++) {
            if (apples[i] >= s && apples[i] <= t) {
                applecount++;
            }
        }
        for (int i = 0; i < oranges.length; i++) {
            if (oranges[i] >= s && oranges[i] <= t) {
                orangecount++;
            }
        }
        System.out.println(applecount);
        System.out.println(orangecount);
    }

    public static void countApplesAndOranges(int s, int t, int a, int b, List<Integer> apples, List<Integer> oranges) {
        int applecount = 0;
        int orangecount = 0;
        for (int i = 0; i < apples.size(); i++) {
            apples.set(i, apples.get(i) + a);
        }
        for (int i = 0; i < oranges.size(); i++) {
            oranges.set(i, oranges.get(i) + b);
        }

        for (int i = 0; i < apples.size(); i++) {
            if (apples.get(i) >= s && apples.get(i) <= t) {
                applecount++;
            }
        }
        for (int i = 0; i < oranges.size(); i++) {
            if (oranges.get(i) >= s && oranges.get(i) <= t) {
                orangecount++;
            }
        }
        System.out.println(applecount);
        System.out.println(orangecount);
    }
}
