
# -*- python -*-
APPNAME = 'kalab'
VERSION = '1.00'

def options(opt):
    opt.load('compiler_cxx python')

def configure(conf):
    conf.load('compiler_cxx python')
    conf.check_python_version((2,4,2))
    conf.env.append_unique('CXXFLAGS', ['-O2'])
    conf.env.INCLUDES += '.'
    conf.env.LIB += ['pthread']

def build(bld):
    bld(features = 'cxx cprogram', source = 'fatt.cc', target = 'fatt')
    executables = ['convertsequence.pl']
    bld.install_files('${PREFIX}/scripts', executables, chmod=0755)