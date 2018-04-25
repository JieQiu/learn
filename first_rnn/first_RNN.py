#This code is a copy from this link:
#https://morvanzhou.github.io/tutorials/machine-learning/tensorflow/5-08-RNN2/
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

tf.set_random_seed(1)#rum the program twice，use it to compare the two result
#data
mnist=input_data.read_data_sets('Mnist_data',one_hot=True)

#hyperparameters
lr=0.01
training_iters=10000
batch_size=128

n_inputs=28
n_steps=28#(img shape: 28*28)
n_inputw=100
n_hidden_units=128
n_classes=10

#tf graph input
x=tf.placeholder(tf.float32,[None,n_steps,n_inputs])#此函数可以理解为形参，用于定义过程，在执行的时候再赋具体的值
y=tf.placeholder(tf.float32,[None,n_classes])

#define weights
weights={'in':tf.Variable(tf.random_normal([n_inputs,n_inputw])),#[28,128],也可以不是n_hidden_units
         'out':tf.Variable(tf.random_normal([n_hidden_units,n_classes]))}
biases={'in':tf.Variable(tf.constant(0.1,shape=[n_inputw,])),#表明'in'是一维向量
        'out':tf.Variable(tf.constant(0.1,shape=[n_classes,]))}

def RNN(X,weights,biases):
    # X ==> (128 batch * 28 steps, 28 inputs)
    X=tf.reshape(X,[-1,n_inputs])
    #into first hidden
    #X_in=(128batch*28steps,100)
    X_in=tf.matmul(X,weights['in'])+biases['in']
    X_in=tf.reshape(X_in,[-1,n_steps,n_inputw])
#####cell
    cell=tf.nn.rnn_cell.BasicLSTMCell(n_hidden_units,forget_bias=1.0,state_is_tuple=True)#forget_bias=1.0不要忘记，
    # state_is_tuple=True，生成的（c_state，h_state）是这种分开的元组类型，而不是两者连接成一个向量，对照公式里面的c，h
    init_state=cell.zero_state(batch_size,dtype=tf.float32)#每个批次都要存初始状态，整个init_state shape=[batch_size,n_hidden_units]
    #关于n_inputw和n_hidden_units不同，因为X_in要经过tf.nn.dynamic_rnn这个模块，里面是先对X_in都会对应乘以一个W矩阵，转换成合适尺寸，再进行操作的。
    #进入rnn
    outputs,final_state=tf.nn.dynamic_rnn(cell,X_in,initial_state=init_state,time_major=False)
    outputs=tf.unstack(tf.transpose(outputs,[1,0,2]))#outputs shape=[batch_size,n_steps,n_hidden_units]->第一维度第二维度交换
    #取时间步最后一步的结果,输出为10类
    results=tf.matmul(outputs[-1],weights['out'])+biases['out']
    return  results#shape=[128,10]

pred=RNN(x,weights,biases)
cost=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred,labels=y))#logits(神经网络最后一层输出),labels维度相同，有batch时候是[batch_size,num_classes]
####train
train_op=tf.train.AdamOptimizer(lr).minimize(cost)
####accuracy tf.argmax(input, dimension, name=None) Returns the index!!! with the largest value across dimensions of a tensor
correct_pred=tf.equal(tf.arg_max(pred,1),tf.arg_max(y,1))#tf.equal:相同的true，不同返回false[[ True  True  True False False]] size（pred）=[128,1]
accuracy=tf.reduce_mean(tf.cast(correct_pred,tf.float32))

with tf.Session() as sess:
    init=tf.initialize_all_variables()
    ####初始化
    sess.run(init)
    step=0
    while step*batch_size<training_iters:
        batch_xs,batch_ys=mnist.train.next_batch(batch_size)
        batch_xs=batch_xs.reshape(batch_size,n_steps,n_inputs)
        sess.run([train_op],feed_dict={x:batch_xs,y:batch_ys})
        if step%20==0:
            print(sess.run(accuracy,feed_dict={x:batch_xs,y:batch_ys}))
        step+=1




