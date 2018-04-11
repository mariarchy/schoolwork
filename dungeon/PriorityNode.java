
public class PriorityNode<T> {

	private T dataItem;
	private PriorityNode<T> next;
	private PriorityNode<T> previous;
	private double priority;
	
	/**
	 * Creates a node storing the given data and priority.
	 * @param data the data item to be stored
	 * @param prio the priority of the given data item 
	 */
	public PriorityNode(T data, double prio) {
		dataItem = data;
		priority = prio;
		next = previous = null;
	}
	
	/**
	 * Creates an empty node, with null data and priority zero
	 */
	public PriorityNode() {
		dataItem = null;
		priority = 0;
		next = previous = null; 
	}
	
	/**
	 * returns the priority for a specified
	 * @return the matching priority for a given dataItem
	 */
	public double getPriority() {
		return priority;
	}
	
	/**
	 * returns the dataItem stored in the node
	 * @return the dataItem stored in the node
	 */
	public T getDataItem() {
		return dataItem;
	}
	
	/**
	 * returns the node after the current node
	 * @return the next node stored
	 */
	public PriorityNode<T> getNext() {
		return next;
	}
	
	/**
	 * returns the node before the current node
	 * @return the previous node stored
	 */
	public PriorityNode<T> getPrevious() {
		return previous;
	}
	
	/**
	 * sets the next node
	 * @param nextNode the data to be stored in the next node
	 */
	public void setNext(PriorityNode<T> nextNode) {
		next = nextNode;
	}
	
	/**
	 * sets the previous node
	 * @param prevNode the data to be stored in the next node
	 */
	public void setPrevious(PriorityNode<T> prevNode) {
		previous = prevNode;
	}
	
	/**
	 * sets the dataItem for a node
	 * @param data the data to be stored as dataItem
	 */
	public void setDataItem(T data) {
		dataItem = data;
	}
	
	/**
	 * sets the priority for the dataItem
	 * @param prior the double to be stored with the dataItem
	 */
	public void setPriority(double prior) {
		priority = prior;
	}
}
