class Solution {
public:
    bool isPalindrome(int x) {

        // palindrome can't be a negative and can't end end in 0 unless it's 0
        if (x < 0 || (x != 0 && x % 10 == 0)){
            return false;
        }
        
        int xReversed = 0;

        // loops to store the first half of x's digits or the first half of x's digits +1 if x has odd number of digits
        while(xReversed < x){
            xReversed *= 10; // increase digit
            xReversed += x % 10; // add the 1ths place of x to xReversed
            x /= 10; // decrease digit
        }

        // xReversed/10 is used to ignore median if x has odd digits
        return xReversed == x || xReversed/10 == x;

        /* First Attempt
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

        // runs log(n) times to check if palindrome
        while(isPalindrome && front != middle){
            isPalindrome = (listOfX[front] == listOfX[back]) ? true : false;
            front++;
            back--;
        }

        return isPalindrome; 
        */
    }
};