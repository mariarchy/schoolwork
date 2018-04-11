
public class Decompress {

	public static void main(String[] args) {
		System.out.println("Name of file to decompress: "+args[0]);
		System.out.println("Name of file storing compression codes: "+args[1]);
	
		String output = args[0].substring(0, args[0].length() - 3) + "dec";
		TextFile codeFile = new TextFile(args[1],"read");			// prepares the file of codes to be read
		TextFile textFile= new TextFile(output,"write");		// prepares the file of uncompressed code to be read and compressed
		CompressedFile compressedFile = new CompressedFile(args[0],"read");		// prepares a new file to write the compressed code to
		// create an array for storing the codes for compressing
		ArrayCode codeKey = new ArrayCode(50);
		char character;
		String bit; 
		String code;
		char char1;
		int codePosition;
				
		character = codeFile.readChar();	// reads the first character in the line
		while (character != (char)0) {		// makes sure the end of the file has not been reached
			code = codeFile.readLine();		// reads the code from the line and stores it into code
			CodePair newCode = new CodePair(character, code);		// creates the CodePair to be added into the codeKey array
			codeKey.add(newCode);
			character = codeFile.readChar(); 	// reads the first character of the next line
		}
		

		bit = Character.toString(compressedFile.readBit()); 			// reads the first character
		while (bit.charAt(bit.length() - 1) != (char)0) {				// makes sure the end of the file has not been reached
			codePosition = codeKey.findCode(bit);			// finds the position of the bit entered
			if (codePosition != -1) {		// if the code is in the array of codes this will write the corresponding character to a new file

				char1 = codeKey.getCharacter(codePosition);
				textFile.writeChar(char1);
				bit = Character.toString(compressedFile.readBit());
			}
			// if the bit are not found in the array of code this will add the next character and look through again 
			else bit = bit + Character.toString(compressedFile.readBit());
		}
		
		codeFile.close();			// closes the files
		compressedFile.close();
		textFile.close();
		

	}

}
