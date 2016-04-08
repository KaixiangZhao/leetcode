package algorithm;

public class No171 {
    public int titleToNumber(String s) {
        char[] chars = s.toCharArray();
        int number = 0;
        for (int i = 0; i < chars.length; i++)
            number += (chars[chars.length - i - 1] - 'A' + 1) * Math.pow(26, i);
        return number;
    }

    public static void main(String[] args) {
        No171 app = new No171();
        int number = app.titleToNumber("AA");
    }
}
