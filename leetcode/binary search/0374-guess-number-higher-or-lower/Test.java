class Test {
    static void check(int n, int pick, int expected) {
        Solution sol = new Solution();
        sol.pick = pick;
        int result = sol.guessNumber(n);
        assert result == expected : result + " != " + expected;
    }

    public static void main(String[] args) {
        check(10, 6, 6);
        check(1, 1, 1);
        check(2, 1, 1);
        check(2, 2, 2);
        check(100, 100, 100);
        System.out.println("all passed");
    }
}