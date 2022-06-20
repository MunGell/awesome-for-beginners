//https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true

package electronicsshop;

import java.util.List;

public class electronicshop {
    
    public static void electronicsshop(Integer budget, List<Integer> keyboards, List<Integer> drives)
    {
        Integer largest_closetobudget = -1;
        for(Integer i = 0; i < keyboards.size(); i++)
        {
            for(Integer j = 0; j < keyboards.size(); j++)
            {
                if(keyboards.get(i) + drives.get(j) < budget)
                {
                    if(keyboards.get(i) + drives.get(j) > largest_closetobudget)
                    {
                        largest_closetobudget = keyboards.get(i) + drives.get(j);
                    }
                }
            }
        }
        System.out.println("max budget cost" + largest_closetobudget);
        
    }
}
