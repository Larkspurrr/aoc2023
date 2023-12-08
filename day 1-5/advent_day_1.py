import re

int_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
str_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

addends = {}
second_addends = {}

iteration = 0
second_iteration = 0

final_num = 0
second_final_num = 0

def part1(iteration, final_num):
	with open("day1list.txt", "r") as advent_list:
		for line in advent_list:
			addends[f"iteration{iteration}"] = ""
			for char in line:
				if char in int_numbers:
					addends[f"iteration{iteration}"] += str(char)
					break
			reversed_line = "".join(reversed(line))
			for char in reversed_line:
				if char in int_numbers:
					addends[f"iteration{iteration}"] += str(char)
					break
			iteration += 1

		for value in addends.values():
			final_num += int(value)

		print(f"Part 1: {final_num}")

part1(iteration, final_num)


def part2(second_iteration, second_final_num):
	with open("day1list.txt", "r") as advent_list:
		for line in advent_list:
			second_addends[f"it{second_iteration}"] = ""
			test_str = ""
			broken = False

			for char in line:
				if char in int_numbers:
					second_addends[f"it{second_iteration}"] += char
					break
				else:
					test_str += char
					for number in str_numbers:
						if re.search(number, test_str):
							index = str_numbers.index(number)
							second_addends[f"it{second_iteration}"] += int_numbers[index]
							test_str = ""
							broken = True
							break
				if broken:
					break

			broken = False
			reversed_line = "".join(reversed(line))
			for char in reversed_line:
				if char in int_numbers:
					second_addends[f"it{second_iteration}"] += char
					break
				else:
					test_str += char
					reversed_test_str = "".join(reversed(test_str))
					for number in str_numbers:
						if re.search(number, reversed_test_str):
							index = str_numbers.index(number)
							second_addends[f"it{second_iteration}"] += int_numbers[index]
							broken = True
							break
				if broken:
					break

			second_iteration += 1

		for value in second_addends.values():
			second_final_num += int(value)

		print(f"Part 2: {second_final_num}")

part2(second_iteration, second_final_num)
