# Note:
# \u2080 : subscript 0
# \u2081 : subscript 1
# \u2082 : subscript 2
# \u2083 : subscript 3
# \u2084 : subscript 4
# \u2205 : empty set or {}
# \u03B4 : delta
# \u0394 : Delta (delta hat)
# \u03B5 : epsilon


# Global Variables
# SAVER is used to save the next state
# TEMP is used to save the next state (temporary)
# ROW_SAVER is used to save the detail process for one row (one step)
# DETAIL_SAVER is used to save all of the detail process of the string
SAVER = set([])
TEMP = set([])
DETAIL_SAVER = []
ROW_SAVER = []


#
# Function delta_helper(state, string)
# This function is used to help the function delta_hat(state, string)..
# ..to get the detail process of ETF for NFA by appending the result..
# ..to the list ROW_SAVER.
# @param state : is the current state
# @param string : is the current string
# @return void : this function does not return anything
#
def delta_helper(state, string):
    if state == "q\u2080" and string[-1] == "1":
        ROW_SAVER.append("{q\u2081}")
    elif state == "q\u2081" and string[-1] == "0":
        ROW_SAVER.append("{q\u2084}")
    elif state == "q\u2081" and string[-1] == "1":
        ROW_SAVER.append("{q\u2082}")
    elif state == "q\u2082" and string[-1] == "0":
        ROW_SAVER.append("{q\u2082}, {q\u2083}")
    elif state == "q\u2082" and string[-1] == "1":
        ROW_SAVER.append("{q\u2082}")
    elif state == "q\u2084" and string[-1] == "0":
        ROW_SAVER.append("{q\u2084}")
    elif state == "q\u2084" and string[-1] == "1":
        ROW_SAVER.append("{q\u2081}")
    else:
        ROW_SAVER.append("\u2205")


#
# Function delta(state, string)
# This function takes state and the last character of the string..
# ..as input symbol and save the next state (can be more than one)..
# ..to the global variable TEMP.
# @param state : is the current state
# @param string : is the current string
# @return void : this function does not return anything
#
def delta(state, string):
    global TEMP
    ROW_SAVER.append("\u03B4(" + state + ", " + string[-1] + ")")
    if state == "q\u2080" and string[-1] == "1":
        TEMP.add("q\u2081")
    elif state == "q\u2081" and string[-1] == "0":
        TEMP.add("q\u2084")
    elif state == "q\u2081" and string[-1] == "1":
        TEMP.add("q\u2082")
    elif state == "q\u2082" and string[-1] == "0":
        TEMP.add("q\u2082")
        TEMP.add("q\u2083")
    elif state == "q\u2082" and string[-1] == "1":
        TEMP.add("q\u2082")
    elif state == "q\u2084" and string[-1] == "0":
        TEMP.add("q\u2084")
    elif state == "q\u2084" and string[-1] == "1":
        TEMP.add("q\u2081")


#
# Function delta_hat(state, string)
# This function takes a state and a string as input and..
# ..return the next state (can be more than one)..
# ..by calling the function delta_hat(state, string)..
# ..and call the function delta_helper(state, string)..
# ..to get the detail process of ETF for NFA..
# @param state : is the current state
# @param string : is the current string
# @return void : this function does not return anything
#
def delta_hat(state, string):
    # make sure that the global variable ROW_SAVER is empty
    ROW_SAVER.clear()
    # make variable SAVER and TEMP are accessible
    global SAVER
    global TEMP
    # if the string is empty (epsilon)
    if string == "\u03B5":
        ROW_SAVER.append("\u0394(" + state + ", \u03B5) =")
        TEMP.add(state)
    # otherwise (string is not empty)
    else:
        ROW_SAVER.append("\u0394(" + state + ", " + string + ") =")
        # function delta will be called to get the next state
        for i in SAVER:
            delta(i, string)
            if i != list(SAVER)[-1]:
                ROW_SAVER.append("\u222A")
            else:
                ROW_SAVER.append("=")
        # function delta_helper will be called to get the detail process
        for i in SAVER:
            if len(SAVER) > 1:
                delta_helper(i, string)
                if i != list(SAVER)[-1]:
                    ROW_SAVER.append("\u222A")
                else:
                    ROW_SAVER.append("=")
    # save the result to the global variable SAVER
    # ..and clear the global variable TEMP
    # ..so that the next state can be saved again
    SAVER = TEMP
    TEMP = set([])
    # append the result of the process to the global variable ROW_SAVER
    ROW_SAVER.append("{" + ", ".join(list(SAVER)) + "}")
    # for every function call, the result will be appended to DETAIL_SAVER
    DETAIL_SAVER.append(" ".join(ROW_SAVER))


#
# Function process_language(string)
# This function takes a string as input and process the string..
# ..by calling the function delta_hat(state, string) for each..
# ..character in the string (including the epsilon).
# @param string : is the input string
# @return void : this function does not return anything
#
def process_language(string):
    for i in range(-1, len(string)):
        if i == -1:
            delta_hat("q\u2080", "\u03B5")
        else:
            delta_hat("q\u2080", string[0:i+1])


#
# Function get_is_accepted(string)
# This function takes a string as input and return the..
# ..result of the string whether it is accepted or not.
# @param string : is the input string
# @return boolean : return True if the string is accepted, False otherwise
#
def get_is_accepted(string):
    process_language(string)
    # final state is q3 according to the transition diagram
    finalState = "q\u2083"
    if finalState in SAVER:
        return True
    else:
        return False


#
# Function get_detail_process(string)
# This function takes a string as input and return the..
# ..detail process of the string using global variable DETAIL_SAVER.
# @param string : is the input string
# @return string : a list that contais the detail process of the string
#
def get_detail_process(string):
    DETAIL_SAVER.clear()
    process_language(string)
    return DETAIL_SAVER
