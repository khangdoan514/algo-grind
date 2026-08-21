import java.util.Arrays;

class Test {
    static Solution sol = new Solution();

    static void check(int[] nums, int[] expected) {
        sol.moveZeroes(nums);
        assert Arrays.equals(nums, expected) : Arrays.toString(nums) + " != " + Arrays.toString(expected);
    }

    public static void main(String[] args) {
        check(new int[]{0, 1, 0, 3, 12}, new int[]{1, 3, 12, 0, 0});
        check(new int[]{0}, new int[]{0});
        check(new int[]{1, 2, 3}, new int[]{1, 2, 3});
        check(new int[]{0, 0, 0}, new int[]{0, 0, 0});
        check(new int[]{1, 2, 0, 0}, new int[]{1, 2, 0, 0});
        System.out.println("all passed");
    }
}