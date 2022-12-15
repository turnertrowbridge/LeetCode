class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int totalSum = 0;
        for(int i = 0; i < nums.size(); i++){
            totalSum += nums[i];
        }
        int runningSum = 0;
        for (int i = 0; i < nums.size(); i++){

            // compare the runningSum to then sum on the other side of currentindex;
            if(runningSum == totalSum - runningSum - nums[i]){ 
                return i;
            }
            
            runningSum += nums[i];
        }
        return -1;
    }
};