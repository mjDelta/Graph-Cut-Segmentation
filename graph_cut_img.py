from pygraph.classes.digraph import digraph
from pygraph.algorithms.minmax import maximum_flow

from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import numpy as np
from scipy.misc import imread,imresize

import matplotlib.pyplot as plt

def get_graph_based_bayes(img,labels,sigma=1e2,kappa=2):
  print(kappa)
  foreground=img[labels==1].reshape((-1,3))
  background=img[labels==-1].reshape((-1,3))
  train_x=np.concatenate((foreground,background))
  temp_y1=np.zeros((len(foreground)))
  temp_y2=np.ones((len(background)))
  train_y=np.concatenate((temp_y1,temp_y2))

#  clf=SVC(probability=True).fit(train_x,train_y)
  clf=GaussianNB().fit(train_x,train_y)
  
  all_x=img.reshape((-1,3))
  preds=clf.predict_proba(all_x)
  
  bg_probs=preds[:,0]
  fg_probs=preds[:,1]
  
  ### build bayes graph ###
  h,w,c=img.shape
  gr=digraph()
  
  gr.add_nodes(range(h*w+2))## add node source and node target
  source=h*w
  target=h*w+1
  
  ### normalization ###
  for i in range(all_x.shape[0]):
    all_x[i]=all_x[i]/np.linalg.norm(all_x[i])

  for i in range(h*w):
    ### add edges from source ###
    gr.add_edge((source,i),wt=fg_probs[i]/(fg_probs[i]+bg_probs[i]))
    
    ### add edges to target ###
    gr.add_edge((i,target),wt=bg_probs[i]/(fg_probs[i]+bg_probs[i]))
    
    ### add edges of 4-neighbors ###
    ## 1.judge whether has upper pixel
    if i//w!=0:
      weight=kappa*np.exp(-1.*np.sum((all_x[i]-all_x[i-w])**2)/sigma)
      gr.add_edge((i,i-w),wt=weight)
    ## 2.judge whether has lower pixel
    if i//w!=h-1:
      weight=kappa*np.exp(-1.*np.sum((all_x[i]-all_x[i+w])**2)/sigma)
      gr.add_edge((i,i+w),wt=weight)    
    ## 3.judge whether has left pixel
    if i%w!=0:
      weight=kappa*np.exp(-1.*np.sum((all_x[i]-all_x[i-1])**2)/sigma)
      gr.add_edge((i,i-1),wt=weight)   
    ## 4.judge whether has right pixel
    if i%w!=w-1:
      weight=kappa*np.exp(-1.*np.sum((all_x[i]-all_x[i+1])**2)/sigma)
      gr.add_edge((i,i+1),wt=weight)  
      
  return gr

def cut_graph(graph,height,width):
  source=width*height
  target=width*height+1
  flows,cuts=maximum_flow(graph,source,target)
  
  result=np.zeros((height*width))
  for loc,label in list(cuts.items())[:-2]:
    result[loc]=label
    
  return result.reshape((height,width))

if __name__=="__main__":
  img_name="empire.png"

  img=imread(img_name)
  rescale=0.5
  img=imresize(img,rescale,interp="bilinear")
  plt.imshow(img)
  plt.show()
  
  labels=np.zeros(img.shape)
#  labels=img.copy()
  labels[-int(rescale*70):-int(rescale*10),-int(rescale*70):-int(rescale*10),:]=1
  labels[int(rescale*10):int(rescale*70),int(rescale*10):int(rescale*70),:]=-1
#  plt.imshow(labels)
#  plt.show()

  graph=get_graph_based_bayes(img,labels,sigma=100,kappa=1)
  result=cut_graph(graph,img.shape[0],img.shape[1])
  plt.imshow(result,cmap=plt.get_cmap("gray"))
  plt.show()  
  
