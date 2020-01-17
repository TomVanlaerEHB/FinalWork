import numpy as np
import tensorflow as tf
from MANN import MANN


num_joints  = 27
num_styles  = 6
datapath    = './data' 
savepath    = './training'
num_experts = 8
index_gatingIn = [285, 286, 287, 
                  345, 346, 347, 
                  393, 394, 395, 
                  441, 442, 443,
                  84,  85,  86, 87, 88, 89, 90]

def main():
    rng  = np.random.RandomState(23456)
    sess = tf.Session()
    mann = MANN(num_joints,
                num_styles,
                rng,
                sess,
                datapath, savepath,
                num_experts,
                hidden_size = 512,
                hidden_size_gt = 32, 
                index_gating = index_gatingIn,
                batch_size = 32 , epoch = 150, Te = 10, Tmult =2, 
                learning_rate_ini = 0.0001, weightDecay_ini = 0.0025, keep_prob_ini = 0.7)
    
    mann.build_model()
    mann.train()
    
    
if __name__ =='__main__':
    main()