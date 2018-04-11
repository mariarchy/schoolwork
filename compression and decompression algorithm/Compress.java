public class Compress {
	
	public static void main(String[] args) {
		System.out.println("Name of file to compress: "+args[0]);
		System.out.println("Name of file storing compression codes: "+args[1]);
	
		String output = args[0].substring(0, args[0].length() - 3) + "zzz";
		TextFile codeFile = new TextFile(args[1],"read");			// prepares the file of codes to be read
		TextFile compressFile = new TextFile(args[0],"read");		// prepares the file of uncompressed code to be read and compressed
		CompressedFile outputFile = new CompressedFile(output,"write");		// prepares a new file to write the compressed code to
		// create an array for storing the codes for compressing
		ArrayCode codeKey = new ArrayCode(50);
		char character;
		char uncompressedChar; 
		String code;
		char[] charCode;
		int codePosition;
		
		character = codeFile.readChar();		// reads the first character in the line
		while (character != (char)0) {		// makes sure the end of the file has not been reached
			code = codeFile.readLine();		// reads the code from the line and stores it into code
			CodePair newCode = new CodePair(character, code);		// creates the CodePair to be added into the codeKey array
			codeKey.add(newCode);
			character = codeFile.readChar(); 	// reads the first character of the next line
		}
		
		uncompressedChar = compressFile.readChar(); 	// reads the first character in the uncompressed file
		while (uncompressedChar != (char)0) {				// makes sure the end of the file has not been reached
			codePosition = codeKey.findCharacter(uncompressedChar);
			if (codePosition != -1) {
				charCode = (codeKey.getCode(codePosition)).toCharArray();
				for (int i = 0; i < charCode.length; i++)
					outputFile.writeBit(charCode[i]);
			}
			else {
				System.out.println("The character you tried to compress does not exist");
				break;
			}
			uncompressedChar = compressFile.readChar();
				
			
		}
		
		codeFile.close();
		compressFile.close();
		outputFile.close();
		}
	}

