import sublime, sublime_plugin

class TypeScriptCompletionListener(sublime_plugin.EventListener):
    #def __init__(self):
    #    self.settings = sublime.load_settings("TypeScriptCompletion.sublime-settings");

    def on_query_completions(self, view, prefix, locations):
        if not view.file_name().endswith('.re'):
            return []

        return ([
            ("ami\t@<ami>{ ... }", "@<ami>{$1}"),
            ("b\t@<b>{ ... }", "@<b>{$1}"),
            ("bib\t@<bib>{ ... }", "@<bib>{$1}"),
            ("bibpaper\t//bibpaper[][]{ ... //}", "//bibpaper[$1][$2]{\n$3\n//}"),
            ("bou\t@<bou>{ ... }", "@<bou>{$1}"),
            ("br\t@<br>{}", "@<br>{}"),
            ("chap\t@<chap>{ ... }", "@<chap>{$1}"),
            ("chapref\t@<chapref>{ ... }", "@<chapref>{$1}"),
            ("cmd\t//cmd{ ... //}", "//cmd{\n$1\n//}"),
            ("code\t@<code>{ ... }", "@<code>{$1}"),
            ("column\t===[column] ... ===[/column]", "===[column] $1\n$2\n===[/column]"),
            ("comment\t@<comment>{ ... }", "@<comment>{$1}"),
            ("em\t@<em>{ ... }", "@<em>{$1}"),
            ("emlist\t//emlist{ ... //}", "//emlist{\n$1\n//}"),
            ("fn\t@<fn>{ ... }", "@<fn>{$1}"),
            ("footnote\t//footnote[][]", "//footnote[$1][$2]"),
            ("graph\t//graph[][][]{ ... //}", "//graph[$1][$2][$3]{\n$4\n//}"),
            ("hd\t@<hd>{ ... }", "@<hd>{$1}"),
            ("href\t@<href>{ ... }", "@<href>{$1}"),
            ("i\t@<i>{ ... }", "@<i>{$1}"),
            ("icon\t@<icon>{ ... }", "@<icon>{$1}"),
            ("image\t//image[][]{ ... //}", "//image[$1][$2]{\n$3\n//}"),
            ("img\t@<img>{ ... }", "@<img>{$1}"),
            ("indepimage\t//indepimage[]", "//indepimage[$1]"),
            ("kw\t@<kw>{ ... }", "@<kw>{$1,$2}"),
            ("lead\t//lead{ ... //}", "//lead{\n$1\n//}"),
            ("li\t@<list>{ ... }", "@<list>{$1}"),
            ("list\t//list[][]{ ... //}", "//list[$1][$2]{\n$3\n//}"),
            ("listnum\t//listnum[][]{ ... //}", "//listnum[$1][$2]{\n$3\n//}"),
            ("m\t@<m>{ ... }", "@<m>{$1}"),
            ("mapfile\t#@mapfile( ... ) ... #@end", "#@mapfile($1)\n$2\n#@end"),
            ("mapoutput\t#@mapoutput( ... ) ... #@end", "#@mapoutput($1)\n$2\n#@end"),
            ("maprange\t#@maprange( ... ) ... #@end", "#@maprange($1,$2)\n$3\n#@end"),
            ("noindent\t//noindent", "//noindent"),
            ("provide\t#@provide", "#@provide"),
            ("quote\t//quote{ ... //}", "//quote{\n$1\n//}"),
            ("raw\t@<raw>{ ... }", "@<raw>{|$1|$2}"),
            ("raw\t//raw[ ... //]", "//raw[|$1|$2]"),
            ("require\t#@require", "#@require"),
            ("ruby\t@<ruby>{ ... }", "@<ruby>{$1,$2}"),
            ("source\t//source[]{ ... //}", "//source[$1]{\n$2\n//}"),
            ("strong\t@<strong>{ ... }", "@<strong>{$1}"),
            ("table\t//table[][]{ ... //}", "//table[$1][$2]{\n$3\n//}"),
            ("tb\t@<table>{ ... }", "@<table>{$1}"),
            ("texequation\t//texequation{ ... //}", "//texequation{\n$1\n//}"),
            ("title\t@<title>{ ... }", "@<title>{$1}"),
            ("tt\t@<tt>{ ... }", "@<tt>{$1}"),
            ("tti\t@<tti>{ ... }", "@<tti>{$1}"),
            ("ttb\t@<ttb>{ ... }", "@<ttb>{$1}"),
            ("u\t@<u>{ ... }", "@<u>{$1}"),
            ("uchar\t@<uchar>{ ... }", "@<uchar>{$1}"),
            ("warn\t#@warn( ... )", "#@warn($1)"),
            ("emlist\t//emlist{ ... //}", "//emlist{\n$1\n//}")
        ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)


