public class MovingAverage {
    /*
    * @param size: An integer
    
    */
    private Queue<Integer> queue ;
    private int size;
    private double sum = 0;
    public MovingAverage(int size) {
        // do intialization if necessary
        this.size = size;
        queue = new LinkedList<>();
    }

    /*
     * @param val: An integer
     * @return:  
     */
    public double next(int val) {
        // write your code here
        sum = sum + val;
        if(queue.size() == size){
            sum = sum - queue.poll();
        }
        queue.offer(val);
        return (double) sum / queue.size();
    }
}
