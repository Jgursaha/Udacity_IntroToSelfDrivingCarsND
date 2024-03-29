#include "headers/initialize_beliefs.h"

using namespace std;

// OPTIMIZATION: pass large variables by reference
vector< vector <float> > initialize_beliefs(vector< vector <char> > grid) {

	// OPTIMIZATION: Which of these variables are necessary?
	// OPTIMIZATION: Reserve space in memory for vectors
	int height, width;
	float prob_per_cell;

	height = grid.size();
	width = grid[0].size();
  
	//area = height * width;

  	prob_per_cell = 1.0 / ( (float) (height * width) );
  
  	vector<float> newRow(width,prob_per_cell);
  	vector< vector <float> > newGrid(height, newRow);

  	// OPTIMIZATION: Is there a way to get the same results 	// without nested for loops?
	//for (i=0; i<grid.size(); i++) {
	//	newRow.clear();
	//	for (j=0; j<grid[0].size(); j++) {
	//		newRow.push_back(prob_per_cell);
	//	}
	//	newGrid.push_back(newRow);
	//}
	return newGrid;
}