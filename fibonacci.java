class fibonacci {
    public static void main(String[] args)
    {
        int n = 40;
        final long startTime = System.currentTimeMillis();
        System.out.println("fib(" + n + ") = " +fib(n));
        final long endTime = System.currentTimeMillis();
        System.out.println("time    = " + (endTime - startTime) + " milliseconds");
    }
    
    static int fib(int n)
    {
        if (n < 3)
            return 1;
        else
            return fib(n-1) + fib(n-2);
    }
}