class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        test=True
        n=0

        while test:
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    test = False
                    break

            if test:
                break

            nb = float('inf')
            n += 1

            for i in range(len(nums) - 1):
                if (nums[i] + nums[i + 1]) < nb:
                    nb = nums[i] + nums[i + 1]
                    j = i

            nums = nums[0:j] + [nb] + nums[j + 2:]
            test = True

        return n