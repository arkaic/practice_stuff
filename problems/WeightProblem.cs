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
            if (w.solve(input.Item1, incrementsChosen) == input.Item2) 
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

    public bool solve(int weight, List<int> incrementsChosen)
    {
        // Base cases
        if (weight == 0)
            return true;
        if (weight < 0)
            return false;

        int[] increments = {16, 7, 3};
        foreach (int inc in increments)
        {
            incrementsChosen.Add(inc);
            if (solve(weight - inc, incrementsChosen))
                return true;
            incrementsChosen.RemoveAt(incrementsChosen.Count - 1);
        }
        return false;
    }
}