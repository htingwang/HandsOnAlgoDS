class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        dp = {0 : []}
        skills_to_idx = {skills : 1 << i for i, skills in enumerate(req_skills)}
        
        for i, p in enumerate(people):
            cur_skills = 0
            for s in p:
                cur_skills |= skills_to_idx[s]

            for skills, team in list(dp.items()):
                comb_skills = skills | cur_skills
                if comb_skills == skills: continue
                if comb_skills not in dp or len(dp[comb_skills]) > len(team) + 1:
                    dp[comb_skills] = team + [i]
                    
        return dp[(1 << len(req_skills)) - 1]
