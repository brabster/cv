#!/usr/bin/env python3

import yaml
from jinja2 import Environment, FileSystemLoader

if __name__ == "__main__":
    with open('./brabban.yml') as fh:
        data = yaml.safe_load(fh)

    env = Environment(
        loader = FileSystemLoader('.'),
        trim_blocks=True,
        lstrip_blocks=True,
        variable_start_string='{~',
        variable_end_string='~}')
    
    template = env.get_template('brabban_cv.jinja2')

    with open('uncommitted/brabban_cv.tex', 'w') as out_fh:
        out_fh.write(template.render(data))