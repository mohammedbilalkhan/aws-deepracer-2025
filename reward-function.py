import math

def reward_function(params):
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    all_wheels_on_track = params['all_wheels_on_track']
    is_offtrack = params['is_offtrack']
    steps = params['steps']
    progress = params['progress']
    heading = params['heading']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    steering = abs(params['steering_angle'])

    # Fail fast
    if is_offtrack or not all_wheels_on_track:
        return 1e-3

    reward = 1.0

    # Direction alignment reward
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    track_direction = math.degrees(math.atan2(
        next_point[1] - prev_point[1],
        next_point[0] - prev_point[0]
    ))
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    if direction_diff < 10:
        reward += 1.0

    # Speed reward in optimal range (1.5 - 2.0 m/s)
    if 1.0 <= speed <= 3.5:
        reward += 2.0
    elif speed > 1.0:
        reward += 1.0  # allow little leeway
    else:
        reward *= 0.5

    # Light penalty for oversteering
    if steering > 20:
        reward *= 0.7

    # Efficiency bonus every 100 steps
    if steps > 0 and steps % 100 == 0:
        reward += min(progress / steps, 1.0)

    # Completion bonus
    if progress == 100:
        reward += 10.0
        reward += max(0.0, (300 - steps) / 300.0) * 5.0  # Faster = more bonus

    return float(reward)
