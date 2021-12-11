from Combo.Core.Text.Pattern import Pattern
import re
import types


class RegexPattern(Pattern):
    def __init__(self, name, pattern, fields, tags=[], version='', processors=[], excludes=[]):
        self.name = name
        self.pattern = pattern
        self.fields = fields
        self.all_tags = tags
        self.version = version
        self.processors = processors
        self.excludes = excludes
        self.matches = 0
        self.regex = re.compile(self.pattern)

    def pattern_id(self):
        return '{}@{}'.format(self.name, self.version) if self.version else self.name

    def pattern_name(self):
        return self.name

    def tags(self):
        return self.all_tags

    def match_count(self):
        return self.matches

    def match(self, s):
        result = self.regex.findall(s)
        if not result:
            return {}

        result = result[0] if isinstance(result[0], type(())) else result
        result_len = len(result) if type(result) in [type([]), type({}), type(())] else 1

        if result_len != len(self.fields):
            raise Exception("bad pattern for {}: length of fields mismatch!".format(self.pattern_id()))

        kv = {v[0]: v[1](result[i]) for i, v in enumerate(result)}
        self.matches += 1

        for p in self.processors:
            kv = p(self.name, kv) if isinstance(p, types.FunctionType) else p.process(self.name, kv)
        return kv
