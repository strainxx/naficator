# Jaccard index implementation

def jaccard(A, B):
  # Convert A and B to sets for efficient membership checks
  set_A = set(A)
  set_B = set(B)

  # Calculate intersection and union efficiently
  intersect = len(set_A.intersection(set_B))
  union = len(set_A.union(set_B))

  # Calculate Jaccard Index
  if union == 0:  # Handle division by zero
    return 0
  index = intersect / union

  print(f"--- |A ∩ B| = {intersect} | |A ∪ B| = {union}")
  return index