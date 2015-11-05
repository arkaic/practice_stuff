using System;
using static System.Console;
using System.Collections.Generic;

 /* Given an array of integers where each element added to its index points 
  * to the index of the next element how would you detect if there is a single 
  * full cycle in this array (meaning it starts at an index, visits all other 
  * indices before returning back to it)
  * Assume the starting point is the first index.
  * Elements may be negative or positive.
  */

class SingleCycleRelativeArrays
{
    // C# doesn't have a proper modulo operation for negative numbers
    delegate int lambda(int x, int y);
    lambda mod = (x, y) => (x % y + y) % y;

    bool Solve(int[] relArray)
    {
        return recurse(relArray, 0, 0);
    }   

    /**
     * The Algorithm: We know that any 0's encountered will lead to an infinite
     * loop with itself. So if we replace all elements with 0's when we visit them, 
     * then for every element encountered, if it is a zero, then we check if we have visited
     * array.Length elements. If so, we have reached a single, full cycle. 
     * Else, the array is not a single complete cycle; we've hit a loop and there 
     * are still unvisited elements outstanding.
     */
    bool recurse(int[] relArray, int index, int count)
    {
        if (relArray[index] == 0) 
        {
            if (count == relArray.Length && index == 0)
                return true;
            else
                return false;
        }

        int next = mod(index + relArray[index], relArray.Length);
        relArray[index] = 0;
        return recurse(relArray, next, ++count);
    }

    static void Main()
    {
        SingleCycleRelativeArrays scra = new SingleCycleRelativeArrays();
        List<Tuple<int[], bool>> testInputs = new List<Tuple<int[], bool>>();
        testInputs.Add(Tuple.Create(new int[] {0, 0, 0}, false));
        testInputs.Add(Tuple.Create(new int[] {-1, 7, 1, 3, -3, 5}, true));
        testInputs.Add(Tuple.Create(new int[] {-1, 7, 1, 0, -3, 5}, false));
        testInputs.Add(Tuple.Create(new int[] {-1, -1, -1, -1, -1, -1}, true));
        testInputs.Add(Tuple.Create(new int[] {1, 1, 1, 1, 1, 0}, false));
        foreach (var input in testInputs)
        {
            if (scra.Solve(input.Item1) != input.Item2)
            {
                WriteLine("Test failed");
                return;
            }
        }
        WriteLine("All tests passed");
    }
}