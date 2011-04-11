# -*- coding: utf-8 -*-

import os
import logging
from babel.messages.mofile import write_mo
from babel.messages.pofile import read_po

class CompileMo(object):
    def __init__(self, buildout, name, options):
        self.name = name
        basedir = buildout['buildout']['directory']
        self.podir = os.path.join(basedir, options.get('po-directory'))

    def install(self):
        generated = []
        for dirpath, _, filenames in os.walk(self.podir):
            for filename in filenames:
                domain, ext = os.path.splitext(filename)
                if ext == '.po':
                    po = open(os.path.join(dirpath, filename))
                    mo = open(os.path.join(dirpath, domain + '.mo'), 'wb')
                    logging.getLogger(self.name).info(
                        "compiling catalog '%s' to '%s'"%(po.name, mo.name))
                    write_mo(mo, read_po(po))
                    generated.append(mo.name)
                    mo.close()

        return generated

    update = install
