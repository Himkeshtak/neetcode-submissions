class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> subset;
        dfs(nums, 0, subset, res);
        return res;
    }

private:
    void dfs(const vector<int>& nums, int i, vector<int>& subset, vector<vector<int>>& res) {
      if (i >= nums.size()) {
    res.push_back(subset);

    cout << "Added subset: [ ";
    for (int x : subset) {
        cout << x << " ";
    }
    cout << "]\n";

    return;
}
        cout<<" i value is "<< i<< " push "<<endl;
        subset.push_back(nums[i]);
        cout<<" i value is "<< i<< " DFS "<<endl;
        dfs(nums, i + 1, subset, res);
        cout<<" i value is "<< i<< " pop "<<endl;
        subset.pop_back();
        cout<<" i value is "<< i<< " DFS "<<endl;
        dfs(nums, i + 1, subset, res);
    }
};