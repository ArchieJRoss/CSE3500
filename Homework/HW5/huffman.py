import heapq

def frequency(file):
    # create a dictionary to efficiently store the frequency of each nucleotide
    frequency_dictionary = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    
    # open the text file and read its contents
    with open(file, 'r') as f:
        contents = f.read().upper()

    # iterate through each nucleotide in the contents, and increment the count for its corresponding key in the dictionary
    for nucleotide in contents:
        if nucleotide in frequency_dictionary:
            frequency_dictionary[nucleotide] += 1

    return frequency_dictionary


def huffman(dictionary):
    # create a heap list of the frequency dictionary items, where each item is a list [frequency, [nucleotide, code]]
    heap = [[amount, [nucleotide, ""]] for nucleotide, amount in dictionary.items()]
    
    # heapify the list so that it can be used to create the Huffman tree
    heapq.heapify(heap)

    # repeatedly extract the two lowest frequency items from the heap, merge them into a new tree node, and re-insert the tree node into the heap
    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)
        
        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        
        for pair in high[1:]:
            pair[1] = '1' + pair[1]
        
        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

    # the last item remaining in the heap is the Huffman tree, represented as a list where the first element is the total frequency
    # and the rest of the elements are the nucleotides and their binary codes
    tree = heapq.heappop(heap)
    
    # create a dictionary from the binary codes in the tree, where the nucleotides are the keys and the codes are the values
    bin = dict(tree[1:])

    return tree, bin

    
def encode(sequence, codes):
    # create an empty string to store the binary encoding of the sequence
    encoded = ""
    
    # iterate through each nucleotide in the sequence, and append its binary code to the encoded string
    for nucleotide in sequence:
        encoded += codes[nucleotide]
        
    return encoded


def compress_file(input_file, output_file):
    # get the frequency of nucleotides in the input file
    frequency_of = frequency(input_file)
    
    # create the Huffman tree and binary codes from the frequency dictionary
    tree, bin = huffman(frequency_of)
    
    # open the input file and read its contents
    with open(input_file, 'r') as i:
        sequence = i.read().upper()
        
        # encode the sequence using the binary codes
        encoded = encode(sequence, bin)

    # write the encoded binary string to the output file
    with open(output_file, 'w') as o:
        o.write(encoded)

        


if __name__ == '__main__':
    compress_file("dna.txt", "compressed.txt")
