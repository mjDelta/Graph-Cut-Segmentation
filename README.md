# Graph-Cut-Segmentation
This repo is about graph-cut applied in sementaic segmentation task of computer vision fileds. It containes two parts: first, an simple example of graph-cut in a 4-nodes-5-edges graph; second, graph-cut in image segmentation.

### Graph Cut 
* Aims: Cut a directed graph into two sets， minmize the sum of the cutted edges.</br>

<img src="http://chart.googleapis.com/chart?cht=tx&chl=E_{cut}=\sum_{i,j\in C} w_{ij}" style="border:none;">

* Basic Idea: Pixels with similar color vector and locations should be put into a same area.</br>
