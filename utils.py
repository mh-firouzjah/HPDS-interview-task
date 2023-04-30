"""This is an initial attempt to grab functions needed in this project"""
import subprocess


def get_memory_info() -> dict[str, int] | None:
    """returns a dict[str, int] represents 'total, used and free memory info, or None in case of failure.

    e.g: {'total': 16637, 'used': 4486, 'free': 7034}
    """
    try:
        byteOutput = subprocess.check_output(["free", "--mega"], timeout=2)
        """
        byteOutput -> b'               total        used        free      shared  buff/cache   available\nMem:           16637        3838        7982         367        4816       12082\nSwap:            536           0         536\n'
        """
        return dict(
            zip(
                ("total", "used", "free"),
                map(
                    int, byteOutput.decode("UTF-8").rstrip().split("\n")[1].split()[1:4]
                ),
            )
        )
    except subprocess.CalledProcessError as e:
        print("Error in 'free --mega':\n", e.output)
        return None
