# interface.py
import os

def clear_screen():
    """Clears the terminal screen.
    Terminal ekranını temizler."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title, subtitle=None):
    """Prints a formatted header with optional subtitle.
    İsteğe bağlı alt başlıkla biçimlendirilmiş bir başlık yazdırır."""
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80
    line = "=" * terminal_width

    title_padding = (terminal_width - len(title)) // 2
    centered_title = ' ' * title_padding + title + ' ' * title_padding

    formatted_header = f"{line}\n{centered_title}\n"

    if subtitle:
        separator = "-" * terminal_width
        subtitle_padding = (terminal_width - len(subtitle)) // 2
        centered_subtitle = ' ' * subtitle_padding + subtitle + ' ' * subtitle_padding
        formatted_header += f"{separator}\n{centered_subtitle}\n"
    formatted_header += f"{line}\n"
    print(formatted_header)# interface.py
import os

def clear_screen():
    """Clears the terminal screen.
    Terminal ekranını temizler."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title, subtitle=None):
    """Prints a formatted header with optional subtitle.
    İsteğe bağlı alt başlıkla biçimlendirilmiş bir başlık yazdırır."""
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80
    line = "=" * terminal_width

    title_padding = (terminal_width - len(title)) // 2
    centered_title = ' ' * title_padding + title + ' ' * title_padding

    formatted_header = f"{line}\n{centered_title}\n"

    if subtitle:
        separator = "-" * terminal_width
        subtitle_padding = (terminal_width - len(subtitle)) // 2
        centered_subtitle = ' ' * subtitle_padding + subtitle + ' ' * subtitle_padding
        formatted_header += f"{separator}\n{centered_subtitle}\n"
    formatted_header += f"{line}\n"
    print(formatted_header)# interface.py
import os

def clear_screen():
    """Clears the terminal screen.
    Terminal ekranını temizler."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title, subtitle=None):
    """Prints a formatted header with optional subtitle.
    İsteğe bağlı alt başlıkla biçimlendirilmiş bir başlık yazdırır."""
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80
    line = "=" * terminal_width

    title_padding = (terminal_width - len(title)) // 2
    centered_title = ' ' * title_padding + title + ' ' * title_padding

    formatted_header = f"{line}\n{centered_title}\n"

    if subtitle:
        separator = "-" * terminal_width
        subtitle_padding = (terminal_width - len(subtitle)) // 2
        centered_subtitle = ' ' * subtitle_padding + subtitle + ' ' * subtitle_padding
        formatted_header += f"{separator}\n{centered_subtitle}\n"
    formatted_header += f"{line}\n"
    print(formatted_header)# interface.py
import os

def clear_screen():
    """Clears the terminal screen.
    Terminal ekranını temizler."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title, subtitle=None):
    """Prints a formatted header with optional subtitle.
    İsteğe bağlı alt başlıkla biçimlendirilmiş bir başlık yazdırır."""
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80
    line = "=" * terminal_width

    title_padding = (terminal_width - len(title)) // 2
    centered_title = ' ' * title_padding + title + ' ' * title_padding

    formatted_header = f"{line}\n{centered_title}\n"

    if subtitle:
        separator = "-" * terminal_width
        subtitle_padding = (terminal_width - len(subtitle)) // 2
        centered_subtitle = ' ' * subtitle_padding + subtitle + ' ' * subtitle_padding
        formatted_header += f"{separator}\n{centered_subtitle}\n"
    formatted_header += f"{line}\n"
    print(formatted_header)