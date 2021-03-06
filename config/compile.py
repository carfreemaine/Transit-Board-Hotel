#!/usr/bin/python

# compile.py: create the JS object for the config tool

# Copyright 2011 Portland Transport

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

try:
    import json
except:
    import simplejson as json

# Open the HTML, CSS and JS files
html = open('config.html').read()
css  = open('config.css').read()
js   = open('config.js').read()

parsed = '<style>' + css + '</style>\n' +\
    '<script type="text/javascript">' + js + '</script>' +\
    html

# Get rid of hidden code
lines = parsed.split('\n')
deleting = False

outlines = ''
# Works on a per-line level
for line in lines:
    if '[compilehidden]' in line:
        deleting = True
    if not deleting:
        outlines += line + '\n'
    if '[/compilehidden]' in line:
        deleting = False

print json.dumps({"html": outlines})
