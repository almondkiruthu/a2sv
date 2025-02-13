# Problem: Design Authentication Manager - https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time_to_live = timeToLive
        self.d = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        expire_time = currentTime + self.time_to_live
        self.d[tokenId] = expire_time
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.d:
            # get expire time for current token id
            token_expire_time = self.d[tokenId]

            # update only the none expired tokens
            if token_expire_time > currentTime:
                    new_expire_time = currentTime + self.time_to_live
                    self.d[tokenId] = new_expire_time


    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for expired_time in self.d.values():
            if expired_time > currentTime:
                count += 1

        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)