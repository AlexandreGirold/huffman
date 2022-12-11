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
    L = []

    for ele in dataIN:
        added = False
        for count, value in enumerate(L):
            if value[1] == ele:
                L[count] = (value[0] + 1, value[1])
                added = True
                break
        if not added:
            L.append((1, ele))
    return L


def __sort_by_freq(tupl_list):
    l = len(tupl_list)
    for i in range(l):
        for j in range(l-1):
            t1 = tupl_list[j]
            t2 = tupl_list[j+1]
            if t1[0] > t2[0]:
                tupl_list[j + 1], tupl_list[j] = tupl_list[j], tupl_list[j + 1]



print(__sort_by_freq(build_frequency_list("aaenaaddde") ))

def build_Huffman_tree(inputList):
    """
    Processes the frequency list into a Huffman tree according to the algorithm.
    """
    # FIXME
    pass


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
