
public class DLPriorityQueue<T> implements PriorityQueueADT<T> {
	
	private PriorityNode<T>  front, rear;
	private int count;
	
	/**
	 * Creates an empty priority queue
	 */
	public DLPriorityQueue() {
		count = 0;
		// is this right
		front = rear = null;
	}
	
	/**
	 * Adds to the priority queue the given dataItem with its associated priority
	 * 
	 * @param dataItem data for the node that is to be stored in the queue
	 * @param priority priority for the node that is to be stored in the queue           
	 */
	public void enqueue(T dataItem, double priority) {
		PriorityNode<T> newNode = new PriorityNode(dataItem, priority);
		if (isEmpty()) {
			newNode.setPrevious(null);
			// don't need to set because already null
			front = newNode;
		}
		else {
			rear.setNext(newNode);
		}
		newNode.setPrevious(rear);
		rear = newNode;
		newNode.setNext(null);
		count ++;
	}
	/**
	 * Removes and returns the data item at the front of the priority queue
	 * 
	 * @return data item removed from the front of the priority queue
	 * @throws EmptyPriorityQueueException if priority queue is empty
	 */
	public T dequeue() throws EmptyPriorityQueueException {
		if (isEmpty()) {
			throw new EmptyPriorityQueueException("Error: cannot dequeue from an empty queue");
		}
		T result = front.getDataItem();		// gets data item from first node
		(front.getNext()).setPrevious(null);
		front = front.getNext();			// sets front as the next node
		count --;						// reduces count by 1
		if (isEmpty()) {					// sets rear and front as null if the queue is empty after removing the first node
			rear = front;
		}
		return result;
	}
	
	/**
	 * Returns the priority of the specified dataItem
	 * 
	 * @param dataItem
	 * @return priority of the specified dataItem
	 * @throws InvalidDataItemException if the given dataItem is not in the priority queue
	 */
	public double getPriority(T dataItem) throws InvalidDataItemException {
		PriorityNode<T> current = front;
		while (current != null) {
			if ((current.getDataItem()).equals(dataItem)) {
				return current.getPriority();
			}
			current = current.getNext();
			}
		throw new InvalidDataItemException("Error");
	}

	/**
	 * Removes and returns the element from the priority queue with smallest priority
	 * 
	 * @return T smallest priority element removed from the priority queue
	 */
	public T getSmallest() throws EmptyPriorityQueueException {
		if (isEmpty()) {
			throw new EmptyPriorityQueueException("Error: cannot get smallest from an empty queue");
		}
		PriorityNode<T> current = front;
		PriorityNode<T> smallest = current;
		while (current != null) {
//			System.out.println(current.getPriority());
//			System.out.println(current.getPriority() < smallestPriority);
			if (current.getPriority() < smallest.getPriority())
				smallest = current;
			current = current.getNext();
		}
		count --;
		if (smallest.equals(rear)) {
			if (isEmpty()) {
				front = rear = null;
			}
			else {
				rear = smallest.getPrevious();	// sets rear as the previous node if the smallest to be removed is the last node
				rear.setNext(null);
			}
			
		}
		else if (smallest.equals(front)) {
			front = smallest.getNext();		// sets front as the next node if the smallest to be removed is the first node
			front.setPrevious(null);
		}
	
		else {
		(smallest.getNext()).setPrevious(smallest.getPrevious());
		(smallest.getPrevious()).setNext(smallest.getNext());
		}
		return smallest.getDataItem();
	}

	/**
	 * Updates the priority of the given element to the new value
	 * 
	 * @param element
	 *            whose priority is to be changed
	 * @param newPriority
	 *            value of the new priority for this element
	 * @throws InvalidDataException if the given dataItem is not in the priority queue
	 */
	public void changePriority(T element, double newPriority) throws InvalidDataItemException {
		boolean found = false;
		PriorityNode<T> current = front;
		while (current != null && !found) {
			if ((current.getDataItem()).equals(element)) {
				current.setPriority(newPriority);
				found = true;
			}
			current = current.getNext();
		}
		if (!found) {
			throw new InvalidDataItemException("Error");
		}
	}

	/**
	 * Returns true if this priority queue contains no elements.
	 * 
	 * @return boolean whether or not this priority queue is empty
	 */
	public boolean isEmpty() {
		if (count == 0) {
			return true;
		}
		return false;
	}
		
	/**
	 * Returns the number of elements in this priority queue.
	 * 
	 * @return int number of elements in this priority queue
	 */
	public int numItems() {
		return count;
	}

	/**
	 * Returns a string representation of this priority queue.
	 * 
	 * @return String representation of this priority queue
	 */
	public String toString() {
		String resultString = "";
		PriorityNode<T> current = front;
		while (current != null) {
			resultString += current.getDataItem();
			current = current.getNext();
		}
		return resultString;
	}
}