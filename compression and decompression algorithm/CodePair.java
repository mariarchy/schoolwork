
// creates an object that contains the character and corresponding code for compression
public class CodePair {

	private char character;
	private String code;

	/**
	 * initializes the character and code
	 * 
	 * @param c the character to compress
	 * @param code the code corresponding to the character
	 */
	public CodePair(char c, String code) {
		this.character = c;
		this.code = code;
	}
	
	/**
	 * accesses the code corresponding to the character
	 * 
	 */
	public String getCode(){
		return this.code;
	}
	
	/**
	 * accesses the character to compress
	 * 
	 */
	public char getCharacter(){
		return this.character;
	}
	
	/**
	 * sets the character of the CodePair
	 * 
	 * @param c the character to override the previous character
	 */
	public void setCharacter(char c){
		this.character = c;
	}
	
	/**
	 * takes the parameter size and creates an array of the parameter size
	 * 
	 * @param code
	 */
	public void setCode(String code){
		this.code = code;
	}
	
	/**
	 * verifies if one CodePair is equal to another 
	 * 
	 * @param anotherPair the CodePair object to compare to
	 */
	public boolean equals(CodePair anotherPair) {
		if ((this.getCode() == anotherPair.getCode()) && (this.getCharacter() == anotherPair.getCharacter())) {
			return true;
		}
		else {
			return false;
		}
	}
	
	/**
	 * formats the information in the object to proper string representation
	 * 
	 */
	public String toString() {
		String s = character + " " + "\t" + code;
		return s;
	}

}