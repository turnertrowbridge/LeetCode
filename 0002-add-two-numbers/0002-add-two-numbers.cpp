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

        
        ListNode *addedList = new ListNode(0);  // create new ListNode for the addedList
        ListNode *l3 = addedList;   // create l3 to traverse addedList

        int carryOut = 0;   // store a carryOut value outside the loop

        // loop while at least one ListNode has values next
        while(l1 || l2 || carryOut != 0){

            // create an int that either sets the value to the ListNode's value or 0 if ListNode is nullptr
            int l1Value = l1 ? l1->val : 0;
            int l2Value = l2 ? l2->val : 0;
            
            int sum = l1Value + l2Value + carryOut;     // add values with the carryOut
            carryOut = sum / 10;    // carryOut stores the values not in the current place

            l1 = l1 ? l1->next : nullptr;   // shift l1 to the next value or keep it at nullptr
            l2 = l2 ? l2->next : nullptr;   // shift l2 to the next value or keep it at nullptr
            l3->next = new ListNode(sum % 10);  // add the current place values to addedList
            l3 = l3->next;  // move to next value in addedList
    }
        return addedList->next;     // addedList initializes with 0, so return all the nodes in addedList after that
    }
};