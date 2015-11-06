using System;
using static System.Console;
using System.Collections.Generic;

/*
 * Evaluate an arithmetic expression in Reverse Polish Notation
 * ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
 * ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
 */

class ReversePolishNotation
{

    int Solve(string[] tokens)
    {
        Stack<int> evalStack = new Stack<int>();
        foreach (string token in tokens)
        {
            int a, b;
            switch (token)
            {
                case "+":
                    evalStack.Push(evalStack.Pop() + evalStack.Pop());
                    break;
                case "*":
                    evalStack.Push(evalStack.Pop() * evalStack.Pop());
                    break;
                case "/":
                    b = evalStack.Pop();
                    a = evalStack.Pop();
                    evalStack.Push(a / b);
                    break;
                case "-":
                    b = evalStack.Pop();
                    a = evalStack.Pop();
                    evalStack.Push(a - b);
                    break;
                default:
                    evalStack.Push(Int32.Parse(token));
                    break;
            }
        }
        WriteLine(evalStack.Peek());
        return evalStack.Pop();
    }

    static void Main()
    {
        ReversePolishNotation rpn = new ReversePolishNotation();
        List<Tuple<string[], int>> testInputs = new List<Tuple<string[], int>>();
        testInputs.Add(Tuple.Create(new string[] {"2", "1", "+", "3", "*"}, 9));
        testInputs.Add(Tuple.Create(new string[] {"4", "13", "5", "/", "+"}, 6));
        foreach (var input in testInputs)
        {
            if (rpn.Solve(input.Item1) != input.Item2)
            {
                WriteLine("Tests failed for {0}!", input.Item2);
                return;
            }
        }
        WriteLine("Tests passed!");
    }   
}