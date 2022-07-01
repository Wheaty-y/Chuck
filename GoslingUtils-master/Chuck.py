from tools import  *
from objects import *
from routines import *


#This file is for strategy

class Chuck(GoslingAgent):
    def run(agent):
        large_boost = [boost for boost in agent.boosts if boost.large and boost.active]
        closest_boost = large_boost[0]
        closest_dist = (large_boost[0].location - agent.me.location).magnitude()
        #car_speed = agent.me.local(agent.me.velocity)[0]
        # close = (agent.me.location - agent.ball.location).magnitude() < 2000
        have_boost = agent.me.boost > 20
        # my_goal_to_ball = (agent.ball.location - agent.friend_goal.location).normalize()
        # goal_to_me = agent.me.location - agent.friend_goal.location
        # me_offside = abs(agent.friend_goal.location.y - agent.me.location.y) - 200 > abs(agent.friend_goal.location.y - agent.ball.location.y)
        # foe_offside = abs(agent.foe_goal.location.y - agent.foes[0].location.y) - 200 > abs(agent.foe_goal.location.y - agent.ball.location.y)
        

        if agent.team == 0:
            agent.debug_stack() #Displays current routine in action (team 0 is blue)
            # print(me_offside)

        for i in large_boost:
            i_dist = (i.location - agent.me.location).magnitude() #Finding distance to closest Large boost
            if i_dist<closest_dist:
                closest_boost = i 
                closest_dist = i_dist

        if len(agent.stack) < 1:
            if agent.kickoff_flag:
                agent.push(kickoff())
            if agent.me.boost > 30:
                agent.push(short_shot(agent.foe_goal.location))
            else:
                agent.push(goto_boost(closest_boost, agent.ball.location))      