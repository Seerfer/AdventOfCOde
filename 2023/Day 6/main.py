from dataclasses import dataclass


@dataclass
class Race:
    distance_record: int
    time: int


def calculate_distance(button_hold_time: int, time: int) -> int:
    if button_hold_time < 0 or time < 0:
        raise ValueError("Button hold time and race time must be postivie numbers")
    speed = button_hold_time
    remain_race_time = time - button_hold_time
    return speed * remain_race_time


if __name__ == "__main__":
    with open("input", "r") as f:
        times_str, distance_str = f.read().split('\n')

    times = [int(time) for time in times_str.replace('Time:', '').split(' ') if time != '']
    distances = [int(dist) for dist in distance_str.replace('Distance:', '').split(' ') if dist != '']
    races = [Race(distance_record=d, time=t) for t, d in zip(times, distances)]

    wins_possibilities_num = []

    for r in races:
        counter = 0
        times_possible = range(0, r.time)
        for t in times_possible:
            dis = calculate_distance(t, r.time)
            if dis > r.distance_record:
                counter += 1
        wins_possibilities_num.append(counter)
    result1 = 1
    for x in wins_possibilities_num:
        result1 *= x

    print(f"Result for part 1: {result1}")
    time2 = int("".join([str(t) for t in times]))
    distance2 = int("".join(str(d) for d in distances))
    race_part_2 = Race(distance_record=distance2, time=time2)
    print(race_part_2)
    hold_butt_margin = range(0, time2)
    result2 = 0
    for t in hold_butt_margin:
        dis = calculate_distance(t, race_part_2.time)
        if dis > race_part_2.distance_record:
            result2 += 1

    print(f"Result for part 2: {result2}")
