# -*- coding: utf-8 -*-

from babel.messages.mofile import write_mo
from babel.messages.pofile import read_po
import zc.buildout

class CompileMo(object):
    def __init__(self, buildout, name, options):
        self.name = name
        base = buildout['buildout']['directory']

    def install(self):
        pass

    update = install
