
#:package TUnit@*

using System.Diagnostics;
using TUnit.Assertions;
using TUnit.Assertions.Extensions;
using TUnit.Core;

public class Solution {
    public int Search(int[] nums, int target) {
        var lowerBound = 0;
        var upperBound = nums.Length - 1;

        while (lowerBound <= upperBound)
        {
            var midpoint = (upperBound + lowerBound) / 2;

            var value = nums[midpoint];
            if (target == value)
                return midpoint;
            else if (target < value)
                upperBound = midpoint - 1;
            else if (target > value)
                lowerBound = midpoint + 1;
        }

        return -1;
    }
}

public class Tests
{    
    [Test]
    public async Task SingleItemArray()
    {
        var soln = new Solution();
        var index = soln.Search( [1], 1);
        await Assert.That(index).IsEqualTo(0);
    }

    [Test]
    public async Task TwoItemArray_FirstItem()
    {
        var soln = new Solution();
        var index = soln.Search( [1,2], 1);
        await Assert.That(index).IsEqualTo(0);
    }

    [Test]
    public async Task TwoItemArray_SecondItem()
    {
        var soln = new Solution();
        var index = soln.Search( [1,2], 2);
        await Assert.That(index).IsEqualTo(1);
    }

    [Test]
    public async Task ForOddN_ReturnsLastItem()
    {
        var soln = new Solution();
        var result = soln.Search( [-1,0,3,5,9], 9);
        await Assert.That(result).IsEqualTo(4);
    }
    
    [Test]
    public async Task ForEvenN_ReturnsLastItem()
    {
        var soln = new Solution();
        var result = soln.Search( [-1,0,3,5,9,12], 12);
        await Assert.That(result).IsEqualTo(5);
    }
}

/*
#####################
# Leetcode 704 Binary Search
# July 29, 2026
# Start: 08:58 PM
# End: 11:02 PM
# Submission Link: https://leetcode.com/problems/binary-search/submissions/2086285783/
#####################
*/