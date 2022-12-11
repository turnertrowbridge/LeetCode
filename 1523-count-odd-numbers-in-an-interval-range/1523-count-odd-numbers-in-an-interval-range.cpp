class Solution {
public:
    int countOdds(int low, int high) {

        int amountOfOddNums = 0;

        for(int i = low; i <= high; i++){
            if(i%2 != 0){
                amountOfOddNums++;
            }
        }

        return amountOfOddNums;
    }
};