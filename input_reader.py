from constant_values import index_position_of_instruction_type, final_lines_without_line_breaks, length_of_line_breaks, index_of_first_numerical_values

class FileReader:
    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.__file = open(file_path, 'r')
        self.__data_lines = self.__file.readlines()
        self.__clean_line_breaks()

    def __clean_line_breaks(self):
        for index in range(len(self.__data_lines)-final_lines_without_line_breaks):  #removing line breaks from every line except last
            self.__data_lines[index] = self.__data_lines[index][:-length_of_line_breaks]
        self.__split_lines()


    def __split_lines(self):
        for index in range(len(self.__data_lines)):  #removing line breaks from every line except last
            self.__data_lines[index] =  self.__data_lines[index].split(" ")
        self.__reformat_lines()

    def __reformat_lines(self):
        for index in range(len(self.__data_lines)):
            self.__input_type = self.__data_lines[index][index_position_of_instruction_type]
            self.__reformatted_line = self.__data_lines[index]
            if self.__input_type == "ALLOCATE":  # excluding "balance" and "rebalance" input types because they have no numbers to reformat
                for pre_correction_index in range(index_of_first_numerical_values,len(self.__reformatted_line)):
                    self.__reformatted_line[pre_correction_index] = int(self.__reformatted_line[pre_correction_index])

            elif self.__input_type == "SIP":
                for pre_correction_index in range(index_of_first_numerical_values, len(self.__reformatted_line)):
                    self.__reformatted_line[pre_correction_index] = int(self.__reformatted_line[pre_correction_index])

            elif self.__input_type == "CHANGE":
                self.__divider_for_two_decimals = 100
                self.__change_index_borders = 1
                for pre_correction_index in range(self.__change_index_borders, len(self.__reformatted_line)-self.__change_index_borders):
                    self.__reformatted_line[pre_correction_index] = self.__reformatted_line[pre_correction_index][:-self.__change_index_borders] # to clip % sign
                    self.__reformatted_line[pre_correction_index] = float(self.__reformatted_line[pre_correction_index])/self.__divider_for_two_decimals


    def _get_instructions(self):
        #print(type(self.__data_lines))
        return self.__data_lines

    def _get_file_path(self): # stupid that i only made this for testing purposes
        return self.__file_path