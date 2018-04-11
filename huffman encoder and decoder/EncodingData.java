public class EncodingData {

	private char symbol;				// a symbol that is to be encoded
	private String encoding;			// the binary Huffman code of the symbol (i.e. a string of 0’s and 1’s)
	
	/** 
	 * Creates an empty stack using an array of length equal to the value of initialCapacity
	 * @param initialCapacity the specified capacity
	 * @param maxCap the maximum size for the array
	 */
	public EncodingData(char symbol, String encoding) {
		this.symbol = symbol;
		this.encoding = encoding;
	}
	
	/** 
	 * Returns the symbol for the given EncodingData object
	 * @return the symbol for this object
	 */
	public char getSymbol() {
		return symbol;
	}
	
	/** 
	 * Returns the binary Huffman code string for the given EncodingData object
	 * @return the binary Huffman code string for this object
	 */
	public String getEncoding() {
		return encoding;
	}
	
	/** 
	 * Sets the binary Huffman code for the corresponding symbol
	 * @param newCode the new Huffman code to be set to the corresponding symbol
	 */
	public void setEncoding(String newCode) {
		encoding = newCode;
	}
	
	/** 
	 * Determines if two EncodingData objects are equal based on the symbol attribute
	 * @param obj the EncodingData object to compare the current EncodingData object to
	 * @return whether or not two Huffman objects have the same symbol
	 */
	public boolean equals(Object obj) {
		EncodingData other = (EncodingData) obj;
		return (this.getSymbol() == other.getSymbol());
	}
	
	/**
	* Gives a string representation of the symbol and its Huffman code
	* @return a string representation of the symbol and Huffman code
	*/
	public String toString() {
		return ("Symbol: " + getSymbol() + " Huffman Code: " + getEncoding());
	}
}
