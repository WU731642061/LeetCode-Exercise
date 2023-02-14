#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/rotate-image/

给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。

说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
"""


def rotate(matrix):
  """
  这道题当时看到的第一反应式用python的zip方法，很快就能解决
  但是既然是刷算法，就要考虑到普遍性，尽量的不要借助这些特殊的方法去处理
  第一种思路先用zip来解决
  """
  # 先将数组，倒序，解构后丢进zip函数，可以得到类似于这样的结果[(7,4,1),(8,5,2),(9,6,3)]
  matrix[::] = zip(*matrix[::-1])
  # 再通过map，依次将tuple转换成list
  matrix = list(map(list, matrix))


def rotate2(matrix):
    """
    如何不通过原生方法去实现这个旋转，同时在原地操作，因为有额外空间的话，这道题就没有难度了，这是需要思考的问题
    直接旋转90度，是不可行的，但是可以将这个步骤拆解成两步，不妨自己拿一张纸片出来，上面按顺序写上1-9，类似题目中的那样
    我们虽然不能操作数组的旋转，但是我们可以操作数组的位置顺序
    我们试着以5为中心，垂直方向180度旋转纸片，会得到一张反过来的结果，同时会发现789在上，123在下了
    然后以当前纸片的‘左对角’线为基准，再次反转数组，就得到旋转90度的纸片了
    也就是达到了我们所谓的，无法直接旋转数组，但是通过改变数组位置去实现
    这道题的解法我也是先从网上看来的，我通过答案去逆推思路，因此也许有更好的思考方式，我暂时没想到
    接下来就是解法的实现
    """

    # 垂直旋转，很容易处理，就是倒叙排列整个二维数组
    matrix[:] = matrix[::-1]
    length = len(matrix)
    # 翻转的过程就像是以左对角线为中心，数字一一互换，因为我们只需要遍历对角线一边的数据即可
    for i in range(length):
      for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]