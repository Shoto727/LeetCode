public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        var lastIndex=new Dictionary<int,int>();
        for(int i=0;i<nums.Length;i++){
            int x=nums[i];

            if(lastIndex.TryGetValue(x,out int prevIndex)){
                if (i - prevIndex <= k) {
                return true;
            }
        }
    lastIndex[x]=i;
        }
        return false;
    }
}