import re

ids = []
part_1_answer = 0

part_2_ids = {}
part_2_answer = 0

# 12 Red, 13 Green, 14 Blue

def part1(part_1_answer):
	with open("day2list.txt", "r") as day_2_list:
		for line in day_2_list:
			broken = False
			match = re.search("(\d+):", line)
			if match:
				red_matches = re.findall("(\d+) ?red", line)
				if not broken:
					if red_matches:
						for red_match in red_matches:
							if int(red_match) > 12:
								broken = True
								break
					green_matches = re.findall("(\d+) ?green", line)
					if green_matches:
						for green_match in green_matches:
							if int(green_match) > 13:
								broken = True
								break
					blue_matches = re.findall("(\d+) ?blue", line)
					if blue_matches:
						for blue_match in blue_matches:
							if int(blue_match) > 14:
								broken = True
								break
				if not broken:
					ids.append(match.group(1))
				else:
					continue

		for game_id in ids:
			part_1_answer += int(game_id)

		print(part_1_answer)

part1(part_1_answer)


def part2(part_2_answer):
	with open("day2list.txt", "r") as day_2_list:
		for line in day_2_list:
			game_id = re.search("(\d+):", line)
			if game_id:
				part_2_ids[f"{game_id.group(1)}"] = []

				red_matches = re.findall("(\d+) ?red", line)
				reds = [int(i) for i in red_matches]
				reds.sort(reverse=True)
				part_2_ids[f"{game_id.group(1)}"].append(reds[0])

				green_matches = re.findall("(\d+) ?green", line)
				greens = [int(i) for i in green_matches]
				greens.sort(reverse=True)
				part_2_ids[f"{game_id.group(1)}"].append(greens[0])

				blue_matches = re.findall("(\d+) ?blue", line)
				blues = [int(i) for i in blue_matches]
				blues.sort(reverse=True)
				part_2_ids[f"{game_id.group(1)}"].append(blues[0])

		for key, values in part_2_ids.items():
			current = 1
			for integer in values:
				current *= int(integer)
			part_2_ids[key] = 0
			part_2_ids[key] += current

		for game in part_2_ids.values():
			part_2_answer += game

		print(part_2_answer)

part2(part_2_answer)