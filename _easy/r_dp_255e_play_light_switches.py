import os

def get_binary(line, light_count):
    str_nums = line.split()
    nums = list(map(int, str_nums))
    nums.sort()
    string = ""
    for i in range(nums[0]):
        string += "0"
    for i in range(nums[0],nums[1]+1):
        string += "1"
    for i in range(nums[1]+1, light_count+1):
        string += "0"
    return int(string[::-1],2)

def main():
    read_first_line = False

    cwd = os.getcwd()
    path = os.path.join(cwd, '_res\\r_dp_255e_input_sm.txt')

    binary = 0b0

    with open(path) as f:
        for line in f:

            if not read_first_line:
                num_of_lights = int(line)
                read_first_line = True
                continue

            flipped_switches = get_binary(line, num_of_lights)
            binary = binary ^ flipped_switches

    print(bin(binary).count("1"))


if __name__ == "__main__":
    main()