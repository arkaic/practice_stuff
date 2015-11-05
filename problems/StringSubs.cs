using static System.Console;
using System.Collections;
using System.Collections.Generic;

// Replace all vowels with the next Nth vowel
// Replace all consonants with the next (N*N)th consonant
// eg  if N=3, a is replaced with o, i is replaced with a
// j is replaced with t

public class StringSubs
{

    public string Solve(string word, int n)
    {
        HashSet<char> vowelSet = new HashSet<char>() {'a', 'e', 'i', 'o', 'u'};
        List<char> vowels = new List<char>() {'a', 'e', 'i', 'o', 'u'};
        HashSet<char> consonantSet = new HashSet<char>() {
            'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
            'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
        };
        List<char> consonants = new List<char>() {
            'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
            'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
        };

        char[] wordChars = word.ToCharArray();
        for (int i = 0; i < wordChars.Length; i++)
        {
            char ch = wordChars[i];
            if (vowelSet.Contains(ch))
                wordChars[i] = vowels[(vowels.IndexOf(ch) + n) % vowels.Count];
            else if (consonantSet.Contains(ch))
                wordChars[i] = consonants[(consonants.IndexOf(ch) + n * n) % consonants.Count];
        }
        return new string(wordChars);
    }

    public static void Main()
    {
        StringSubs ss = new StringSubs();
        WriteLine("henry lin ==> {0}", ss.Solve("henry lin", 3));
        string s = "we've woken up alone/no song to sing us off the edge";
        WriteLine("{0} ==> {1}", s, ss.Solve(s, 3));
    }
}