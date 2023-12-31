import math


def find_angle_mbc(ab: float, bc: float):
    theta = math.degrees(math.atan(ab / bc))
    rounded_theta = math.floor(theta + 0.5)  # round it to the nearest integer

    return rounded_theta


if __name__ == '__main__':
    theta = find_angle_mbc(3, 4)
    print(theta)