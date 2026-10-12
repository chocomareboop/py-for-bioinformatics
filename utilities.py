

def colored(seq):
    'coloured output sequence'
    color_dict = {
        'A': '\033[91m',  # Red
        'C': '\033[92m',  # Green
        'G': '\033[93m',  # Yellow
        'T': '\033[94m',  # Blue
        'U': '\033[95m',  # Magenta
        'N': '\033[96m',  # Cyan
    }
    reset_color = '\033[0m'

    colored_seq = ''.join(color_dict.get(nuc, '') + nuc + reset_color for nuc in seq)
    print(colored_seq)