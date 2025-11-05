import networkx as nx
import community as community_louvain  # This is the python-louvain library
import matplotlib.pyplot as plt
import matplotlib.cm as cm # colormap

def get_user_graph():
    """
    Prompts the user to enter edges to build a graph.
    Returns the user-defined NetworkX graph.
    """
    print("--- Create Your Graph ---")
    print("Enter edges one by one (e.g., '0 1' or 'nodeA nodeB').")
    print("Type 'done' when you are finished.")
    
    G = nx.Graph()
    
    while True:
        # Get raw input
        user_input_raw = input("Enter edge (or 'done'): ")
        
        # --- FIX ---
        # Strip whitespace and common quote characters (' and ")
        # from the beginning and end of the raw input.
        user_input = user_input_raw.strip().strip("'\"")
        
        if user_input.lower() == 'done':
            if G.number_of_nodes() == 0:
                print("No graph created. Exiting.")
                return None
            print("--- Graph creation complete ---")
            break
            
        # Try to parse the input
        # Replace commas just in case, then split by whitespace
        nodes = user_input.replace(',', ' ').split()
        
        if len(nodes) == 2:
            u, v = nodes[0], nodes[1]
            G.add_edge(u, v)
            print(f"Added edge: ({u}, {v}). Graph now has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
        else:
            print(f"  Invalid input: '{user_input_raw}'. Please enter two node names separated by a space (e.g., 'A B').")
            
    return G

def run_louvain_on_user_graph():
    """
    Gets a graph from user input, runs the Louvain algorithm,
    and visualizes the result.
    """
    
    # 1. Get graph from user
    G = get_user_graph()
    
    if G is None:
        return

    print(f"\nGraph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
    print("Running Louvain algorithm to find best partition...")

    # 2. Run the Louvain algorithm
    # This function computes the best partition of the graph
    # It returns a dictionary where keys are nodes and values are the community ID
    try:
        partition = community_louvain.best_partition(G)
    except AttributeError:
        print("\n--- ERROR ---")
        print("AttributeError: 'community' module has no 'best_partition'.")
        print("This usually means you installed the wrong library.")
        print("Please stop this script and run the following commands in your terminal:")
        print("1. pip uninstall community networkx-community")
        print("2. pip install python-louvain")
        print("-------------\n")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    
    print("Algorithm complete. Detected communities:")
    
    # 3. Print the results
    # We can group the nodes by their community ID
    communities = {}
    for node, community_id in partition.items():
        if community_id not in communities:
            communities[community_id] = []
        communities[community_id].append(node)

    for i, nodes in sorted(communities.items()):
        # Sort nodes within the community for cleaner output
        # We sort them numerically if they are digits, otherwise alphabetically
        try:
            sorted_nodes = sorted(nodes, key=lambda x: int(x))
        except ValueError:
            sorted_nodes = sorted(nodes)
        print(f"  Community {i}: {sorted_nodes}")
        
    modularity = community_louvain.modularity(partition, G)
    print(f"\nFinal Modularity Score: {modularity:.4f}")

    # 4. Visualize the graph
    print("\nGenerating visualization (this may take a moment)...")
    
    # Get a color map
    # We'll map each unique community ID to a distinct color
    unique_communities = set(partition.values())
    cmap = cm.get_cmap('viridis', max(unique_communities) + 1)
    colors = [cmap(partition[node]) for node in G.nodes()]

    # Use a spring layout to position nodes
    # This layout algorithm tries to position nodes so connected nodes are
    # closer, making communities visually distinct.
    pos = nx.spring_layout(G, seed=42) # Seed for reproducible layout

    # Create the plot
    plt.figure(figsize=(12, 8))
    nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=600, alpha=0.9)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
    
    plt.title("Louvain Community Detection on User-Input Graph", fontsize=16)
    plt.axis('off') # Hide the axes
    
    # Save the plot to a file
    output_filename = f"louvain_user_graph_visualization.png"
    plt.savefig(output_filename)
    print(f"Visualization saved to '{output_filename}'")
    
    # Show the plot
    try:
        plt.show()
    except Exception as e:
        print(f"\nCould not display plot interactively ({e}).")
        print(f"Please check the saved file: {output_filename}")

# Run the example
if __name__ == "__main__":
    run_louvain_on_user_graph()
