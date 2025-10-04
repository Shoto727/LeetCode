public class Solution {
    public int[] Intersection(int[] nums1, int[] nums2) {
        HashSet<int> set1 = new HashSet<int>(nums1);
        HashSet<int> common = new HashSet<int>();

        foreach(int num in nums2){
            if(set1.Contains(num)){
                common.Add(num);
            }
        }
        return common.ToArray();
    }
}