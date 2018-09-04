#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gettext
import os

appName = 'i18n_demo'
languageDir = os.path.abspath('local')
gettext.bindtextdomain(appName, languageDir)
gettext.textdomain(appName)

_ = gettext.gettext

print _('This is a translatable string.')