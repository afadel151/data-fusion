import numpy as np



def generate_matrice(s:int,d:int):
    res = np.zeros((s, d), dtype=int)
    random_cols = np.random.randint(0, d, size=s)
    res[np.arange(s), random_cols] = 1
    return res


def combine_decisions(decisions_matrix: np.ndarray):
    shape = decisions_matrix.shape
    print(f"sources  : {shape[0]}")
    print(f"decisions  : {shape[1]}")
    vect = np.zeros((shape[1],),dtype=int)
    for k in range(shape[1]):
        comb = 0
        for j in range(shape[0]):
            comb = comb + decisions_matrix[j,k]
        vect[k] = comb
    
    print(vect)
    return vect


def majority_vote(vector: np.ndarray):
    max = np.amax(vector)
    index = np.argmax(vector)
    count = np.sum(vector == vector.max())
    if(count> 1):
        print(f"can't decide the major vote, there is {count} decisions with {max} votes")
        return vector.size + 1
    print(f"maximum: {max}, index: {index + 1}, count: {count}")
    return index + 1 


def absolute_majority_vote(vector: np.ndarray):
    sources = np.sum(vector)
    max = np.amax(vector)
    index = np.argmax(vector)
    count = np.sum(vector == vector.max())
    if(count > 1):
        print(f"can't decide the major vote, there is {count} decisions with {max} votes")
        return vector.size + 1
    if(max > sources/2):
        return index +1 
    else:
        print(f"can't decide the major vote, {max} is less than {sources/2}")
        return vector.size +1


def random_reliability(s: int):
    return np.random.ranf(s)

def normalize_vector(vector: np.ndarray):
    sum = vector.sum()
    print(f"sum of reliability : {sum}")
    if sum == 0 :
        return np.zeros_like(vector, dtype=float)
    normalized = vector / sum
    return normalized
    

def compute_with_reliability(matrix: np.ndarray,reliability_vector: np.ndarray):
    return matrix * reliability_vector.reshape(-1, 1)
    

    
matrix = generate_matrice(5,6)
reliabilty_vector = random_reliability(5)
print(f"reliability vector : {reliabilty_vector}")
print(f"original matrix: {matrix}")
print(f"with reliability : {compute_with_reliability(matrix,reliability_vector=reliabilty_vector)}")
# vect = combine_decisions(matrix)

# print(f"max index:  {absolute_majority_vote(vect)}")


# print(normalize_vector(reliabilty_vector))