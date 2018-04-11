public class HuffmanCoder {
	
	// the Huffman tree
	private HuffmanTree huffTree;
	
	// an unordered list of encoding data that will be used for encoding a text file into a Huffman-coded compressed file
	private ArrayUnorderedList<EncodingData> encodingList;
	
	/**
	 * Creates the huffTree, using the 4th Huffman tree constructor. It will also call the private helper method
	 * buildEncodingList which will build the list of symbols and their encodings from the Huffman tree huffTree
	 * @param pairsList the ordered list to create a Huffman tree out of
	 */
	public HuffmanCoder(ArrayOrderedList<HuffmanPair> pairsList) {
		huffTree = new HuffmanTree(pairsList);
		encodingList = new ArrayUnorderedList();
		buildEncodingList(huffTree.getRoot(), "");
	}
	
	/** Takes the specified string of binary digits that is a Huffman encoding, and will return the original coded character
	 * @param code the string of binary digits to be decoded
	 */
	public char decode(String code) {
		char character = 0;
		BinaryTreeNode<HuffmanPair> currentNode = huffTree.getRoot();
		char[] charArray = code.toCharArray();
		int i = 0;
		while ((currentNode.getLeft() != null || currentNode.getRight() != null) && i < charArray.length) {
		    	if (charArray[i] == '0') {
		    		currentNode = currentNode.getLeft();
		    	}
		    	else if (charArray[i] == '1') {
		    		currentNode = currentNode.getRight();
		    	}
		    	i++;
		}    
		if (currentNode.isLeaf() && i == charArray.length) {
			character = currentNode.getElement().getCharacter();
		}
		return character;	
	}
	
	/**
	 * Takes the specified character and returns the string representation of the binary Huffman encoding of that character
	 * @param c the character to be encoded
	 * @return the string representation of the binary Huffman encoding of the specified character
	 * @throws ElementNotFoundException if the character cannot be encoded?
	 */
	public String encode(char c) throws ElementNotFoundException {
		for (EncodingData i: encodingList) {
			if (i.getSymbol() == c) {
				return i.getEncoding();
			}
		}
		throw new ElementNotFoundException("Error, character was not found");
	}
	
	/**
	 * Returns a string representation of the encoding list
	 * @return a string representation of the encoding list.
	 */
	public String toString() {
		return encodingList.toString();
	}
	
	/**
	 * Builds the unordered list encodingList from the Huffman tree huffTree and adds new EncodingData objects to encodingList recursively
	 * @param node the node to assess to be added to encodingList
	 * @param encoding the string representation of the binary encoding 
	 */
	private void buildEncodingList (BinaryTreeNode<HuffmanPair> node, String encoding) {
		if (node == null) {
			return;
		}
		
		if (node.isLeaf()) {
			EncodingData encodedNode = new EncodingData(node.getElement().getCharacter(), encoding);
			encodingList.addToRear(encodedNode);
		}
		
		else {
			buildEncodingList(node.getLeft(), encoding+"0");
			buildEncodingList(node.getRight(), encoding+"1");
		}
	}
}
