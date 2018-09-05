import json

from ipykernel.kernelbase import Kernel
import tracery
from tracery.modifiers import base_english

class TraceryKernel(Kernel):
    implementation = 'Tracery'
    implementation_version = '0.1'
    language = 'Tracery'
    language_version = '0.1'
    language_info = {
        'name': 'json',
        'mimetype': 'application/json',
        'file_extension': '.json',
    }
    banner = "Tracery - for making Jupyter Notebooks with Tracery!"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        try:
            grammar = tracery.Grammar(json.loads(code))
            grammar.add_modifiers(base_english)
            result = grammar.flatten("#origin#")
            if not silent:
                stream_content = {'name': 'stdout', 'text': result}
                self.send_response(self.iopub_socket, 'stream', stream_content)

            return {'status': 'ok',
                    # The base class increments the execution count
                    'execution_count': self.execution_count,
                    'payload': [],
                    'user_expressions': {},
                }
        except json.decoder.JSONDecodeError as e:
            if not silent:
                stream_content = {'name': 'stdout', 'text': "Error: " + str(e)}
                self.send_response(self.iopub_socket, 'stream', stream_content)
            return {'status': 'error',
                    'execution_count': self.execution_count,
                    'payload': [],
                    'user_expressions': {},
                }

