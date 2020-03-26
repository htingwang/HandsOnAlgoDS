class Solution {
public:
    vector<int> findPermutation(string s) {
        int n = s.size();
#if 0
        vector<int> res(n + 1);
        for (int i = 0; i < n + 1; ++i) res[i] = i + 1;
        for (int i = 0; i < n; ++i) {
            //printf("%d\n", i);
            if (s[i] == 'I') continue;
            int j = i;
            while (s[i] == 'D' && i < n) ++i;
            reverse(res.begin() + j, res.begin() + i + 1);
            --i;
        }
#else
        vector<int> res;
        for (int i = 0; i < n + 1; ++i) {
            if (i == n || s[i] == 'I') {
                int size = res.size();
                for (int j = i + 1; j > size; --j) {
                    res.push_back(j);
                }
            }
        }
#endif
        return res;
    }
};
