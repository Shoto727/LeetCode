public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var dict = new Dictionary<int,int>();
        
        for (int i=0;i<nums.Length;i++){
            int x=nums[i];
            int complement = target-x;

            if(dict.TryGetValue(complement,out int j)){
                return new int[]{j,i};
            }
            dict[x]=i;

        }
        return new int[0];
    }
}