for agent in env.agent_iter():
#     observation, reward, termination, truncation, info = env.last(observe=True)

#     if termination or truncation:
#         action = None
#         break
#     else:
#         # this is where you would insert your policy
#         action = env.action_space(agent).sample()

#     env.step(action)
# env.close()