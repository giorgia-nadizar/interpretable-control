import gymnasium as gym

from continuous.controller import RandomContinuousController

if __name__ == '__main__':
    # TODO make render work
    env = gym.make("Walker2d-v4", render_mode='human')
    controller = RandomContinuousController(env.action_space)
    episode_length = 1000

    observation, info = env.reset(seed=0)
    for _ in range(episode_length):
        action = controller.control(observation)
        observation, reward, terminated, truncated, info = env.step(action)
        env.render()

        if terminated or truncated:
            observation, info = env.reset()

    env.close()
