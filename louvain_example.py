import networkx as nx
import community as community_louvain  # This is the python-louvain library
import matplotlib.pyplot as plt
import matplotlib.cm as cm # colormap

def get_static_graph():
    """
    Creates and returns a static graph with a known community structure.
    
    This graph has 3 communities of different sizes:
    - Community 0 (Small): 3 nodes [0, 1, 2]
    - Community 1 (Large): 5 nodes [3, 4, 5, 6, 7]
    - Community 2 (Medium): 4 nodes [8, 9, 10, 11]
    """
    G = nx.Graph()
    
    # Community 0 (Small: 3 nodes)
    G.add_edges_from([(0, 1), (1, 2), (0, 2)])
    
    # Community 1 (Large: 5 nodes) - A densely connected group
    G.add_edges_from([(3, 4), (3, 5), (3, 6), (3, 7),
                      (4, 5), (4, 6), (4, 7),
                      (5, 6), (5, 7),
                      (6, 7)])
                      
    # Community 2 (Medium: 4 nodes) - A clique
    G.add_edges_from([(8, 9), (8, 10), (8, 11),
                      (9, 10), (9, 11),
                      (10, 11)])
                      
    # Bridges between communities
    G.add_edge(2, 3) # Connects Comm 0 and Comm 1
    G.add_edge(7, 8) # Connects Comm 1 and Comm 2
    
    print("--- Static graph created ---")
    return G

def run_louvain_static_example():
    """
    Gets a static graph, runs the Louvain algorithm,
    finds the largest community, and visualizes the result.
    """
    
    # 1. Get static graph
    G = get_static_graph()

    print(f"\nGraph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
    print("Running Louvain algorithm to find best partition...")

    # 2. Run the Louvain algorithm
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
    
    # 3. Print the results and find the largest community
    communities = {}
    for node, community_id in partition.items():
        if community_id not in communities:
            communities[community_id] = []
        communities[community_id].append(node)

    largest_community_id = -1
    max_size = -1
        
    for i, nodes in sorted(communities.items()):
        # Sort nodes for cleaner output
        try:
            sorted_nodes = sorted(nodes, key=lambda x: int(x))
        except ValueError:
            sorted_nodes = sorted(nodes)
            
        print(f"  Community {i}: {sorted_nodes} (Size: {len(nodes)})")
        
        # Check if this is the largest community
        if len(nodes) > max_size:
            max_size = len(nodes)
            largest_community_id = i

    # 4. Print the analysis of the largest community
    print("\n--- Analysis ---")
    largest_nodes = communities[largest_community_id]
    try:
        sorted_largest_nodes = sorted(largest_nodes, key=lambda x: int(x))
    except ValueError:
        sorted_largest_nodes = sorted(largest_nodes)
        
    print(f"The largest community is Community {largest_community_id} with {max_size} nodes.")
    print(f"Nodes: {sorted_largest_nodes}")
        
    modularity = community_louvain.modularity(partition, G)
    print(f"\nFinal Modularity Score: {modularity:.4f}")

    # 5. Visualize the graph
    print("\nGenerating visualization (this may take a moment)...")
    
    # Get a color map
    unique_communities = set(partition.values())
    cmap = cm.get_cmap('viridis', max(unique_communities) + 1)
    colors = [cmap(partition[node]) for node in G.nodes()]

    # Use a spring layout
    pos = nx.spring_layout(G, seed=42) # Seed for reproducible layout

    # Create the plot
    plt.figure(figsize=(12, 8))
    nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=600, alpha=0.9)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
    
    plt.title("Louvain Community Detection on Static Graph", fontsize=16)
    plt.axis('off') # Hide the axes
    
    # Save the plot to a file
    output_filename = f"louvain_static_graph_visualization.png"
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
    run_louvain_static_example()