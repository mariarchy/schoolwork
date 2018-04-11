import java.util.Iterator;

public class HuffmanTree extends LinkedBinaryTree<HuffmanPair> implements Comparable<HuffmanTree> {
	
	private HuffmanTree newTree;
	/** 
	 * Creates an empty Huffman tree
	 */
	public HuffmanTree() {
		super();
	}
	
	/** 
	 * Creates a Huffman tree with one Huffman pair at the root
	 * @param element the element to be placed as the root
	 */
	public HuffmanTree(HuffmanPair element) {
		super(element);
	}
	
	/** 
	 * Creates a Huffman tree rooted at a node containing element, where the roots of the left subtree 
	 * and right subtree are its left child and right child, respectively
	 * @param element the element to be placed as the root
	 * @param leftSubtree the element to be placed as the left child
	 * @param rightSubtree the element to be placed as the right child
	 */
	public HuffmanTree(HuffmanPair element, HuffmanTree leftSubtree, HuffmanTree rightSubtree) {
		super(element);
		(getRoot()).setLeft((leftSubtree.getRoot()));
		(getRoot()).setRight((rightSubtree.getRoot()));
	}
	
	/** 
	 * Builds a Huffman tree using pairsList 
	 * @param pairsList an ordered list of Huffman pairs in ascending order by frequency
	 */
	public HuffmanTree(ArrayOrderedList<HuffmanPair> pairsList) {
		super();
		ArrayOrderedList<HuffmanTree> buildList = new ArrayOrderedList();
		for (int i=0; i < pairsList.size(); i++) {
			buildList.add(new HuffmanTree((HuffmanPair) pairsList.getElement(i)));			// trees with just a root, to get freq just get root and then get fre
			
		}

			
		while (buildList.size() > 1) {
			HuffmanTree element1 = buildList.removeFirst();
			HuffmanTree element2 = buildList.removeFirst();				
			int rootFreq = ((element1.getRoot()).getElement()).getFrequency() + ((element2.getRoot()).getElement()).getFrequency(); 

			HuffmanPair rootP = new HuffmanPair(rootFreq);
			HuffmanTree newTree = new HuffmanTree(rootP, element1, element2);

			buildList.add(newTree);
		}
		this.setRoot(buildList.first().getRoot());

		}
		

	/**
	 * Compares the frequencies in the root node of the trees
	 * @param otherTree the tree that is to be compared with this tree
	 * @return the differences between the frequencies
	 */
	public int compareTo(HuffmanTree otherTree) {

		return this.getRoot().getElement().getFrequency() - otherTree.getRoot().getElement().getFrequency();
		}
	
	/**
	 * returns a string representation of the Huffman tree object
	 * @return string representation of the Huffman tree object using a preorder traversal  
	 */
	public String toString() {
		String stringRep = "";
		Iterator<HuffmanPair> list ;
		
		list = iteratorPreOrder();
		while (list.hasNext()) {
			stringRep += list.next().toString();
		}

		return stringRep;
		
	}
}
