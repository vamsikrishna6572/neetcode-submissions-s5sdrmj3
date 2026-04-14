/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {

        for(int i=0;i<intervals.size();i++){
            int start=intervals.get(i).start;
            int end=intervals.get(i).end;
            for(int j=i+1;j<intervals.size();j++){
                if (intervals.get(j).start < end &&
                    intervals.get(j).end > start) {
                    return false;
                }
            }
        }

        return true;
    }
}
