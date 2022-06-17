//https://www.hackerrank.com/challenges/beautiful-triplets/problem?isFullScreen=true
package beautifultriplets;

import java.util.List;

public class beautifultriplets {
    
    public static void beautifultriplet(int d, int[] arr) {
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                for (int k = 0; k < arr.length; k++) {
                    if (arr[i] + d == arr[j] && arr[j] + d == arr[k]) {
                        count++;
                    }
                }
            }
        }
        System.out.println(count);
    }

    public static void beautifultriplet(int d, List<Integer> arr) {
        int count = 0;
        for (int i = 0; i < arr.size(); i++) {
            for (int j = 0; j < arr.size(); j++) {
                if (arr.get(i) + d == arr.get(j)) {
                    for (int k = 0; k < arr.size(); k++) {
                        if (arr.get(j) + d == arr.get(k)) {
                            count++;
                        }
                    }
                }
            }
        }
        System.out.println(count);
    }
}
