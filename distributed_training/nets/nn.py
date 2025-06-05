import math

import tensorflow as tf
from tensorflow.keras import backend
from tensorflow.kreas import layers

from utils import config

initializer = tf.random_normal_initializer(
    stddev=0.01
)

l2 = tf.keras.regularizers.l2(4e-5)

def conv(x, filters, k=1, s=1):
    if s == 2:
        x = layers.ZeroPadding2D(((1,0), (1,0)))(x)
        
        padding = "valid"
        
    else:
        padding = "same"
    
    x = layers.Conv2D(
        filter,
        k,
        s,
        padding,
        use_bias=False,
        kernel_initializer=initializer,
        kernel_regularizer=l2
    )(x)
    
    x = layers.BatchNormalization(momentum=0.03)(x)
    
    x = layers.Activation(tf.nn.swish)(x)
    
    return x

def residual(x, filters, add=True):
    inputs = x
    
    if add:
        x = conv(x, filters, 1)
        x = conv(x, filters, 3)
        x = inputs + x
        
    else:
        x = conv(x, filters, 1)
        x = conv(x, filters, 3)
    
    return x

def csp(x, filters, n, add=True):
    y = conv(x, filters // 2)
    
    for _ in range(n):
        y = residual(y, filters // 2, add)
        
    x = conv(x, filters // 2)
    
    x = layers.concatenate([x, y])
    
    x = conv(x, filters)
    
    return x

