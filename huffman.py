import heapq
from collections import defaultdict

# Node class to represent each character in the Huffman tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # To ensure that the heapq works correctly based on frequency
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman tree
def build_huffman_tree(char_freq):
    heap = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

# Function to generate Huffman codes
def generate_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.char is not None:  # If it's a leaf node
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

# Main function to perform Huffman encoding
def huffman_encoding(data):
    # Count frequency of each character
    char_freq = defaultdict(int)
    for char in data:
        char_freq[char] += 1

    # Build Huffman tree
    huffman_tree = build_huffman_tree(char_freq)

    # Generate Huffman codes
    huffman_codes = generate_codes(huffman_tree)

    # Encode the data using the Huffman codes
    encoded_output = ''.join(huffman_codes[char] for char in data)
    return encoded_output, huffman_codes

# Example usage
if __name__ == "__main__":
    data = "hello huffman"
    encoded_data, codes = huffman_encoding(data)

    print("Original Data:", data)
    print("Encoded Data:", encoded_data)
    print("Huffman Codes:", codes)


#next import heapq 
class Node: 
    def __init__(self, freq, char, l=None, r=None): 
        self.freq = freq 
        self.char = char 
        self.l = l 
        self.r = r 
        self.code = '' 

    def __lt__(self, other): 
        return self.freq < other.freq 

def generateCodes(node, code_val=''): 
    code_val += str(node.code) 
    if node.l: 
        generateCodes(node.l, code_val) 
    if node.r: 
        generateCodes(node.r, code_val) 
    if not node.l and not node.r: 
        print(f"{node.char} -> {code_val}") 


n = int(input("Enter the number of characters: "))
chars = []
freqs = []

for i in range(n):
    char = input(f"Enter character {i+1}: ")
    chars.append(char)
    freq = int(input(f"Enter frequency of {char}: "))
    freqs.append(freq)

heap = [] 

for i in range(len(chars)): 
    heapq.heappush(heap, Node(freqs[i], chars[i])) 

while len(heap) > 1: 
    l = heapq.heappop(heap) 
    r = heapq.heappop(heap) 
    l.code = 0
    r.code = 1
    new_node = Node(l.freq + r.freq, l.char + r.char, l, r) 
    heapq.heappush(heap, new_node) 

print("Huffman Codes:")
generateCodes(heap[0])