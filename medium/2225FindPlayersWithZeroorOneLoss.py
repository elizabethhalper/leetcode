# 2225. Find Players With Zero or One Losses

# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:

# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        no_loss = []
        one_loss = []
        loss_dict = {}
        
        for match in matches:
            if match[1] in loss_dict.keys():
                loss_dict[match[1]] += 1
            else:
                loss_dict[match[1]] = 1
            if match[0] not in loss_dict.keys():
                loss_dict[match[0]] = 0
                
        for player in loss_dict:
            if loss_dict[player] == 1:
                one_loss.append(player)
            if loss_dict[player] == 0:
                no_loss.append(player)

        no_loss.sort()
        one_loss.sort()
                
        return [no_loss, one_loss]