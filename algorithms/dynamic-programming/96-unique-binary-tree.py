"""
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
Input: n = 3
Output: 5
"""

"""
G(n) = F(1, n) + F(2, n) + ... + F(n, n). 
Base case: G(0)=1, G(1)=1. 
F(i, n) = G(i-1) * G(n-i)	1 <= i <= n 
==> combine: G(n) = G(0) * G(n-1) + G(1) * G(n-2) + … + G(n-1) * G(0) 


public int numTrees(int n) {
  int [] G = new int[n+1];
  G[0] = G[1] = 1;
    
  for(int i=2; i<=n; ++i) {
    for(int j=1; j<=i; ++j) {
      G[i] += G[j-1] * G[i-j];
    }
  }
  return G[n];
}
"""
