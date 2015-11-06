using System;
using System.Collections.Generic;
using static System.Console;
/*
 * Given an array of integers, find two numbers such that they add up to a specific target number.
 * The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
 * You may assume that each input would have exactly one solution.
 * Input: numbers={2, 7, 11, 15}, target=9
 * Output: index1=1, index2=2 
 */

class TwoSum
{

	bool Solve(int[] nums, int target)
	{
		Array.Sort(nums);
		int left = 0;
		int right = nums.Length - 1;
		while (left < right)
		{
			if (nums[left] + nums[right] < target)
				left++;
			else if (nums[left] + nums[right] > target)
				right--;
			else
			{
				WriteLine("num {0}: {1} and num {2}: {3}", left + 1, nums[left], right + 1, nums[right]);
				return true;
			}
		}
		return false;
	}

	static void Main()
	{
		TwoSum ts = new TwoSum();
		List<Tuple<int[], int, bool>> testInputs = new List<Tuple<int[], int, bool>>();
		testInputs.Add(Tuple.Create(new int[] {2, 7, 11, 15}, 9, true));
		foreach (var input in testInputs)
		{
			if (ts.Solve(input.Item1, input.Item2) != input.Item3)
			{
				WriteLine("Tests failed for {0}!", input.Item3);
				return;
			}
		}
		WriteLine("Tests passed!");
	}
}
