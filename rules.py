lex_rule = [ #Identifier, Keyword
    (r'[ \t]+', None),
    (r'#[^\n]*', None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'', None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"', None),
    (r'\n', "newline"),

    (r'[\+\-]?[0-9]*\.[0-9]+', "numbers"),
    (r'[\+\-]?[1-9][0-9]+', "numbers"),
    (r'[\+\-]?[0-9]', "numbers"),
    (r'\"[^\"\n]*\"', "string"),
    (r'\'[^\'\n]*\'', "string"),

    (r'\=(?!\=)', "equal"),
    (r'\==', "iseq"),
    (r'!=', "neq"),
    (r'<=', "le"),
    (r'<', "l"),
    (r'>=', "ge"),
    (r'>', "g"),
    (r'\(', "lp"), #left parenthesis
    (r'\)', "rp"), #right parenthesis
    (r'\[', "lsb"), #left square bracket
    (r'\]', "rsb"), #right square bracket
    (r'\{', "lcb"), #left curly bracket
    (r'\}', "rcb"), #right curly bracket
    (r'\:', "colon"), 
    (r'-=', "subtreq"),
    (r'\*=', "muleq"),
    (r'\+=', "sumeq"),
    (r'/=', "diveq"),
    (r'\->', "arrow"),
    (r'\+', "add"),
    (r'\-', "subtr"),
    (r'\*', "mul"),
    (r'/', "div"),
    (r'\,', "comma"),
    (r'\w+[.]\w+', "dotbetween"),
    (r'\.', "dot"),
    (r'\%', "mod"),
    (r'\c', "colon"),
    (r'\;', "semicolon"),
    (r'\&&', "and"),
    (r'\||', "or"),
    (r'\!', "not"),
    (r'\+\+', "increment"),
    (r'\-\-', "decrement"),

    (r'\bfunction\b', "function"),
    (r'\blet\b', "let"),
    (r'\bconst\b', "const"),
    (r'\band\b', "and"),
    (r'\bor\b', "or"),
    (r'\bnot\b', "not"),
    (r'\btrue\b', "true"),
    (r'\bfalse\b', "false"),
    (r'\bNone\b', "none"),
    (r'\bif\b', "if"),
    (r'\belse\b', "else"),
    (r'\bfor\b', "for"),
    (r'\bin\b', "in"),
    (r'\bwhile\b', "while"),
    (r'\bbreak\b', "break"),
    (r'\bcontinue\b', "continue"),
    (r'\breturn\b', "return"),
    (r'\btry\b', "try"),
    (r'\bcatch\b', "catch"),
    (r'\bfinally\b', "finally"),
    (r'\bswitch\b', "switch"),
    (r'\bdefault\b', "default"),

    (r'[A-Za-z_][A-Za-z0-9_]*', "var"),
  ]