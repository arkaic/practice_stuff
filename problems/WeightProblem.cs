using System;
using System.Collections.Generic;

// 3, 7, 16. They are the only weight drops that our poor man can lose. Can he lose
// just enough to make it to 0 without going negative? 
// Let's find out.

public class WeightProblem
{
    public static void Main()
    {
        WeightProblem w = new WeightProblem();
        int totalWeight = 444;
        w.solve(totalWeight)
    }

    public void solve(int totalWeight)
    {
        List<int> weights = new List<int>();
        recurse(totalWeight, weights);
    }

    public bool recurse(int weight, int weights)
    {
        if (weight == 0)
        {
            return true;
        }
        if (weight < 0)
        {
            return false;
        }
        int[] weightDrops = {16, 7, 3};
        foreach (int drop in weightDrops)
        {
            weights.Add(drop);
            if (recurse(weight - drop, weights))
                return true;
            weights.RemoveAt(weights.Count - 1);
        }
    }
}