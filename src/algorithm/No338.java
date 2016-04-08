package algorithm;

public class No338 {
    public int[] countBits(int num) {
        int[] result = new int[num + 1];
        int j = 0;
        for (int i = 0; i <=num; i++) {
            j = i;
            while (j != 0) {
                if (j%2 != 0) result[i] += 1;
                j /= 2;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        No338 app = new No338();
        int[] result = app.countBits(5);
    }
}
