// 两数相加
// 地址：https://leetcode.cn/problems/add-two-numbers/

// 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

// 请你将两个数相加，并以相同形式返回一个表示和的链表。

// 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  // 进位
  let carry = 0

  let result: ListNode | null = new ListNode(0, null)

  let head: ListNode | null = null
  let isInit: boolean = true

  let curL1 = l1
  let curL2 = l2

  while(curL1 || curL2) {
    let value = (curL1?.val ?? 0) + (curL2?.val ?? 0) + carry
    
    curL1 = curL1?.next ?? null
    curL2 = curL2?.next ?? null
    
    if (value >= 10) {
      value = value % 10
      carry = 1
    } else {
      carry = 0
    }

    const node = new ListNode(value, null)
    result.next = node
    result = result?.next
    if (isInit) {
      isInit = false
      head = node
    } 
  }

  if (carry) {
    result.next = new ListNode(1, null)
  }
  return head
};