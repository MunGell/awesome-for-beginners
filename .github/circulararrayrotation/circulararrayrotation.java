//https://www.hackerrank.com/challenges/circular-array-rotation/problem?isFullScreen=true 
package circulararrayrotation;

import java.util.ArrayList;
import java.util.List;

public class circulararrayrotation {
    
    public static List<Integer> circulararrayrotationnumbers(List<Integer> a, int k, List<Integer> queries)
    {   
        List<Integer> shiftedarray = new ArrayList();
        List<Integer> return_indicedarray = new ArrayList();
        for(int i = a.size() - k; i < a.size(); i++ )
        {
            shiftedarray.add(a.get(i));
        }
        for (int j = 0; j < k - 1 ; j++)
        {
            shiftedarray.add(a.get(j));
        }

        for (int l = 0; l < queries.size(); l++)
        {
            return_indicedarray.add(shiftedarray.get(queries.get(l)));
        }
        return return_indicedarray;

    }
}
