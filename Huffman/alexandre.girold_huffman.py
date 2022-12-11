__license__ = 'Junior (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: huffman.py 2022-11-24'

"""
Huffman homework
2022-11
@author: login
"""

from algopy import bintree
from algopy import heap


###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import

###############################################################################
## COMPRESSION

def build_frequency_list(dataIN):
    """
    Builds a tuple list of the character frequencies in the input.
    """
    freq = []
    for i in range(len(dataIN)):
        found = False
        for j in range(len(freq)):
            if freq[j][1] == dataIN[i]:
                freq[j] = (freq[j][0] + 1, freq[j][1])
                found = True
        if not found:
            freq.append((1, dataIN[i]))
    return freq

# L = build_frequency_list("bbaabtttaabtctce")

def __sort_by_freq(tupl_list):
    """
    Sorts the list of tuples by frequency, from biggest to smallest.
    """
    for i in range(1, len(tupl_list)):
        j = i
        while j > 0 and tupl_list[j][0] > tupl_list[j-1][0]:
            tupl_list[j], tupl_list[j-1] = tupl_list[j-1], tupl_list[j]
            j -= 1
    return tupl_list
        

#print(__sort_by_freq(build_frequency_list("dddfgdfgf")))

def build_Huffman_tree(inputList):
    """
    Processes the frequency list into a Huffman tree according to the algorithm.
    """
    H = heap.Heap()
    for el in inputList:
        H.push((el[0], bintree.BinTree(el[1], None, None)))
    while len(H.elts) > 2:
        (c1, t1) = H.pop()
        (c2, t2) = H.pop()
        ht = bintree.BinTree(None, t1, t2)
        H.push((c1 + c2, ht))
    return H.pop()[1]    

# HT = build_Huffman_tree(L)

def __prettyprint(HT):
    """
    Prints the huffman tree as a pretty string.
    """
    # FIXME
    pass
    
        

def __encode_data(huffmanTree, dataIN, elem):
    """
    Encodes the input string to its binary string representation.
    Recursively goes through the tree.
    """
    if huffmanTree.left is None and huffmanTree.right is None:
        if huffmanTree.key == elem:
            return dataIN
        else:
            return ""
    else:
        return (__encode_data(huffmanTree.left, dataIN + "0", elem)
                or __encode_data(huffmanTree.right, dataIN + "1", elem))



def encode_data(huffmanTree, dataIN):
    """
    Encodes the input string to its binary string representation.
    """
    final = ""
    for elem in dataIN:
        final += __encode_data(huffmanTree, "", elem)
    return final
    
# encode_data(HT, 'bbaabtttaabtctce')

def __ascii_to_binary (data):
    """
        Encodes a ascii character into its binary representation. On 8 bits.
    """
    binary = ""
    for i in range(8):
        binary = str(data % 2) + binary
        data = data // 2
    return binary


def __binary_to_asccii (data):
    """
        Decodes a binary string into its int representation.
    """
    int_ = 0
    for i in range(len(data)):
        int_ = int_ * 2 + int(data[i])
    return chr(int_)


def encode_tree(huffmanTree): #Working
    """
    Encodes a huffman tree to its binary representation using a preOrder traversal:
        * each leaf key is encoded into its binary representation on 8 bits preceded by '1'
        * each time we go left we add a '0' to the result
    """
    """
    
    if huffmanTree.left == None:
        if huffmanTree.right == None:
            return __ascii_to_binary(ord(huffmanTree.key))
        else:
            return "1" + encode_tree(huffmanTree.right)
    else:
        if huffmanTree.right == None:
            return "0" + encode_tree(huffmanTree.left)
        else:
            return "1" + encode_tree(huffmanTree.left) + "0" + encode_tree(huffmanTree.right)
    """   
    if huffmanTree.left == None and huffmanTree.right == None:
        return "1" + __ascii_to_binary(ord(huffmanTree.key))
    else:
        return "0" + encode_tree(huffmanTree.left) + encode_tree(huffmanTree.right)
    
    
# print(encode_tree(HT))
# print(len(encode_tree(HT)))
# print(len('0010111010010110001001011000010101100011101100101'))

def to_binary(dataIN):
    """
    Compresses a string containing binary code to its real binary value.
    This code must return a tuple containing the binary string and the number of bits to ignore.
    """
    char, list, bits = '', [], 0
    for element in dataIN:
        char += element
        bits += 1
        if bits == 8:
            list.append(__binary_to_asccii(char))
            char = ''
            bits = 0
    reste = 8 - bits
    if reste == 8:
        reste = 0
    if bits != 0:
        while bits < 8:
            char = "0" + char
            bits += 1
        list.append(__binary_to_asccii(char))
    
    res = ""
    for el in list:
        res += el
    return (res, reste)
            
  
#print(to_binary('01011010010000001010010011000110111'))


def compress(dataIn): #Not the same result as the example
    """
    The main function that makes the whole compression process.
    """
    frequencies = build_frequency_list(dataIn)
    huffmanTree = build_Huffman_tree(frequencies)
    encoded = encode_data(huffmanTree, dataIn)
    encodedTree = encode_tree(huffmanTree)
    binData = to_binary(encodedTree)
    binTree = to_binary(encoded)

    return binTree, binData

#print(compress('bbaabtttaabtctce'))

################################################################################
## DECOMPRESSION

def decode_data(huffmanTree, dataIN):
    """
    Decode a string using the corresponding huffman tree into something more readable.
    """
    # FIXME
    pass

    
def decode_tree(dataIN):
    """
    Decodes a huffman tree from its binary representation:
        * a '0' means we add a new internal node and go to its left node
        * a '1' means the next 8 values are the encoded character of the current leaf         
    """
    # FIXME
    pass


def from_binary(dataIN, align):
    """
    Retrieve a string containing binary code from its real binary value (inverse of :func:`toBinary`).
    """
    # FIXME
    pass


def decompress(data, dataAlign, tree, treeAlign):
    """
    The whole decompression process.
    """
    # FIXME
    pass
