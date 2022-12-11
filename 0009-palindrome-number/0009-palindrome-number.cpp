class Solution {
public:
    bool isPalindrome(int x) {

        vector<int> listOfX;
        bool isPalindrome = true;

        // negative can't be a palindrome
        if (x < 0){
            return false;
        }

        // move values into vector
        while(x != 0){
            listOfX.push_back(x % 10);
            x /= 10;
        }

        int front = 0;
        int back = listOfX.size() - 1;
        int middle = listOfX.size() / 2;

        // runs n/2 times to check if palindrome
        while(isPalindrome && front != middle){
            isPalindrome = (listOfX[front] == listOfX[back]) ? true : false;
            front++;
            back--;
        }

        return isPalindrome; 
    }
};