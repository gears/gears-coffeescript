import os
from gears.compilers import ExecCompiler


class CoffeeScriptCompiler(ExecCompiler):

    result_mimetype = 'application/javascript'
    executable = 'node'
    params = [os.path.join(os.path.dirname(__file__), 'compiler.js')]

    def __init__(self, bare=False, **kwargs):
        super(CoffeeScriptCompiler, self).__init__(**kwargs)
        self.bare = bare

    def get_args(self):
        args = super(CoffeeScriptCompiler, self).get_args()
        if self.bare:
            args.append('--bare')
        return args
