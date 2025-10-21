public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length)
            return false;

        char[] sArr = s.ToCharArray();
        char[] tArr = t.ToCharArray();

        Array.Sort(sArr);
        Array.Sort(tArr);

        return new string(sArr) == new string(tArr);
    }
}