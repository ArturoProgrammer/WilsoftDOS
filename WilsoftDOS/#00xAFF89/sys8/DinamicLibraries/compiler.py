import ply.lex as lex
import re
import codecs
import os
import sys

tokens = ['ID', 'ASSIGN', 'VALUE', 'NEXT', 'OPENL', 'ENDL', 'LISTREFBEGIN', 'LCORCHETE', 'RCORCHETE', 'LKEY', 'RKEY', 'ADDREF']

palabras_reservadas = {
	'#define' : 'DEFINITION',
	'block' : 'BLOCK',
	'referential' : 'REFERENTIAL',
	'#BEGIN#' : 'BEGIN',
	'#END#' : 'END',
	'public__' : 'PUBLIC__',
	'private__' : 'PRIVATE__'
}

tokens = tokens + list(palabras_reservadas.values())
t_ignore = '\t'
t_ASSIGN = r'='
t_LISTREFBEGIN = r'@'
t_LCORCHETE = r'\['
t_RCORCHETE = r'\]'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_ADDREF = r':'

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in keywords:
		t.value = t.value.upper()
		t.type = t.value

	return t

def t_COMMENT(t):
	r'\//*'
	pass

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_ERROR(t):
	print("CARACTER ILEGAL '%s'") % t.value[0]
	t.lexer.sikip(1)

directorio = ''