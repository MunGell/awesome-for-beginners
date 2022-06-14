//https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true
package applesoranges;

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
}
