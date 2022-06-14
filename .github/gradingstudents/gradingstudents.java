//https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
package gradingstudents;

import java.util.List;

public class gradingstudents {
    
    public static Integer[] gradingStudents(Integer[] grades) {
        for (int i = 0; i < grades.length; i++) {
            if(grades[i] < 38){
                continue;
            }
            if(grades[i] % 5 > 2){
                grades[i] = grades[i] + (5 - (grades[i] % 5));
            }
        }
        return grades;
    }

    public static List<Integer> gradingStudents(List<Integer> grades) {
        for (int i = 0; i < grades.size(); i++) {
            if(grades.get(i) < 38){
                continue;
            }
            if(grades.get(i) % 5 > 2){
                grades.set(i, grades.get(i) + (5 - (grades.get(i) % 5)));
            }
        }
        return grades;
    }
}
