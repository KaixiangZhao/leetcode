package algorithm;

public class No67 {
    public String addBinary(String a, String b) {
        int v1 = 0, v2 = 0;
        char[] char1 = a.toCharArray();
        char[] char2 = b.toCharArray();
        int maxLength = Math.max(char1.length, char2.length);
        int[] newChar1 = new int[maxLength + 1];
        int[] newChar2 = new int[maxLength + 1];
        int[] result = new int[maxLength + 1];
        for (int i = 0; i < maxLength + 1 - char1.length; i++) newChar1[i] = 0;
        for (int i = maxLength + 1 - char1.length; i < maxLength + 1; i++) newChar1[i] = char1[i - (maxLength + 1 - char1.length)] - '0';
        for (int i = 0; i < maxLength + 1 - char2.length; i++) newChar2[i] = 0;
        for (int i = maxLength + 1 - char2.length; i < maxLength + 1; i++) newChar2[i] = char2[i - (maxLength + 1 - char2.length)] - '0';
        int up = 0;
        for (int i = maxLength; i >=0; i--) {
            result[i] = newChar1[i] + newChar2[i] + up;
            up = 0;
            if (result[i] >= 2) {
                result[i] %= 2;
                up = 1;
            }
        }
        int index;
        for (index = 0; index < maxLength + 1; index++) if (result[index] != 0) break;
        String s = "";
        for (int i = index; i < maxLength + 1; i++) s += result[i];
        if (s.equals("")) return "0"; else return s;
    }

    public static void main(String[] args) {
        No67 app = new No67();
        String s = app.addBinary("1", "1");
    }
}
