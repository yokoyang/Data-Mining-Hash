# Hash for data mining

标签（空格分隔）： hash

---

## LSHash部分
data_processing.py
对“Traj_1000_SH_UTM”文件中的数据进行栅格化切分，将每个坐标点的栅格标号写入到文件grid_data.csv中。

u_2_gps.py
用来将utm坐标转换为GPS坐标

path_overview.py
用来显示所有路线，X轴latitude，Y轴为Longitude，显示出来效果如下：
![image_1bc2sgulgduo1rntf8m96bvqe9.png-136kB][1]
row_pca_lshash.py
pca_lshash.py
先grid_data.csv中的Tid进行groupby操作，然后对所对应的栅格“Grid”列，进行排序、去重，得到有轨迹点落下的栅格共有44107个栅格，把这44107个栅格作为LSH运算中每条轨迹的属性，得到轨迹-栅格的0./1矩阵。
后面的lshash处理过程，做了2种尝试，一种是先进行了特征选取，然后再通过PCA降维，再通过局部敏感性哈希处理，另外一种是直接对原始的轨迹-栅格的0./1矩阵进行局部敏感性哈希处理。在测试过程中，观察到使用汉明距离得到的结果更好，下面展示的结果均为汉明距离结果。
得到的部分结果如下所示（其余数据在相应的.txt文件中）：

编号——对应颜色

![image_1bc2shuc813ivu241ffj13e019fjm.png-173.9kB][2]

![image_1bc2si1ojlir1agbb0dgsc17tv13.png-177.8kB][3]

![image_1bc2si67oeha12ntsranmo1kq81g.png-176.3kB][4]

对比显示，经过特征选取和PCA降维后，前者的聚类效果明显优于后者。而且Hash Size 取10比较合适。
这里，特征选取的原则是去掉在该特征上，所有路线的方差小于0.001
threshold=0.001

此外，PCA降维为500维。
## KNN部分
Knn_handler.py 为使用KNN的方法，对轨迹数据进行标注。
使用特征选取和PCA降维的方法，得到的部分结果展示如下：（k=1时，即为该线路本身）
调整
threshold=0.002

n_neighbors=5
![image_1bc2sl69b10rb1dt15ol1n97sm62n.png-146.3kB][5]

## 实现的投影可视化工具
to_view.py 定义了一个Class，有2种方法，分别对应画多个聚类结果，和单个类。
LSHash_Result_2.js, add.js 生成相应JS代码
g1.html 谷歌地图显示

## 总结：
对于该数据集，局部敏感性哈希使用汉明距离得到结果相对其他距离函数更好，但是整体效果没有KNN效果好。
因为矩阵的维度在降维之后仍然比较高，所有使用KNN 的ball_tree算法，来解决高维距离描述问题，获得的结果较好。

  [1]: http://static.zybuluo.com/yokoyang/cmie4rg6tpfloahcbx91tpki/image_1bc2sgulgduo1rntf8m96bvqe9.png
  [2]: http://static.zybuluo.com/yokoyang/4mzeeanmteed1g88wajb0qvw/image_1bc2shuc813ivu241ffj13e019fjm.png
  [3]: http://static.zybuluo.com/yokoyang/8lshkquyztzse1app235hln8/image_1bc2si1ojlir1agbb0dgsc17tv13.png
  [4]: http://static.zybuluo.com/yokoyang/85n9900prnzk07ox86nhv2ya/image_1bc2si67oeha12ntsranmo1kq81g.png
  [5]: http://static.zybuluo.com/yokoyang/qulsum0u7jzvfqy9uvv6fit0/image_1bc2sl69b10rb1dt15ol1n97sm62n.png