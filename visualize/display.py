def print_colored_array(arr, highlight_indices=None, color="\033[91m"):
    highlight_indices = highlight_indices or []
    output = []
    for i, val in enumerate(arr):
        if i in highlight_indices:
            output.append(f"{color}{val}\033[0m")
        else:
            output.append(str(val))
    print(" ".join(output))


def print_colored_text(text, color="\033[94m"):
    print(f"{color}{text}\033[0m")


def print_dp_table(dp, row_highlight=None, col_highlight=None):
    for i, row in enumerate(dp):
        row_display = []
        for j, val in enumerate(row):
            if (row_highlight is not None and i == row_highlight) or \
               (col_highlight is not None and j == col_highlight):
                row_display.append(f"\033[92m{val}\033[0m")
            else:
                row_display.append(str(val))
        print(" ".join(row_display))
    print()