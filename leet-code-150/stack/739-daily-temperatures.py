"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""

"""
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        
        int n = temperatures.size();
        vector<int>nge(n, 0); // initially all 0, stores distance between their next greater element and current temperature
        stack<int>st{};
        
        // move from right to left
        for(int i = n-1; i>=0; --i){
            // pop until we find next greater element to the right
            // since we came from right stack will have element from right only
            // s.top() is the index of elements so we put that index inside temperatures vector to check
            while(!st.empty() && temperatures[st.top()] <= temperatures[i])
                st.pop();
				
            // if stack not empty, then we have some next greater element, 
            // so we take distance between next greater and current temperature
            // as we are storing indexes in the stack
            if(!st.empty())
                nge[i] = st.top()-i; // distance between next greater and current
            
            // push the index of current temperature in the stack,
            // same as pushing current temperature in stack
            st.push(i);
        }
        
        return nge;
    }
};
"""
