class Test {
    static Solution sol = new Solution();

    static void check(String s, String p, boolean expected) {
        boolean result = sol.isMatch(s, p);
        assert result == expected : s + ", " + p + " -> " + result + " != " + expected;
    }

    public static void main(String[] args) {
        check("aa", "a", false);
        check("aa", "a*", true);
        check("ab", ".*", true);
        check("aab", "c*a*b", true);
        check("mississippi", "mis*is*p*.", false);
        check("abc", "a.c", true);
        System.out.println("all passed");
    }
}
