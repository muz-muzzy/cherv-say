def cherv_say(text="Я червяк"):
    message = \
    f"""
                                                \\
                                                    /~~\\
      ____                                         /'o  |
    .~  | `\\             ,-~~~\\~-_               ,'  _/'|
    `\\_/   /'\\         /'`\\    \\  ~,             |     .'
        `,/'  |      ,'_   |   |   |`\\          ,'~~\\  |
        |   /`:     |  `\\ /~~~~\\ /   |        ,'    `.'
        | /'  |     |   ,'      `\\  /`|      /'\\    /
        `|   / \\_ _/ `\\ |         |'   `----\\   |  /'
        `./'  | ~ |   ,'          |    |     |  |/'
        `\\   |   /  ,'            `\\ /      |/~'
         `\\/_ /~ _/                 `~------'
            ~~~~
    """

    max_width = 50
    words = text.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= max_width:
            current_line += f" {word}"
        else:
            lines.append(current_line.strip())
            current_line = f" {word}"
    
    if current_line.strip():
        lines.append(current_line.strip())
    
    print('\n' * 2)
    for line in lines:
        print('\t' * 4 + line)
    print(message)