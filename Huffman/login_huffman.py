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

L = build_frequency_list("bbaabtttaabtctce")

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
    Build a heap by iterating over the list stating at the end of the list.
    """
    H = heap.Heap()
    for el in inputList:
        H.push((el[0], bintree.BinTree(el[1], None, None)))
    return H

HT = build_Huffman_tree(L)

def prettyprint(HT):
    """
    Prints the huffman tree as a pretty string.
    """
    
        


def encode_data(huffmanTree, dataIN):
    """
    Encodes the input string to its binary string representation.
    """
    # FIXME
    pass


def encode_tree(huffmanTree):
    """
    Encodes a huffman tree to its binary representation using a preOrder traversal:
        * each leaf key is encoded into its binary representation on 8 bits preceded by '1'
        * each time we go left we add a '0' to the result
    """
    # FIXME
    pass


def to_binary(dataIN):
    """
    Compresses a string containing binary code to its real binary value.
    """
    # FIXME
    pass


def compress(dataIn):
    """
    The main function that makes the whole compression process.
    """
    
    # FIXME
    pass

    
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
