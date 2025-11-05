Python Louvain Community Detection

This project provides a simple, interactive Python script to detect communities in a graph using the Louvain algorithm.

You can build a graph by entering connections (edges) directly into the terminal. The script will then process the graph, identify distinct communities, and generate a visual representation of the results.

Description

The script uses the networkx library to build the graph and the python-louvain library to perform the community detection. The Louvain algorithm is a fast and efficient method for finding communities in large networks by optimizing a "modularity" score.

The script will:

Prompt you to enter graph edges one by one.

Stop when you type done.

Run the Louvain best_partition function to find communities.

Print the detected communities and the final modularity score to the terminal.

Generate and save a louvain_user_graph_visualization.png image, coloring each node based on its community.

Requirements

Python 3.x

networkx

python-louvain

matplotlib

Setup & Installation

It is highly recommended to use a Python virtual environment to manage dependencies and avoid library conflicts.

Clone the repository (or just download louvain_example.py)

Create a Virtual Environment:
In your project folder, run:

python3 -m venv venv


(On Windows, you might use python -m venv venv)

Activate the Environment:

On macOS/Linux:

source venv/bin/activate


On Windows (Command Prompt):

.\venv\Scripts\activate


Install Required Libraries:
With your virtual environment active, run:

pip install networkx python-louvain matplotlib


How to Run

Make sure your virtual environment is active.

Run the script from your terminal:

python louvain_example.py


Follow the prompts:
Enter edges as pairs of nodes (e.g., A B or 0 1).

--- Create Your Graph ---
Enter edges one by one (e.g., '0 1' or 'nodeA nodeB').
Type 'done' when you are finished.
Enter edge (or 'done'): 0 1
Added edge: (0, 1). Graph now has 2 nodes and 1 edges.
Enter edge (or 'done'): 1 2
Added edge: (1, 2). Graph now has 3 nodes and 2 edges.
Enter edge (or 'done'): 0 2
Added edge: (0, 2). Graph now has 3 nodes and 3 edges.
Enter edge (or 'done'): done
--- Graph creation complete ---


Example Output

After you type done, the script will process the graph and output the results.

Terminal Output:

Graph created with 3 nodes and 3 edges.
Running Louvain algorithm to find best partition...
Algorithm complete. Detected communities:
  Community 0: ['0', '1', '2']

Final Modularity Score: 0.0000

Generating visualization (this may take a moment)...
Visualization saved to 'louvain_user_graph_visualization.png'


Image Output:
A file named louvain_user_graph_visualization.png will be saved in the same directory, showing your graph with the communities colored.
