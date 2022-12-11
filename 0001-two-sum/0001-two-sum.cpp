class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> index;
        
        map<int, int> elementsSeen;

        for(int i = 0; i< nums.size(); i++){
            int difference = target - nums[i];
            if(elementsSeen.count(difference)){
                index.push_back(elementsSeen[difference]);
                index.push_back(i);
                return index;
            }
            elementsSeen.insert({nums[i], i});
        }
        return index;
    }
};