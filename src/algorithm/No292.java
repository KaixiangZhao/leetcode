package algorithm;

public class No292 {
    public boolean canWinNim(int n) {
        return n%4 != 0;
    }

    public  static void main(String[] args) {
        No292 app = new No292();
        boolean canWin = app.canWinNim(10);
    }
}
