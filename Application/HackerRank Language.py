# https://www.hackerrank.com/challenges/hackerrank-language/problem
import re
languages = ":C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC:"

for x in range(int(input())):
    text = input()
    if bool(re.match('^[1-9][0-9]{4}\s(\w+)$',text)):
        lanauge = re.findall('^[1-9][0-9]{4}\s(\w+)$',text)[0]
        lanauge = ':'+lanauge+':'
        if (lanauge in languages):
            print('VALID')
        else:
            print('INVALID')
    else:
        print('INVALID')