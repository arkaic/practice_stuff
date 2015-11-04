using System;
using System.Collections.Generic;
using static System.Console;

// 3, 7, 16. They are the only weight drops that our poor man can lose. Can he lose
// just enough to make it to 0 without going negative? 
// Let's find out.

public class WeightProblem
{
    public static void Main()
    {
        WeightProblem w = new WeightProblem();
        List<Tuple<int, bool>> testInputs = new List<Tuple<int, bool>>();
        testInputs.Add(Tuple.Create(3, true));
        testInputs.Add(Tuple.Create(4, false));
        testInputs.Add(Tuple.Create(8, false));
        testInputs.Add(Tuple.Create(10, true));
        testInputs.Add(Tuple.Create(11, false));
        testInputs.Add(Tuple.Create(321, true));
        testInputs.Add(Tuple.Create(445, true));

        foreach (Tuple<int, bool> input in testInputs)
        {
            List<int> incrementsChosen = new List<int>(); 
            int[] increments = {16, 7, 3};   // choices of what he can drop
            if (w.solve(input.Item1, incrementsChosen, increments) == input.Item2) 
            {
                WriteLine("Test input: [{0} lbs, {1}]", input.Item1, input.Item2);
                if (input.Item2)
                {
                    int c = 0;
                    foreach (var inc in incrementsChosen)
                    {
                        Write("{0} ", inc);
                        c += inc;
                    }
                    WriteLine("");
                    if (c != input.Item1)
                        exitOnTestFail();
                }
                WriteLine("Tests passed\n");
            }
            else
                exitOnTestFail();
        }
    }

    public static void exitOnTestFail()
    {
        WriteLine("Test failed");
        return;
    }

    /*
     * The depth first search ALGORITHM to solve the problem.
     * The ordering of the increments should be nonincreasing so that the dfs
     * prioritizes choosing the largest increments to get the best possible 
     * combination. Returns true if a solution is found, otherwise false, recursively.
    
     * Note: Probably faster if I use a linked list implementation for 
     * incrementschosen. The increase in speed would be from not having to resize
     * the list if it gets too large. It won't be THAT much fast because the adding
     * and removing currently are from the ends of the ArrayList so there isn't a 
     * constant dynamic resizing, at least.
     */
    public bool solve(int weight, List<int> incrementsChosen, int[] increments)
    {
        // Base cases
        if (weight == 0) return true;
        if (weight < 0) return false;

        foreach (int inc in increments)
        {
            incrementsChosen.Add(inc);
            // first solution found also assumed to be the best, so cut off the dfs
            if (solve(weight - inc, incrementsChosen, increments))
                return true;
            incrementsChosen.RemoveAt(incrementsChosen.Count - 1);
        }
        return false;
    }
}