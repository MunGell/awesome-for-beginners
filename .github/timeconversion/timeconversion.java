
//https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

package timeconversion;

public class timeconversion {

    public static String timeConversion(String s) {
        if(s.length() == 10){
            String[] time = s.split(":");
            String seconds = time[2].substring( 0,  2);
            String ampm = time[2].substring( 2,  4);
            String[] time2 = new String[2]; //07:01:00PM
            time2[0] = seconds;
            time2[1] = ampm;

            if(time2[1].equals("AM")){
                if(time[0].equals("12")){
                    return "00"+":"+time[1]+":"+time2[0];
                }
                return time[0]+":"+time[1]+":"+time2[0];
            }
            if(time2[1].equals("PM")){   //07:01:00PM
                if(time[0].equals("12")){
                    return "12"+":"+time[1]+":"+time2[0];
                }
                return String.valueOf((Integer.parseInt(time[0])  + 12))  +":" + time[1]+":"+time2[0];
            }
        }
        return null;
    }
    
}
