import difflib

def calculate_similarity(input_str, db_str):
    sequence_matcher = difflib.SequenceMatcher(None, input_str, db_str)
    similarity_ratio = sequence_matcher.ratio()
    return similarity_ratio * 100 

correct_input = "Sons of Scotland, I am William Wallace. William Wallace is seven feet tall. Yes, I've heard. Kills men by the hundred. And if he were here, he'd consume the English with fireballs from his eyes and bolts of lightning from his arse. I am William Wallace, and I see a whole army of my countrymen, here in defiance of tyranny. You've come to fight as free men, and free men you are. What will you do without freedom? Will you fight? No! No! No! Fight? Against that? No! We will run, and we will live. I fight, and you may die. Run, and you'll live. At least a while. I'm dying in your beds many years from now. Would you be willing to trade all the days from this day to that for one chance, just one chance, to come back here and tell our enemies that they may take our lives, but they'll never take our freedom?"
user_input = "Sons of Scotland, I am e. William Wallace is seven fit tall. Yes, I've heard. Kills men by the hundred. And if he were here, he'd consume the English with balls from his eyes and bolts of light from his are. I am William Wallace, and I see a whole army of my country, here in defianse of tiranny. You've come to fight as free men, and free men you are. What will you do without fredom? Will you fight? No! Fight? Against that? No! We will run, and we will live. Fight, and you may die. Run, and you'll live. At least a while. I'm dying in your beds many years from now. Would you be willing to trade all the days from this day to that for one chance, just one chance, to come back here and tell our enemies that they may take our lives, but they'll never take our freedom?"

user_input_2 = "Sim, eu sou o nome do Andre"
correct_input_2 = "Sim, eu sou nami di Andre"

def highlight_differences(str1, str2):
    matcher = difflib.SequenceMatcher(None, str1, str2)
    differences = []
    for opcode, a0, a1, b0, b1 in matcher.get_opcodes():
        text = str1[a0:a1] if opcode != 'insert' else str2[b0:b1]
        differences.append({
            "type": opcode,
            "text": text
        })
    return differences

def highlight_differences_ansi(str1, str2):
    matcher = difflib.SequenceMatcher(None, str1, str2)
    output = []
    for opcode, a0, a1, b0, b1 in matcher.get_opcodes():
        if opcode == 'equal':
            output.append(str1[a0:a1])
        elif opcode in ['replace', 'delete']:
            output.append(f"\033[41m\033[97m{str1[a0:a1]}\033[0m")
        elif opcode == 'insert':
            output.append(f"\033[41m\033[97m{str2[b0:b1]}\033[0m")
    return ''.join(output)

