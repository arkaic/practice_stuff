using System.Collections.Generic;
using static System.Console;


class FindPrimes
{
    const int N = 88;
    /*
     * Find all primes up to and including n. Builds up a list of primes.
     * For each successive number < n, mod them with all current primes 
     * found. 
     */
    LinkedList<int> solve(int n)
    {
        LinkedList<int> primes = new LinkedList<int>();
        if (n < 2) return primes;
        
        for (int i = 2; i <= n; i++)
        {
            bool isPrime = true;
            foreach (int prime in primes)
            {
                if (i % prime == 0)
                {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime)
                primes.AddLast(i);
        }
        return primes;
    }

    static void printCollection<T>(ICollection<T> collection)
    {
        if (collection.Count == 0)
        {
            WriteLine("[Empty]");
            return;
        }
        foreach (T item in collection)
            Write("{0}, ", item);
        WriteLine("");
    }

    static void Main()
    {
        FindPrimes fp = new FindPrimes();
        WriteLine("All primes up to and including {0}", N);
        printCollection(fp.solve(N));
    }
}