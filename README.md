# Graph-Cut-Segmentation
This repo is about graph-cut applied in sementaic segmentation task of computer vision fileds. It containes two parts: first, an simple example of graph-cut in a 4-nodes-5-edges graph; second, graph-cut in image segmentation.

### Graph Cut 
* Aims: Cut a directed graph into two sets.</br>
* Loss: Minimize the sum of the cutted edges.</br>
![loss](https://github.com/mjDelta/Graph-Cut-Segmentation/blob/master/imgs/loss.png)</br>
* Basic Idea: Pixels with similar color vector and locations should be put into a same area.</br>

### Simple Graph Cut
Here is the example graph with 4 nodes and 5 edges. Our task is to segment these nodes into two parts with less loss.</br>
![graph](https://github.com/mjDelta/Graph-Cut-Segmentation/blob/master/imgs/graph.png)</br>

### Graph Cut in image segmentation
The keypoint of applying Graph-Cut in Image Segmentation task is building the edges weights among the nodes. And we can compute edges weights by the following equations.```P is probability of pixel i belonging to foreground or background. ```</br>
![graph](https://github.com/mjDelta/Graph-Cut-Segmentation/blob/master/imgs/wsi.png)</br>
![graph](https://github.com/mjDelta/Graph-Cut-Segmentation/blob/master/imgs/wit.png)</br>
![graph](https://github.com/mjDelta/Graph-Cut-Segmentation/blob/master/imgs/wij.png)</br>
