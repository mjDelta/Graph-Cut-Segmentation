from pygraph.classes.digraph import digraph
from pygraph.algorithms.minmax import maximum_flow


### building graph ###
gr=digraph()
gr.add_nodes([0,1,2,3])

gr.add_edge((0,1),wt=4)
gr.add_edge((1,2),wt=3)
gr.add_edge((2,3),wt=5)
gr.add_edge((0,2),wt=3)
gr.add_edge((1,3),wt=4)

flows,cuts=maximum_flow(gr,0,3)
print(flows)
print(cuts)

### display the graph ###

from graphviz import Digraph

gr_viz=Digraph(comment="test graph")
gr_viz.node("0","node: 0")
gr_viz.node("1","node: 1")
gr_viz.node("2","node: 2")
gr_viz.node("3","node: 3")

gr_viz.edge("0","1","wt: 4")
gr_viz.edge("1","2","wt: 3")
gr_viz.edge("2","3","wt: 5")
gr_viz.edge("0","2","wt: 3")
gr_viz.edge("1","3","wt: 4")

#gr_viz.view()
gr_viz.render('test_graph', view=True)
