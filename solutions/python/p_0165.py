'''
Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:

    If version1 < version2, return -1.
    If version1 > version2, return 1.
    Otherwise, return 0.

Constraints:

    1 <= version1.length, version2.length <= 500
    version1 and version2 only contain digits and '.'.
    version1 and version2 are valid version numbers.
    All the given revisions in version1 and version2 can be stored in a 32-bit integer.

'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = str(version1).split('.')
        version2 = str(version2).split('.')
        

        # initial pass through for the lesser version
        for i in range(max(len(version1), len(version2))):

            # ensures that it's given 0 if the version doesn't exist
            v1 = int(version1[i]) if i < len(version1) else 0
            v2 = int(version2[i]) if i < len(version2) else 0

            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        # else they are the same version
        return 0
