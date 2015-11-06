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
        Stack<string> exprStack = new Stack<string>(); // builds the string represention
        foreach (string token in tokens)
        {
            int a, b;
            a = b = 0;
            string s, t;
            s = t = null;
            if (token.Equals("+") || token.Equals("*") || token.Equals("/") || token.Equals("-"))
            {
                b = evalStack.Pop();
                a = evalStack.Pop();
                t = exprStack.Pop();
                s = exprStack.Pop();
            }
            switch (token)
            {
                case "+":
                    evalStack.Push(a + b);
                    exprStack.Push("(" + s + " + " + t + ")");
                    break;
                case "*":
                    evalStack.Push(a * b);
                    exprStack.Push("(" + s + " * " + t + ")");
                    break;
                case "/":
                    evalStack.Push(a / b);
                    exprStack.Push("(" + s + " / " + t + ")");
                    break;
                case "-":
                    evalStack.Push(a - b);
                    exprStack.Push("(" + s + " - " + t + ")");
                    break;
                default:
                    evalStack.Push(Int32.Parse(token));
                    exprStack.Push(token);
                    break;
            }
        }
        WriteLine("{0} = {1}", exprStack.Peek(), evalStack.Peek());
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