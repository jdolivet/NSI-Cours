import ast
import uuid
from graphviz import Digraph
 
  
def ast_graph(expression):
    graph = Digraph(format='png')
    code = ast.parse(expression)
 
    # création des noeuds
    for node in ast.walk(code):
        label = node.__class__.__name__
        if label not in ["Store", "Load", "Module"]:
            print(label)
            if label == "Num":
                label += "\n n = " + str(node.n)
            elif label in ["Add", "Sub", "Mult", "Div", "Mod", "Pow"]:
                label += "()"
            graph.node(str(id(node)), label)
    
    # création des liens
    for node in ast.walk(code):
        if node.__class__.__name__ == "Name":
            node_id = str(id(node))
            child1_id = str(uuid.uuid4())
            graph.node(child1_id, node.id)
            graph.edge(node_id, child1_id, label="id")
            child2_id = str(uuid.uuid4())
            graph.node(child2_id, node.ctx.__class__.__name__ + "()")
            graph.edge(node_id, child2_id, label="ctx")
        elif node.__class__.__name__ == "Module":
            pass
        else:
            for child, field in zip(ast.iter_child_nodes(node), ast.iter_fields(node)):
                graph.edge(str(id(node)), str(id(child)), label=str(field[0]))
    return graph


expression = 'i = 3\nwhile i > O:\n    print("prends garde à toi !")\n    i = i - 1\nprint(1 / i)\nprint("Carmen épouse-moi !")'
g = ast_graph(expression)
g.render("arbre_de_syntaxe", view=True)