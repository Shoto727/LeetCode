public class Solution {
    public bool UniqueOccurrences(int[] arr) {
        Dictionary<int, int> freq = new Dictionary<int, int>();

        //1
        foreach (int num in arr) {
            if (freq.ContainsKey(num))
                freq[num]++;
            else
                freq[num] = 1;
        }

        //2
        HashSet<int> occurrences = new HashSet<int>();

        foreach (int count in freq.Values) {
            if (!occurrences.Add(count)) {
                // If Add() returns false → duplicate frequency found
                return false;
            }
        }
        
        return true;
    }
}