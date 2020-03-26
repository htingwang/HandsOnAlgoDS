class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        vector<string> res;
        queue<string> q{{s}};
        unordered_set<string> seen{{s}};
        bool found = false;
        while (!q.empty()) {
            string cur = q.front(); q.pop();
            if (isValid(cur)) {
                res.push_back(cur);
                found = true;
            }
            if (found) continue;
            for (int i = 0; i < cur.size(); i++) {
                if (cur[i] == '(' || cur[i] == ')') {
                    string next = cur.substr(0, i) + cur.substr(i + 1);
                    if (!seen.count(next)) {
                        q.push(next);
                        seen.insert(next);
                    }
                }
            }
        }
        return res;
    }
    bool isValid(string s) {
        int cnt = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') cnt++;
            if (s[i] == ')') {
                if (cnt == 0) return false;
                cnt--;
            }
        }
        return cnt == 0;
    }
};
