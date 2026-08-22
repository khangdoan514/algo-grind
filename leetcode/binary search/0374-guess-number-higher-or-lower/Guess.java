class Guess {
    int pick;

    int guess(int num) {
        if(num > pick) return -1;
        else if(num < pick) return 1;
        else return 0;
    }
}