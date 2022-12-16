class Solution {
private:
int getDigitSum(int n){
    int sum = 0;
    while(n > 0){
        int digit = n % 10;
        n /= 10;
        sum += digit*digit;
    }

    return sum;
}


public:
    bool isHappy(int n) {
        set<int> seenNums; 
        while(n != 1 && !seenNums.count(n)){
            seenNums.insert(n);
            n = getDigitSum(n);
        }
        return n == 1;
    }
};