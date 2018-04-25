# learn
#This code is a tiny modified version from this link:
#https://morvanzhou.github.io/tutorials/machine-learning/tensorflow/5-08-RNN2/
Mnist手写数据x分类任务：第一层wx+b=x_in,第二层rnn，第三层wx+b=x_out十类（0-9）
#搞懂了一个问题，关于x的维度可以不用和n_hidden_units相同。n_inputw和n_hidden_units可以不同，因为X_in要经过tf.nn.dynamic_rnn这个模块，里面是先对X_in都会对应乘以一个W矩阵，转换成合适尺寸，再进行操作的。