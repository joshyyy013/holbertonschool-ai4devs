public class bug5_fixed {
    public static double calculateCompletion(int completed, int total) {
        double percentage = ((double) completed / total) * 100;
        return percentage;
    }

    public static void main(String[] args) {
        int completedTasks = 3;
        int totalTasks = 8;
        double percentage = calculateCompletion(completedTasks, totalTasks);
        System.out.println("Completed tasks: " + completedTasks);
        System.out.println("Total tasks: " + totalTasks);
        System.out.println("Completion: " + percentage + "%");
    }
}