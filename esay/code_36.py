#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/valid-sudoku/

判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

说明:

一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
给定数独序列只包含数字 1-9 和字符 '.' 。
给定数独永远是 9x9 形式的。
"""

def isValidSudoku(board):
  """
  第一次做这道题，真的做的挺久的，估计数学思维全忘光了吧，然后我也挺菜的，23333
  需要做的就是遍历，然后判断是否满足上述的三个条件，如果都满足，返回true，只要一个不满足，则返回false
  不需要考虑是否可解，这就是给出的所有信息了，接下来聊一下解决思路，先来一个正常思维的，不去想那些复杂的数学逻辑
  正常拿到这道题的时候，一般是处理三次，先处理一次行，再处理一次列，最后处理一次3x3
  那么先按照这种思路来做一次试试看
  """

  def checkRow(board):
    # 首先处理行的部分，就是遍历每一行有没有重复的数字
    for i in board:
      # 我们初始化一个数组，让这个数组代表1-9，这里代表了什么，代表了9个false，
      # 每当我们获取到一个数字，例如5，那么我们就将值-1的位置改成true，即row[4]，就可以得到这个值存在过的证明
      row = [False for i in range(9) ]
      for j in i:
        if j != ".":
          num = int(j) - 1
          if row[num]:
            return False
          row[num] = True
    return True

  def checkCol(board):
    # 其次判断列，可以和行做一样的处理，但是列我们只要判断第一行就可以了
    for i in range(9):
      # 和行一样，初始化一个数组，代表这每列的1-9
      # 我们只需要判断col中，1-9是否出现过两次
      col = [False for i in range(9)]
      for j in range(9):
        if board[j][i] != ".":
          num = int(board[j][i]) - 1
          if col[num]:
            return False
          col[num] = True
    return True
  
  def checkBox(board):
    # 最后，来处理最复杂的逻辑，块结构的数据
    # 但有了上面两种思路思路后，也很好处理的
    # 正常情况下，处理一个二维数组是十分复杂的，所以我们需要像一个办法，将二维数组转换成1维的去判断
    # 简单的说就是我们希望像处理行一样去处理块级的二维数组
    # 怎么实现，我们将9宫格分成了9个部分，那么只需要通过一个公式，将每个宫格内的任意一个元素，都能通过计算后变成一个固定的值
    # 例如，board[0][0], board[0][2], board[2][2]都是第一个宫格内，我们创造一个公式，去处理这些index，变成一个相同的值
    # 这里我就直接贴出答案了，我们值需要相除取整即可，用到python的“//”表达式
    # 即：block = i//3*3 + j//3, 为什么要i//3*3，因为横向是0，1，2，纵向是0，3，6
    # 获取到这个公式，即可以对每一个区块内，进行处理了
    block = [[False for i in range(9)] for j in range(9)]
    for i in range(9):
      for j in range(9):
        if board[i][j] != ".":
          num = int(board[i][j]) - 1
          k = i//3*3 + j//3
          if block[k][num]:
            return False
          block[k][num] = True
    return True

  print(checkRow(board))
  print(checkCol(board))
  print(checkBox(board))
  if not checkRow(board) or not checkCol(board) or not checkBox(board):
    return False
  return True


def isValidSudoku2(board):

  """
  第一种思路做着做着的时候，你发现完全是可以合并的，于是有了这种简化的思路
  我们分别为row,col,block创造了一个9*9的九宫格，借此来验证行，列，块的重复与否
  """
  row = [[False for i in range(9)] for j in range(9)]
  col = [[False for i in range(9)] for j in range(9)]
  block = [[False for i in range(9)] for j in range(9)]

  for i in range(9):
    for j in range(9):
      if board[i][j] != '.':
        # 获得这个数字，因为要放进数组中去，所以要-1，因为数组通过0-8表示1-9
        num = int(board[i][j]) - 1
        k = i//3*3 + j//3
        if row[i][num] or col[j][num] or block[k][num]:
          return False
        row[i][num] = col[j][num] = block[k][num] = True
  return True


# 解答中，还有一些更快的答案，不过大概思路也是如此，即通过行，列，块分析
# 有的答案对行分析用了这种写法 len(set(board[i])) - 1 < 9 - tmp，tmp是一行中‘.’的个数，以此来判断是否有重复值
  
