import re

def makeBracePattern(brace, depth=32):  # depth: 能够匹配的最大深度
    pattern = r'\%s[^%s%s]*\%s' % (brace[0], brace[0], brace[1], brace[1])  # depth 0 pattern
    left = r'\%s(?:[^%s%s]|' % (brace[0], brace[0], brace[1])
    right = r')*\%s' % brace[1]
    while depth > 0:
        pattern = left + pattern + right
        depth -= 1
    return pattern

BRACES_PATTERN = makeBracePattern('{}')  # {{{}}}
BRACKETS_PATTERN = makeBracePattern('[]')
PARENTHESES_PATTERN = makeBracePattern('()')
