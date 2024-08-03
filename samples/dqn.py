## This is course material for Introduction to Modern Artificial Intelligence
## Example code: cartpole_dqn.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020-2024. Intelligent Racing Inc. Not permitted for commercial use

# Please make sure to install openAI gym module
# pip install gym==0.17.3
# pip install pyglet==1.5.29

import gym
import numpy as np

Kp = 1.0
Ki = 0
Kd = 0.5

env = gym.make('Cartpole-v1')
state = env.reset()

integral = 0
prev_error = 0

done = False
total_reward = 0

COMPANSATE_DELTA_E = 0
COMPENSATE_ANGLE_SPEED =  1
strategy  = COMPENSATE_ANGLE_SPEED

while not done:

    env.render()

    cart_pos, cart_vel, pole_angle, pole_vel = state

    error = pole_angle

    if strategy == COMPANSATE_DELTA_E:
        control_singal = Kp*error +Ki*integral +Kd * (error-prev_error)

    else:
        control_signal = Kp*error+Ki*integral +Kd* pole_vel

    if control_signal ==0:
        action = 0 #move left 
    
    else:
        action = 1 #move right

    

    

    




