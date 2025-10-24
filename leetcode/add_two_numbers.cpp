// https://leetcode.com/problems/add-two-numbers-ii/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* L1 = reverse(l1);
        ListNode* L2 = reverse(l2);


        int n;
        int carry = 0;
        ListNode* out = nullptr;

        while (L1 != nullptr && L2 != nullptr) {
            n = L1->val + L2->val + carry;
            carry = n / 10;
            out = new ListNode(n % 10, out);
            L1 = L1->next;
            L2 = L2->next;
        }
        ListNode* L;
        if (L1 == nullptr) {
            L = L1;
        } else {
            L = L2;
        }
        while (L != nullptr) {
            n = L->val + carry;
            carry = n / 10
            out = new ListNode(n % 10, out);
            L = L->next
        }
        return out;
    }

    // ListNode* add(ListNode* L1, ListNode* L2, int carry) {


    // }

    ListNode* reverse(ListNode* l) {
        ListNode* L = nullptr;
        while (l != nullptr) {
            L = new ListNode(l->val, L);
            l = l->next;
        }
        return L;
    }
};
