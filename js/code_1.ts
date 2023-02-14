// 两数之和
// 连接：https://leetcode.cn/problems/two-sum/

// 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

// 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

// 你可以按任意顺序返回答案。

// 常规思路：O(n^2) 
function twoSum(nums: number[], target: number): number[] {
  for (let i = 0; i < nums.length; i++) {
    const targetValue = target - nums[i]
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[j] === targetValue) {
        return [i, j]
      }
    }
  }
  return []
}

// 空间换时间：O(n)
function twoSum2(nums: number[], target: number): number[] {
  const dict = {}
  for (let i = 0; i < nums.length; i++) {
    const targetValue = target - nums[i]
    if (targetValue !== undefined) {
      return [i, dict[targetValue]]
    }
    dict[nums[i]] = i
  }
  return []
}