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

            // Add two numbers
            while (L1 != nullptr && L2 != nullptr) {
                n = L1->val + L2->val + carry;
                carry = n / 10;
                out = new ListNode(n % 10, out);
                L1 = L1->next;
                L2 = L2->next;
            }

            // Add one number
            ListNode* L;
            if (L1 == nullptr) {
                L = L2;
            } else {
                L = L1;
            }
            while (L != nullptr) {
                n = L->val + carry;
                carry = n / 10;
                out = new ListNode(n % 10, out);
                L = L->next;
            }

            // Add zero numbers
            while (carry != 0) {
                n = carry;
                carry = n / 10;
                out = new ListNode(n % 10, out);
            }

            return out;
        }


        ListNode* reverse(ListNode* l) {
            ListNode* L = nullptr;
            while (l != nullptr) {
                L = new ListNode(l->val, L);
                l = l->next;
            }
            return L;
        }
    };
