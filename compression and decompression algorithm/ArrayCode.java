/**
 * Creates an array with objects of CodePair as elements
 */
public class ArrayCode {
	private int size;
	private int numPairs;
	private CodePair[] codeArray;
	
	/**
	 * takes the parameter size and creates an array of the parameter size
	 * 
	 * @param int
	 *            size of the array
	 */
	public ArrayCode(int size) {
		this.size = size;
		codeArray = new CodePair[size];
		numPairs = 0;
		
	}
	/**
	 * Adds the CodePair object to the array
	 * 
	 * @param codePair
	 *            takes the object of class CodePair to add to the array 
	 */
	public void add(CodePair codePair) {
		// why do i need this for newSize to work as the array size
		int newSize = size;
		if (numPairs == size) {
			if (size <= 100) {
				newSize = codeArray.length * 2;
			}
			else if (size > 100) {
				newSize = codeArray.length + 20;
			}
			size = newSize;
			CodePair[] newCodeArray = new CodePair[size];
			newCodeArray[numPairs] = codePair;
			for (int i = 0; i < codeArray.length; i++)
				newCodeArray[i] = codeArray[i];
			codeArray = newCodeArray;
			}
		
		codeArray[numPairs] = codePair;
		numPairs++;
		
	}
	/**
	 * Removes the specified CodePair object from the array
	 * 
	 * @param pairToRemove	
	 *           the CodePair object that is to be removed from the array     
	 */
	public void remove(CodePair pairToRemove){
		int i = findCharacter(pairToRemove.getCharacter());
		
		if (i == -1) {
			return;
		}
		// replaces pairToRemove with the last element in the array 
		codeArray[i] = codeArray[numPairs-1];
		codeArray[numPairs-1] = null;
		numPairs--;
		
		// reduces the size of the array if the number of pairs is less than 1/4 of the maximum size of the array
		if (numPairs < (size / 4)) { 
			int newSize = size/2;
			CodePair[] newCodeArray = new CodePair [newSize];
			for (int j = 0; j < newSize; j++)
				newCodeArray[j] = codeArray[j];
			codeArray = newCodeArray;
			size = newSize;
			
		}
		}
	
	/**
	 * accesses the CodePair in the specified index 
	 * 
	 * @param index the position of the array to access
	 */
	// allows user to reference a specific index/codePair
	// check if more efficient way to do this without this method
	public CodePair getPair(int index) {
		return codeArray[index];
	}
	
	/**
	 * searches the array for the specified code
	 * 
	 * @param code the code to search for in the array
	 * @return returns the position of the corresponding CodePair in the array or -1 if the corresponding CodePair is not found
	 */
	public int findCode(String code) {
		for (int i = 0; i < numPairs; i++) {
			if (codeArray[i].getCode().equals(code)) {
				return i;
			}
		}
		return -1;
		}
	
	/**
	 * searches the array for the specified character
	 * 
	 * @param character the character to search for in the array
	 * @return returns the position of the corresponding CodePair in the array or -1 if the corresponding CodePair is not found
	 */
	public int findCharacter(char character) {
		for (int i = 0; i < numPairs; i++) {
			if (codeArray[i].getCharacter() == character) {
				return i;
			}
		}
			return -1;
	}
	
	/**
	 * accesses the code in the specified position
	 * 
	 * @param i the specified position the user wants to access
	 * @return returns the code of the corresponding CodePair in the specified position or null if the position does not exist in the array
	 */
	public String getCode(int i) {
		if ((i < numPairs) && (i >= 0)) {
			return codeArray[i].getCode();
		}
		return null;
	}
	
	/**
	 * searches the array for the specified code
	 * 
	 * @param code the code to search for in the array
	 * @return returns the position of the corresponding CodePair in the array or -1 if the corresponding CodePair is not found
	 */
	public char getCharacter(int i) {
		if ((i < numPairs) && (i >=0)) {
			return codeArray[i].getCharacter();
		}
		return 0;
	}
	
	/**
	 * returns the size of the array
	 *
	 * @return returns the size of the array
	 */
	public int getSize() {
		return size;
	}
	
	/**
	 * returns the number of pairs in the array 
	 *
	 * @return returns the number of pairs in the array
	 */
	public int getNumPairs() {
		return numPairs;
	}
}	
