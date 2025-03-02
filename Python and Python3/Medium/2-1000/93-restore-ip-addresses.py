class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        size = len(s)
        validIps = []
        for i in range(1 , size - 2):
            j = i + 1
            startj = j
            k = size - 1

            tmpString = s[:i] + "." + s[i:j] + "." + s[j:k] + "." + s[k:]
            splitted = tmpString.split('.')
            if int(splitted[0]) > 255 or (len(splitted[0]) > 1 and splitted[0][0] == "0"):
                continue
            
            while j < k:
                tmpString = s[:i] + "." + s[i:j] + "." + s[j:k] + "." + s[k:]
                splitted = tmpString.split('.')
                if int(splitted[1]) > 255 or (len(splitted[1]) > 1 and splitted[1][0] == "0"):
                    break

                if int(splitted[2]) > 255 or (len(splitted[2]) > 1 and splitted[2][0] == "0"):
                    if (len(splitted[2]) >= 2 and len(splitted[3]) < 3 and int(splitted[3]) < 255) or (len(splitted[2]) > 3 and len(splitted[3]) < 3):
                        if j < size - 1 and j == k - 1:
                            j = j + 1
                            k = size - 1
                        else:
                            k = k - 1
                    else:
                        j = j + 1
                        k = size - 1
                    continue

                if int(splitted[3]) > 255 or (len(splitted[3]) > 1 and splitted[3][0] == "0"):
                    if (startj == k - 1) or ((j < size - 1) and j == k - 1):
                        j = j + 1
                        k = size - 1
                    else:
                        k = k - 1
                    continue

                validIps.append(tmpString)
                if (startj == k - 1) or ((j < size - 1) and j == k - 1):
                    j = j + 1
                    k = size - 1
                else:
                    k = k - 1
        return validIps   

