"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from distutils import sysconfig
their_parse_makefile = sysconfig.parse_makefile
def my_parse_makefile(filename, g):
    their_parse_makefile(filename, g)
    g['MACOSX_DEPLOYMENT_TARGET'] = '10.4'
sysconfig.parse_makefile = my_parse_makefile

import sys, os
from setuptools import setup

# current version of Artisan
VERSION = '0.5.2'
LICENSE = 'GNU General Public License (GPL)'

QTDIR = r'/Developer/Applications/Qt/'

APP = ['artisan.py']

DATA_FILES = [
    "index.html",
    "LICENSE.txt",
    ("../PlugIns/iconengines", [QTDIR + r'/plugins/iconengines/libqsvgicon.dylib']),
    ("../PlugIns/imageformats", [QTDIR + r'/plugins/imageformats/libqsvg.dylib']),
    ("../translations", [QTDIR + r'/translations/qt_de.qm']),
    ("../translations", [QTDIR + r'/translations/qt_es.qm']),
    ("../translations", [QTDIR + r'/translations/qt_fr.qm']),
    ("../translations", [QTDIR + r'/translations/qt_sv.qm']),
    ("../translations", [r"translations/artisan_de.qm"]),
    ("../translations", [r"translations/artisan_es.qm"]),
    ("../translations", [r"translations/artisan_fr.qm"]),
    ("../translations", [r"translations/artisan_it.qm"]),
    ("../translations", [r"translations/artisan_sv.qm"]),
  ]
  
OPTIONS = {
    'strip':True,
    'argv_emulation': False,
    'semi_standalone': False,
    'site_packages': True,
    'packages':[],
    'optimize':  2,
    'compressed':True,
    'iconfile': 'artisan.icns',
#    'frameworks' : ['/Developer/SDKs/MacOSX10.4u.sdk/usr/X11R6/lib/libfreetype.dylib'], # cannot be relocated!
    'includes': ['sip',
                 'serial',
                 'PyQt4.QtCore',
                 'PyQt4.QtGui',
                 'PyQt4.QtSvg',
                 'PyQt4.QtXml'],
    'excludes' :  ['_tkagg','_ps','_fltkagg','Tkinter','Tkconstants',
                      '_agg','_cairo','_gtk','gtkcairo','pydoc','sqlite3',
                      'bsddb','curses','tcl',
                      '_wxagg','_gtagg','_cocoaagg','_wx'],
    'plist'    : {  'CFBundleDisplayName': 'Artisan',
                    'CFBundleGetInfoString' : 'Artisan, Roast Logger',
                    'CFBundleIdentifier':'com.google.code.p.Artisan',
                    'CFBundleShortVersionString':VERSION,
                    'CFBundleVersion': 'Artisan ' + VERSION,
                    'LSMinimumSystemVersion':'10.4',
                    'LSMultipleInstancesProhibited':'false',
                    'NSHumanReadableCopyright':LICENSE
                }}

setup(
    name='Artisan',
    version=VERSION,
    author='YOUcouldbeTOO',
    author_email='zaub.ERASE.org@yahoo.com',
    license=LICENSE,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

            
os.system(r'cp README.txt dist')
os.system(r'cp LICENSE.txt dist')
os.chdir('./dist')
os.system(r'macdeployqt Artisan.app -verbose=0')

print '*** Removing Qt debug libs ***'
for root, dirs, files in os.walk('.'):
    for file in files:
        if 'debug' in file:
            print 'Deleting', file
            os.remove(os.path.join(root,file))
        elif 'test_' in file:
            print 'Deleting', file
            os.remove(os.path.join(root,file))
        elif '_tests' in file:
            print 'Deleting', file
            os.remove(os.path.join(root,file))
        elif '.pyc' in file:
            print 'Deleting', file
            os.remove(os.path.join(root,file))
        # remove also all .h .in .cpp .cc .html files 
        elif '.h' in file:
            print 'Deleting', file
            os.remove(os.path.join(root,file))
        elif '.in' in file:
            print 'Deleting', file
            os.remove(os.path.join(root,file))
        elif '.cpp' in file:
            print 'Deleting', file
            os.remove(os.path.join(root,file))
        elif '.cc' in file:
            print 'Deleting', file
            os.remove(os.path.join(root,file))
        # removing some frameworks that are not needed but added by macdeployqt
        elif file in ['QtDeclarative','QtNetwork','QtScript','QtXmlPatterns','QtSql']:
            print 'Deleting', file
            os.remove(os.path.join(root,file))
        # removing some plugins that are not needed but added by macdeployqt
        elif file in ['libqtaccessiblewidgets.dylib',
                'libqgenericbearer.dylib',
                'libqcncodecs.dylib',
                'libqjpcodecs.dylib',
                'libqkrcodecs.dylib',
                'libqtwcodecs.dylib',
                'libqtracegraphicssystem.dylib',
                'libtcpserver.dylib']:
            print 'Deleting', file
            os.remove(os.path.join(root,file))
            
os.chdir('..')
os.system(r"rm artisan-mac-" + VERSION + r".dmg")
os.system(r'hdiutil create artisan-mac-' + VERSION + r'.dmg -volname "Artisan" -fs HFS+ -srcfolder "dist"')
# otool -L dist/Artisan.app/Contents/MacOS/Artisan

