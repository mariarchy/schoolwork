import java.io.FileNotFoundException;
import java.io.IOException;

public class FindShortestPath {
	static Map cityMap;
	/**
	 * reads the input file and displays the map on the screen
	 * @param filename containing the description of the city map, and the initial and destination map cells.
	 * @throws InvalidMapException if map selection is invalid
	 * @throws FileNotFoundException if input file name is invalid
	 * @throws IOException if file cannot be opened
	 */
	public FindShortestPath(String filename) throws InvalidMapException, FileNotFoundException, IOException {
		cityMap = new Map(filename);
	}
	
	/**
	 * runs through the map to find the shortest path to the customer
	 * @throws InvalidMapException if map selection is invalid
	 * @throws FileNotFoundException if input file name is invalid
	 * @throws IOException if file cannot be opened
	 */
	public static void main(String[] args) throws InvalidMapException, FileNotFoundException, IOException {	
		try {
			if (args.length < 1)
				// catches error if there is no input for args
				throw new IllegalArgumentException("Invalid input for map file name. Must be at least one character long.");
			
			FindShortestPath path = new FindShortestPath(args[0]);
	
			DLPriorityQueue<MapCell> priorQueue = new DLPriorityQueue();
			MapCell uwoStore = cityMap.getUWOstore();
			priorQueue.enqueue(uwoStore, 0);
			uwoStore.markEnqueued();
			MapCell currentCell = uwoStore; 
			while (!priorQueue.isEmpty() && !currentCell.isCustomer()) {
				currentCell = priorQueue.getSmallest();
				currentCell.markDequeued();
				if (currentCell.isCustomer()) {
					break;
				}
				// if cell tower, go back to beginning of while loop and start again
				if (path.interference(currentCell) || currentCell.isTower()) {
					continue;
				}
				else {
					for (int i = 0; i < 6; i++) {
						MapCell neighbourCell = currentCell.getNeighbour(i);
						if (neighbourCell != null && !neighbourCell.isNoFlying() && !neighbourCell.isMarkedDequeued()) {
							int distance = 1 + currentCell.getDistanceToStart();
							if (neighbourCell.getDistanceToStart() > distance) {
								neighbourCell.setDistanceToStart(distance);
								neighbourCell.setPredecessor(currentCell);
						double totalDistance = (double) neighbourCell.getDistanceToStart() + neighbourCell.euclideanDistToDest(cityMap);
						if (neighbourCell.isMarkedEnqueued() && totalDistance < priorQueue.getPriority(neighbourCell)) {
							priorQueue.changePriority(neighbourCell, totalDistance);
						}
						
						if (!neighbourCell.isMarkedEnqueued()) {
							priorQueue.enqueue(neighbourCell, totalDistance);
							neighbourCell.markEnqueued();
						}
								
							}
						}
					}
				}
			}
			if (currentCell.isCustomer()) {
				System.out.println("The length of the path was " + Integer.toString(currentCell.getDistanceToStart()));
			}
			else {
				System.out.println("Destination was not reached.");
			}
		}
		catch(IOException e) {			
		System.out.println("Invalid input for map file name.");
		} 
		catch (IllegalArgumentException e) {
			System.out.println("No input file provided");
		}
		catch (InvalidMapException e) {
			System.out.println("Invalid Map");
		}
			
	}
	
	/**
	 * checks if any of the adjacent cells to the current one is a towercell
	 * @param cell the cell to cross-check if any adjacent ones are towercells
	 * @return true if adjacent cell is a towercell
	 */
	private boolean interference(MapCell cell) {
		for (int i = 0; i <= 5; i++)
			if (cell.getNeighbour(i) != null && (cell.getNeighbour(i)).isTower()) {
				return true;
			}
		return false;
	}
}
